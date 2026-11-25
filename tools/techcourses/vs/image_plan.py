# -*- coding: utf-8 -*-
"""Vascular Surgeon track: image plan (single source of truth).

    python3 tools/techcourses/vs/image_plan.py            # write figs.py, wire figure macros into m01-m20, write the prompt book
    python3 tools/techcourses/vs/image_plan.py --md-only  # prompt book only

Writes:
  tools/techcourses/vs/figs.py                   FIGS: key -> (file in images/, alt, caption) for the 40 teaching figures
  tools/techcourses/vs/mNN.py                    {{fig:vsNN_a}} / {{fig:vsNN_b}} after the first paragraph of the named section (idempotent)
  image-prompts/vascular-surgeon-image-plan.md   the GPT prompt book (also copied to the Academy working folder by the caller)

Every clinical label on a figure comes from the module text, which is PubMed- or guideline-verified (refs.py).
No figure carries a number that is not in the module. Images are produced in ChatGPT Image Generator, then
prepared with tools/techcourses/vs/prep_images.py.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HUB = "vascular-surgeon"
SLUGS = {
    "01": "the-surgeon-in-the-kidney-care-team", "02": "the-lifetime-access-plan", "03": "examine-and-preserve-the-vessels",
    "04": "mapping-and-choosing-an-access", "05": "make-the-patient-ready-for-surgery", "06": "plan-and-create-an-autogenous-fistula",
    "07": "grafts-and-alternative-configurations", "08": "dialysis-catheters-and-central-veins", "09": "maturation-and-the-first-cannulation",
    "10": "recognize-a-failing-access", "11": "stenosis-and-endovascular-choices", "12": "thrombosis-and-urgent-dialysis",
    "13": "hand-ischemia-and-neurologic-injury", "14": "aneurysm-and-life-threatening-bleeding", "15": "access-infection-and-sepsis",
    "16": "high-flow-and-central-venous-obstruction", "17": "the-difficult-access-and-changing-modality",
    "18": "kidney-care-beyond-the-access", "19": "philippine-documentation-and-quality", "20": "the-integrated-vascular-access-service",
}
TITLES = {
    "01": "The surgeon in the kidney care team", "02": "The lifetime access plan", "03": "Examine and preserve the vessels",
    "04": "Mapping and choosing an access", "05": "Make the patient ready for surgery", "06": "Plan and create an autogenous fistula",
    "07": "Grafts and alternative configurations", "08": "Dialysis catheters and central veins", "09": "Maturation and the first cannulation",
    "10": "Recognize a failing access", "11": "Stenosis and endovascular choices", "12": "Thrombosis and urgent dialysis",
    "13": "Hand ischemia and neurologic injury", "14": "Aneurysm and life threatening bleeding", "15": "Access infection and sepsis",
    "16": "High flow and central venous obstruction", "17": "The difficult access and changing modality",
    "18": "Kidney care beyond the access", "19": "Philippine documentation and quality", "20": "The integrated vascular access service",
}

# ───────────────────────── house rules shared by every figure prompt ─────────────────────────
FONT = "Inter"
FIG_NEG = ("Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, "
           "excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. "
           "NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, "
           "IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, "
           "pressures or thresholds that are not written in this prompt. Use American English spelling on every label. "
           "Never omit the renalcarematters.com attribution.")
FIG_QC = ("Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic "
          "(anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; "
          "renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.")
STYLE = (f"Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); "
         f"navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, "
         f"amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: {FONT} only, "
         f"bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. "
         f"Bottom-right corner: \"renalcarematters.com\" in small semi-transparent navy text (about 70% opacity).")
SIZES = {"land": ("16:9 landscape", "1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)"),
         "port": ("2:3 portrait", "1024 × 1536"), "card": ("4:3 card", "1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)"),
         "sq": ("1:1 square", "1024 × 1024")}

# ───────────────────────── the 40 teaching figures ─────────────────────────
# (key, file-descriptor, section id, skill, scaffold, size, title on image, body of the prompt, alt, caption)
F = [
 # 01
 ("vs01_a", "who-owns-what", "roles", "williamriveromd-simple-figure", "E Reference card", "card",
  "Three authorities, one patient",
  "A reference card with three stacked columns joined at the bottom by one patient icon. Column 1 header \"Dialysis facility\" (teal): "
  "\"Licensed by the DOH\", \"Staff, records, referral arrangements\". Column 2 header \"Attending nephrologist\" (navy): \"Kidney plan and "
  "dialysis prescription\", \"Coordinates access with the surgeon (PSN 2024, §1.2 b3)\". Column 3 header \"Surgeon\" (purple): \"Privileges "
  "from the operating hospital\", \"Creation, revision, salvage, ligation\". A green band across the bottom where the columns meet: "
  "\"The overlap is the access. Name an owner for every decision.\"",
  "Card comparing the dialysis facility, the attending nephrologist and the surgeon: who authorizes each and what each decides.",
  "Three authorities, one patient. The facility is licensed by the Department of Health (DOH), the attending nephrologist owns the "
  "dialysis prescription and coordinates access under the Philippine Society of Nephrology (PSN) 2024 guidelines, and the surgeon&rsquo;s "
  "authority comes from hospital privileges. Responsibility blurs where they overlap: the access."),
 ("vs01_b", "referral-triage-tree", "triage", "williamriveromd-algorithm-generator-skill", "A Clinical algorithm", "port",
  "Where does this access referral go?",
  "A top-to-bottom algorithm. Start node (navy): \"Access referral received\". Decision 1 (teal): \"Threat now? Bleeding, cold or weak "
  "hand, fever or low blood pressure, breathlessness\" -> YES -> red node \"Emergency pathway today: named receiving clinician and hospital\". "
  "NO -> Decision 2 (teal): \"Last session missed or failed?\" -> YES -> amber node \"Attending nephrologist decides on dialysis now, in "
  "parallel with the access plan\". NO -> green node \"Dated clinic or imaging slot, with instructions if it worsens\". All three end "
  "nodes flow into one final navy node: \"Close the loop: owner, time, read-back, fallback, record\".",
  "Decision tree that sends an access referral to the emergency pathway, to a parallel dialysis decision, or to a dated clinic slot.",
  "Where an access referral goes. Threats go to the emergency pathway the same day; a missed session goes to the attending "
  "nephrologist in parallel; everything else gets a dated slot. Every branch ends with a closed loop."),
 # 02
 ("vs02_a", "present-contingency-successor", "lifeplan", "williamriveromd-infographic-skill", "Journey (horizontal pathway)", "land",
  "One plan, three answers",
  "A horizontal journey along a gently curving path drawn over a faint schematic left-arm silhouette (labeled \"schematic\"). Three "
  "milestones as large rounded cards: 1 green \"Present access: what works now\", 2 amber \"Contingency: what if it fails\", 3 teal "
  "\"Successor: what comes after, and what to protect\". Beside the path, two small side branches leaving the arm: \"Peritoneal "
  "dialysis\" and \"Transplant\" with simple icons. A small shield icon over the right arm labeled \"Protect for later\". Footer strip: "
  "\"KDOQI 2019 ESKD Life-Plan: write the second and third plans before you need them.\"",
  "Pathway showing a present access, a contingency and a successor, with peritoneal dialysis and transplant as side branches.",
  "The Life-Plan in one picture. The Kidney Disease Outcomes Quality Initiative (KDOQI) end-stage kidney disease (ESKD) Life-Plan asks "
  "three questions in advance: what works now, what happens if it fails, and what comes after."),
 ("vs02_b", "association-not-causation", "evidence", "williamriveromd-simple-figure", "B Side-by-side comparison", "land",
  "What the access-type data can and cannot say",
  "Two equal panels. Left panel, green header \"What 62 cohorts found\": three horizontal bars comparing catheter users with fistula users, "
  "labeled exactly \"Death: risk ratio 1.53\", \"Fatal infection: risk ratio 2.12\", \"Cardiovascular events: risk ratio 1.38\". Under it "
  "a small note \"586,337 people, observational\". Right panel, amber header \"Why it is not the whole story\": three icon rows: \"Sicker "
  "patients more often get catheters\", \"Unplanned starts begin with catheters\", \"Exhausted sites leave only catheters\". Footer: "
  "\"Prefer a working fistula. Never promise that a fistula will work, or that it will prolong life.\"",
  "Two panels: the higher risks seen with catheters in cohort studies, and the confounders that explain part of that difference.",
  "Association, not proof. In a systematic review of 62 cohorts (586,337 people), catheter users had higher risks of death, fatal "
  "infection and cardiovascular events than fistula users, but sicker patients and unplanned starts explain part of the gap."),
 # 03
 ("vs03_a", "catheter-to-central-stenosis", "history", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "How old lines close future outflow",
  "Left panel: simplified upper torso (schematic) with the right internal jugular, subclavian and brachiocephalic veins and the superior "
  "vena cava in soft blue; a dialysis catheter and a pacemaker lead drawn in gray; a dashed connector to the inset. Center inset (dashed "
  "box): magnified vein wall where the catheter rubs, labels \"Endothelial injury\", \"Platelets and fibrin\", \"Smooth muscle growth\", "
  "\"Narrowed lumen\". Right small panel: an arm with a new fistula and swelling, label \"Arterial flow meets a blocked outflow\". Bottom "
  "row: pink box \"Catheters, device leads, PICCs injure veins\" -> blue box \"Ask about every line and device; image the central veins "
  "when at risk\" -> blue box \"The fistula is placed where it can drain\".",
  "Schematic of a catheter and pacemaker lead injuring a central vein, narrowing it, and later causing arm swelling after a fistula.",
  "How old lines close future outflow. Wall contact by catheters and device leads injures the endothelium; healing narrows the vein, "
  "and a fistula on that side later swells the arm. Schematic, not to scale."),
 ("vs03_b", "four-part-arm-exam", "exam", "williamriveromd-simple-figure", "C Horizontal step sequence", "land",
  "Examine both arms in four steps",
  "Four rounded cards in a row joined by arrows, each with a simple line icon of an arm. Card 1 teal \"Inflow\": \"Pulses\", \"Pressure "
  "in both arms\", \"Palmar arch\". Card 2 green \"Superficial veins\": \"Light tourniquet\", \"Continuity and depth\", \"Straight "
  "segment\". Card 3 amber \"Outflow warning signs\": \"Edema\", \"Chest-wall collaterals\", \"Device on that side\". Card 4 purple "
  "\"Hand baseline\": \"Color and refill\", \"Sensation\", \"Grip and pinch\". Footer strip: \"Record the hand before you touch it.\"",
  "Four-step arm examination: inflow, superficial veins, outflow warning signs and a recorded hand baseline.",
  "Examine both arms in four steps. The baseline hand examination is what lets you recognize a new deficit after surgery."),
 # 04
 ("vs04_a", "what-the-map-shows", "reading", "williamriveromd-simple-figure", "D Single mechanism poster", "land",
  "What a vessel map shows, and what it cannot",
  "A central schematic left arm (labeled \"schematic\") with radial and brachial arteries in red and cephalic vein in blue. Callout cards "
  "with green ticks: \"Arterial diameter and calcification\", \"Vein continuity, depth, branches\", \"Straight segment for two needles\". "
  "Callout cards with amber question marks: \"How the artery will dilate\", \"Wall quality and remodeling\", \"Skill of the cannulator\". "
  "A faded zone behind the clavicle marked with a red outline and the label \"Central veins: not seen on arm duplex\". Bottom strip: "
  "\"Never declare an access usable from diameter alone.\"",
  "Annotated arm schematic: what duplex mapping shows, what it cannot predict, and the central veins it cannot see.",
  "What a vessel map shows, and what it cannot. Diameter stands in for how a vessel will respond to flow; read it with depth, length "
  "and central outflow in mind."),
 ("vs04_b", "distal-first-tradeoff", "evidence", "williamriveromd-simple-figure", "B Side-by-side comparison", "land",
  "Distal first: a trade, not a rule",
  "Two panels with a balance-scale icon between them. Left panel teal \"Distal (forearm) first\": \"Keeps upper-arm sites for later\", "
  "\"Fails primarily more often\", \"Needs time to mature\". Right panel purple \"Proximal (upper arm) now\": \"More likely to mature\", "
  "\"Uses a site the future may need\", \"More hand ischemia with brachial inflow\". Footer: \"UKKA 2025, statement 3.2 (1B): favor distal "
  "sites when anatomy and preference allow. Time to dialysis tips the balance.\"",
  "Balance comparing a distal-first fistula with an upper-arm fistula: what each preserves and what each risks.",
  "Distal first is a trade. The UK Kidney Association (UKKA) 2025 guideline favors distal sites first (grade 1B); with little time "
  "before dialysis, the balance shifts upward."),
 # 05
 ("vs05_a", "potassium-and-the-heart", "threats", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "Why potassium stops an operation",
  "Left panel: a heart with an electrocardiogram strip showing tall peaked T waves. Inset (dashed box): one cardiac cell membrane with "
  "potassium ions outside rising, labels \"Higher outside potassium\", \"Membrane partly depolarized\", \"Slower conduction\". Inflow arrows "
  "into the potassium pool from four labeled sources: \"No kidney excretion\", \"Acidosis shifts potassium out of cells\", \"Tissue injury "
  "releases it\", \"Some anesthetic drugs raise it\". Bottom row: pink \"Missed dialysis, high potassium, peaked T waves\" -> blue \"Treat "
  "with the nephrologist and anesthesiologist; postpone elective surgery\" -> blue \"Operate when the threat is fixed\".",
  "Mechanism of hyperkalemia: four sources of potassium, a depolarized heart cell, peaked T waves, and the decision to postpone.",
  "Why potassium stops an operation. Rising outside potassium partly depolarizes heart cells and slows conduction; peaked T waves "
  "are the warning. An elective access benefit never outweighs this threat."),
 ("vs05_b", "day-of-surgery-readiness", "anesthesia", "williamriveromd-algorithm-generator-skill", "A Clinical algorithm", "port",
  "Day-of-surgery readiness",
  "Top-to-bottom checklist algorithm with four teal decision diamonds in sequence: \"Potassium and ECG acceptable?\", \"Can lie flat, "
  "no new breathlessness?\", \"No fever or bacteremia?\", \"Anticoagulant plan agreed?\". Every YES continues down; every NO branches "
  "right to an amber node \"Postpone. Name the owner of the fix\" with small owner tags: \"Nephrologist\", \"Nephrologist\", \"Treating "
  "team\", \"Prescriber with anesthesia\". Final green node: \"Proceed; huddle confirms anesthesia plan\". Bottom note: \"Readiness is "
  "checked on the day, not at the clinic visit.\"",
  "Four-question readiness algorithm on the day of access surgery, with an owner for each reason to postpone.",
  "Readiness is checked on the day. Each reason to postpone has a named owner, so the access plan survives the delay."),
 # 06
 ("vs06_a", "maturation-race", "maturation", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "Maturation is a race",
  "Left panel: a forearm with a radiocephalic fistula (schematic). Center inset (dashed box): the vein beyond the anastomosis split into "
  "two halves. Upper half in blue, label \"High flow -> shear stress -> nitric oxide -> outward remodeling, thicker wall\". Lower half "
  "at the swing segment in red, label \"Injury -> neointimal hyperplasia -> narrowed lumen\". A finish-line icon reading \"Usable for "
  "two needles\". Bottom row of four small failure cards: \"Inflow: small or calcified artery\", \"Juxta-anastomotic stenosis\", "
  "\"Deep or branched vein\", \"Outflow stenosis\". Footer: \"Median 115 days to maturation in the HFM study.\"",
  "Mechanism of fistula maturation: outward remodeling from shear stress racing against neointimal hyperplasia, with four failure routes.",
  "Maturation is a race between outward remodeling and neointimal hyperplasia. In the Hemodialysis Fistula Maturation (HFM) study, "
  "median time to maturation was 115 days."),
 ("vs06_b", "surrogate-versus-function", "drugs", "williamriveromd-simple-figure", "B Side-by-side comparison", "land",
  "A drug moved the surrogate, not the outcome",
  "Two panels, each with a pair of simple vertical bars (placebo gray, clopidogrel teal), exact labels on bars. Left panel title "
  "\"Early thrombosis (surrogate)\": placebo \"19.5%\", clopidogrel \"12.2%\", a green check. Right panel title \"Never suitable for "
  "dialysis (what matters)\": placebo \"59.5%\", clopidogrel \"61.8%\", an amber equals sign. Caption under panels: \"DAC trial, 877 "
  "patients, randomized\". Footer: \"Judge a fistula by use, not by patency.\"",
  "Bar pairs from the clopidogrel trial: less early thrombosis, but no more fistulas suitable for dialysis.",
  "A surrogate is not the outcome. In the Dialysis Access Consortium (DAC) trial, clopidogrel reduced early fistula thrombosis "
  "but did not increase the number of fistulas suitable for dialysis."),
 # 07
 ("vs07_a", "graft-venous-anastomosis", "why", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "Why grafts narrow at the venous end",
  "Left panel: a forearm loop graft (schematic) with the arterial end and the venous end labeled. Dashed inset at the venous end: a "
  "stiff graft joined to a soft vein, swirl arrows labeled \"Turbulence and vibration\", a stiffness gradient labeled \"Compliance "
  "mismatch\", and growing tissue inside the vein labeled \"Neointimal hyperplasia\". Bottom row: pink \"Venous anastomotic stenosis -> "
  "falling flow -> clot\" -> blue \"Watch the venous end; treat lesions that cause dysfunction\" -> blue \"A graft trades a maturation "
  "problem for a maintenance problem\".",
  "Schematic of a loop graft and its venous anastomosis, where turbulence and compliance mismatch drive narrowing.",
  "Why grafts narrow at the venous end. Turbulence and the mismatch between a stiff graft and a soft vein drive hyperplasia that "
  "slowly lowers flow until the graft clots."),
 ("vs07_b", "fistula-versus-graft-card", "when", "williamriveromd-simple-figure", "E Reference card", "card",
  "Fistula or graft: choosing with the patient",
  "A two-column comparison table with teal headers \"Fistula\" and \"Graft\" and five rows: \"Time to use\": \"Usually 3 to 6 months\" "
  "| \"Usually 2 to 4 weeks; early-cannulation grafts within days\"; \"Primary failure\": \"Common, about 1 in 4\" | \"Uncommon\"; "
  "\"Procedures to maintain\": \"Fewer once mature\" | \"More\"; \"Infection\": \"Lowest\" | \"Higher\"; \"Hand ischemia\": \"Usually "
  "later\" | \"More often early\". Footer: \"UKKA 3.4 (1C): a graft may be considered when early use is needed or anatomy is unfavorable.\"",
  "Table comparing fistula and graft for time to use, primary failure, maintenance, infection and timing of hand ischemia.",
  "Fistula or graft. A graft is a reasoned first choice when early use is needed or conventional anatomy is unfavorable (UKKA 2025, "
  "statement 3.4, grade 1C)."),
 # 08
 ("vs08_a", "central-veins-and-catheter-sites", "injury", "williamriveromd-simple-figure", "D Single mechanism poster", "land",
  "Where a catheter goes, and what it can cost",
  "A clean frontal schematic of the neck and upper chest veins (labeled \"schematic\"): right and left internal jugular, subclavian and "
  "brachiocephalic veins, superior vena cava, right atrium. A tunneled catheter in the right internal jugular marked with a green "
  "badge \"First choice (UKKA 5.1)\". The subclavian route crossed out in red with \"Avoid when other veins exist (UKKA 5.2)\". Red "
  "injury markers at the bends where veins pass under the clavicle labeled \"Wall injury -> stenosis\". A faint arm on each side "
  "labeled \"Future access drains here\". Bottom strip: \"Every catheter: why now, where, how checked, until when.\"",
  "Schematic of central veins showing the preferred right internal jugular site, the avoided subclavian route and stenosis sites.",
  "Where a catheter goes, and what it can cost. The UK Kidney Association (UKKA) favors the right internal jugular vein and avoiding "
  "the subclavian route, because injured central veins drain future arm access."),
 ("vs08_b", "stop-troubleshooting", "complications", "williamriveromd-algorithm-generator-skill", "A Clinical algorithm", "port",
  "Poor flow after insertion: when to stop",
  "Top node navy \"Poor catheter flow after insertion or exchange\". Decision teal \"Is the patient deteriorating? breathless, "
  "hypotensive, hypoxic, chest pain\". YES -> red node \"Stop using the catheter. Airway, breathing, circulation. Image the chest. "
  "Call senior and emergency team\" -> red node \"Do not reverse lines or keep dialyzing until position is confirmed\". NO -> amber "
  "node \"Systematic dysfunction work-up\" -> amber \"Thrombolytic lock (UKKA 6.2)\" -> purple \"Exchange where fibrin sheath "
  "disruption is available (UKKA 6.3)\". Footer: \"Resistance is information. The problem is the patient, not the flow rate.\"",
  "Algorithm for poor catheter flow: stop and escalate if the patient deteriorates; otherwise lock, then exchange.",
  "When to stop troubleshooting. A deteriorating patient after a catheter procedure turns a flow problem into an emergency."),
 # 09
 ("vs09_a", "robbin-criteria", "readiness", "williamriveromd-simple-figure", "E Reference card", "card",
  "Ultrasound and readiness: what the numbers showed",
  "A clean card with three horizontal bars showing the share of fistulas adequate for dialysis: green bar \"Both: vein at least 4 mm "
  "and flow at least 500 mL/min -> 95% (19 of 20)\"; amber bar \"Vein at least 4 mm (either flow) -> 89% (24 of 27)\" and amber bar "
  "\"Flow at least 500 mL/min (either diameter) -> 84% (26 of 31)\"; red bar \"Neither -> 33% (5 of 15)\". Small source line: "
  "\"Robbin 2002, 54 fistulas with known outcome\". Footer: \"Surrogates for usability. Add depth and a straight segment, judged together.\"",
  "Bar card of the Robbin criteria: share of fistulas adequate for dialysis when both, one, or neither ultrasound criterion was met.",
  "Ultrasound and readiness. In Robbin&rsquo;s study, 95% of fistulas meeting both diameter and flow criteria were adequate for dialysis, "
  "against 33% meeting neither. Depth and a usable straight segment still decide first use."),
 ("vs09_b", "patent-is-not-usable", "timing", "williamriveromd-simple-figure", "D Single mechanism poster", "land",
  "A thrill is not a usable fistula",
  "A central forearm fistula schematic with a glowing \"thrill\" icon near the anastomosis and four numbered problem callouts along it: "
  "1 \"Vein too deep to needle\" (cross-section showing depth below skin), 2 \"Large side branch steals flow\", 3 \"Narrowing beside the "
  "anastomosis\", 4 \"Segment too short or tortuous\". Each callout has a small green fix chip: \"Superficialization\", \"Branch "
  "ligation\", \"Imaging and angioplasty or revision\", \"Discuss another site\". Footer: \"Silence is not permission to cannulate.\"",
  "Fistula schematic with a thrill but four reasons it cannot yet be needled, each paired with its usual fix.",
  "A thrill is not a usable fistula. Depth, a diverting side branch, a juxta-anastomotic narrowing or a short segment can each "
  "block first use; each has a usual fix."),
 # 10
 ("vs10_a", "where-is-the-stenosis", "physiology", "williamriveromd-simple-figure", "B Side-by-side comparison", "land",
  "Reading the access: where is the narrowing?",
  "Two panels, each with a garden-hose-style access drawn over a forearm. Left panel red header \"Outflow stenosis\": the pinch near the "
  "outflow, the segment before it swollen; labels \"Pulsatile, firm\", \"Does not collapse when the arm is raised\", \"Needle sites bleed "
  "longer\", \"High venous pressure\", \"Arm swelling\". Right panel amber header \"Inflow stenosis\": the pinch near the artery, the "
  "access flat; labels \"Soft and flat\", \"Collapses when the arm is raised\", \"Poor blood flow\", \"More negative arterial pressure\". "
  "Footer: \"Compare with the patient&rsquo;s own baseline.\"",
  "Two panels: the bedside signs of an outflow stenosis versus an inflow stenosis.",
  "Where is the narrowing? Outflow lesions trap pressure; inflow lesions starve the access. Compare every sign with the patient&rsquo;s "
  "own baseline."),
 ("vs10_b", "preemptive-correction-forest", "evidence", "williamriveromd-simple-figure", "E Reference card", "card",
  "Fixing stenosis before it causes trouble",
  "A simple forest-plot style card with a vertical line at 1.0 labeled \"No effect\". Row 1 \"Access loss\": point at 0.81 with a "
  "horizontal line from 0.65 to 1.02 crossing the 1.0 line, label \"RR 0.81 (0.65 to 1.02): not significant\". Row 2 \"Thrombosis\": "
  "point at 0.79 with a line from 0.65 to 0.97, label \"RR 0.79 (0.65 to 0.97)\". Header: \"14 randomized trials, 1,390 people\". "
  "Footer: \"A scan finding in a working access is not, by itself, a reason to treat.\"",
  "Forest-plot card: preemptive stenosis correction reduced thrombosis but did not significantly reduce access loss.",
  "Fixing stenosis early. Across 14 randomized trials, preemptive correction reduced thrombosis but not access loss; treat the "
  "patient&rsquo;s problem, not the scan."),
 # 11
 ("vs11_a", "why-restenosis", "mechanism", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "Why stenoses come back, and how devices respond",
  "Left panel: an upper-arm access with a narrowed segment (schematic). Center inset (dashed box) in three small frames: \"Balloon "
  "stretches and tears the wall\" -> \"Recoil\" -> \"New neointimal hyperplasia\". Two therapy callouts: blue \"Drug-coated balloon: "
  "paclitaxel slows the cells that drive scar\", blue \"Stent graft: holds the lumen and walls off healing tissue\". Bottom row: pink "
  "\"Injury restarts the healing that caused the lesion\" -> blue \"Choose the device for the lesion and the next site\" -> blue \"Judge "
  "success by reliable dialysis\".",
  "Mechanism of restenosis after balloon angioplasty, with how drug-coated balloons and stent grafts aim to delay it.",
  "Why stenoses return. Balloon injury restarts neointimal hyperplasia; drug-coated balloons slow it and stent grafts wall it off, "
  "each with trade-offs."),
 ("vs11_b", "landing-zone", "future", "williamriveromd-simple-figure", "B Side-by-side comparison", "land",
  "Landing zone: protect the next site",
  "Two panels of the same upper-arm venous anatomy (schematic): graft-vein anastomosis, basilic vein, axillary vein junction. Left panel "
  "green \"Protects the contingency\": a stent graft ending before the junction, the axillary vein open and labeled \"Next access "
  "possible\". Right panel red \"Consumes the contingency\": a stent graft crossing the junction into the axillary vein, label \"Future "
  "site covered\". Footer: \"Agree the landing zone with the access team before deployment.\"",
  "Two diagrams: a stent graft ending before a venous junction versus one crossing it and covering the next access site.",
  "Landing zone. A convenient deployment across a venous junction can consume the patient&rsquo;s next access; agree where the device may land."),
 # 12
 ("vs12_a", "two-lanes", "two", "williamriveromd-infographic-skill", "Two-lane workflow", "land",
  "A clotted access: two jobs at once",
  "Two parallel horizontal lanes that merge on the right. Upper lane red header \"Dialysis safety (nephrologist and emergency team)\": "
  "steps \"Potassium and ECG\", \"Oxygen and volume\", \"Emergency treatment\", \"Dialysis, bridge catheter if needed\". Lower lane teal "
  "header \"Access salvage (surgeon or interventionist)\": steps \"How long silent?\", \"Surgical or endovascular\", \"Find the culprit "
  "lesion\", \"Confirm flow\". Both lanes merge into a green node \"Next session booked and confirmed\". Small note on the bridge "
  "catheter: \"Site chosen to protect the access arm\".",
  "Two-lane workflow: dialysis safety and access salvage run in parallel and meet at a confirmed next session.",
  "A clotted access means two jobs at once. Dialysis safety and salvage run in parallel, with a bridge catheter placed to protect the access arm."),
 ("vs12_b", "why-accesses-clot", "why", "williamriveromd-simple-figure", "E Reference card", "card",
  "Clues to why the access clotted",
  "A reference table with teal headers \"Clue before the clot\", \"Likely cause\", \"At salvage\" and four rows: \"Rising venous "
  "pressure, prolonged bleeding\" | \"Outflow stenosis\" | \"Image and treat the outflow\"; \"Weak, flat access in prior weeks\" | "
  "\"Inflow or juxta-anastomotic stenosis\" | \"Image the arterial side\"; \"Clot after a hypotensive session or diarrhea\" | \"Low flow "
  "from low pressure\" | \"Review target weight and drugs\"; \"Repeated clots, no lesion\" | \"Hypercoagulability or compression\" | "
  "\"Consider testing and teaching\". Footer: \"Remove the clot, then fix the reason it formed.\"",
  "Table linking clues before an access clot to the likely cause and what to do at salvage.",
  "Why the access clotted. Removing the clot without treating the culprit leads to another clot."),
 # 13
 ("vs13_a", "pressure-not-steal", "mechanism", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "Hand ischemia is a pressure problem",
  "Left panel: an arm with a brachial-based fistula (schematic) and a color gradient of perfusion pressure along the forearm arteries "
  "from teal near the elbow to pale red at the fingers, label \"Pressure falls toward the fingers\". Inset (dashed box): the artery beyond "
  "the anastomosis with a small reversed-flow arrow labeled \"Reversed flow: common, often harmless\". Risk chips: \"Diabetes\", "
  "\"Coronary disease\", \"Female\", \"Brachial inflow\". Bottom row: pink \"Arteries cannot enlarge; the access draws off pressure\" -> "
  "blue \"Grade it; find inflow stenosis or high flow\" -> blue \"Restore hand perfusion; the hand outranks the access\".",
  "Mechanism of access-related hand ischemia: falling perfusion pressure toward the fingers, with reversed flow shown as often harmless.",
  "Hand ischemia is a pressure problem. Reversed flow beyond the access is common; symptoms come when perfusion pressure in the hand "
  "falls too low."),
 ("vs13_b", "steal-grading-card", "grading", "williamriveromd-simple-figure", "E Reference card", "card",
  "Grade the threatened hand",
  "A four-row reference card with colored left bars. Row 1 green \"Grade 1, mild: pale or cool, no pain -> no treatment; document and "
  "review\". Row 2 amber \"Grade 2, moderate: pain on exercise or during dialysis -> treatment often needed; may be planned\". Row 3 red "
  "\"Grade 3, severe: rest pain, ulcer or necrosis -> prompt treatment\". Row 4 dark red with an alert icon \"Any grade with new weakness "
  "or numbness -> immediate surgical assessment\". Footer: \"A thrill reassures you about the access, never about the hand. (UKKA 2025)\"",
  "Card grading access-related hand ischemia from mild to severe, with new neurologic deficit as an immediate emergency.",
  "Grade the threatened hand. The UK Kidney Association (UKKA) grade links symptoms to urgency; new weakness or numbness needs "
  "immediate surgical assessment."),
 # 14
 ("vs14_a", "skin-threat-ladder", "why", "williamriveromd-simple-figure", "E Reference card", "card",
  "Read the skin over an aneurysm",
  "A vertical ladder of four illustrated skin swatches over an access bulge (clean illustration, no blood), from bottom to top: green "
  "\"Thick healthy skin: rotate sites, review\"; amber \"Rapid growth, rising venous pressure: image and treat the outflow\"; red \"Thin, "
  "shiny or discolored skin: do not cannulate; urgent review\"; dark red \"Ulcer, scab or recent bleed: do not cannulate; same-day "
  "surgical assessment\". Footer: \"A small bleed from threatened skin is a warning, not a resolved problem.\"",
  "Ladder of skin changes over an access aneurysm, from healthy to impending rupture, with the action for each.",
  "Read the skin over an aneurysm. Thin, shiny, ulcerated or scabbed skin means the barrier has almost gone; never needle it."),
 ("vs14_b", "two-finger-pressure", "teaching", "williamriveromd-simple-figure", "B Do / Don&rsquo;t comparison", "land",
  "Stopping an access bleed at home",
  "Two clean illustrated panels of a hand over an upper-arm access (no blood, no wound shown). Left panel green check \"Do\": two "
  "fingertips pressing firmly on one point, labels \"Press firmly on the spot\", \"Keep pressing\", \"Call for emergency help\". Right "
  "panel red cross \"Don&rsquo;t\": a bulky towel spread loosely, labels \"Bulky dressing spreads the pressure\", \"Do not lift to look\". "
  "Footer: \"Teach every patient and household. Most fatal access bleeds happen at home.\"",
  "Do and don&rsquo;t panels: two-finger focused pressure versus a loose bulky dressing for an access bleed.",
  "Stopping an access bleed. In a forensic series of 100 deaths, 81% of fatal access hemorrhages occurred at home, so every household "
  "should know focused two-finger pressure."),
 # 15
 ("vs15_a", "biofilm-versus-living-wall", "biology", "williamriveromd-biomedical-mechanism-figure", "Organ → inset → injury/benefit", "land",
  "Why foreign material keeps the infection",
  "Two magnified dashed insets side by side. Left inset \"Catheter or graft surface\": bacteria in a gel-like biofilm matrix on a gray "
  "synthetic surface, antibiotic molecules bouncing off, labels \"Biofilm forms within days\", \"Shielded from antibiotics and white "
  "cells\", \"Sheds into the blood\". Right inset \"Living fistula wall\": vessel wall with capillaries and immune cells reaching bacteria, "
  "label \"Perfused, defended tissue\". Bottom row: pink \"Same organism returns after treatment\" -> blue \"Sepsis care first, then "
  "source control\" -> blue \"Remove infected synthetic material when indicated\".",
  "Comparison of biofilm on a catheter or graft surface with a perfused, defended fistula wall.",
  "Why foreign material keeps the infection. Biofilm shields bacteria on synthetic surfaces; a living fistula wall can often clear "
  "infection with antibiotics."),
 ("vs15_b", "source-control-matrix", "sepsis", "williamriveromd-simple-figure", "E Reference card", "card",
  "Source control by access type",
  "Reference table with teal headers \"Access\", \"Why it matters\", \"Usual source control\" and four rows: \"Catheter\" | \"Biofilm on "
  "the surface\" | \"Exchange or removal for severe, recurrent or S. aureus infection\"; \"Graft, localized\" | \"Infected segment of "
  "synthetic material\" | \"Partial excision and bypass\"; \"Graft, extensive or with sepsis\" | \"Material cannot be sterilized\" | "
  "\"Total or near-total removal\"; \"Fistula\" | \"Living wall\" | \"Often antibiotics; surgery for abscess or bleeding\". A red banner "
  "above the table: \"Hypotension with an infected access = sepsis first\".",
  "Table of usual source control for an infected catheter, graft or fistula, under a sepsis-first banner.",
  "Source control by access type, after sepsis care has started."),
 # 16
 ("vs16_a", "access-heart-crosstalk", "physiology", "williamriveromd-organ-crosstalk-sigil-graphic", "Organ crosstalk sigil", "land",
  "The access and the heart",
  "Minimal monoline organ sigils on white: an arm with an access on the left, a heart in the center, lungs on the right, connected by "
  "dotted teal flow lines. Labels along the lines: \"Low resistance shunt\" (arm), \"Venous return rises\" (arm to heart), \"Cardiac "
  "output rises\" (heart), \"Most adapt without symptoms\" (green note), \"High flow in some: breathlessness\" (amber note toward lungs). "
  "A small caption chip: \"Access flow of 2.0 L/min or more: investigate, do not assume (small study)\".",
  "Minimal sigil diagram linking an arm access, the heart and the lungs through rising venous return and cardiac output.",
  "The access and the heart. An access lowers resistance and raises cardiac output; most patients adapt, and high flow prompts "
  "investigation rather than a diagnosis."),
 ("vs16_b", "breathlessness-tree", "options", "williamriveromd-algorithm-generator-skill", "A Clinical algorithm", "port",
  "Breathless with an access: find the mechanism",
  "Top node navy \"Breathless patient with an upper-arm access\". Five parallel teal test branches: \"Volume: weight trend, edema, "
  "response to fluid removal\", \"Access: flow and cardiac output\", \"Heart: ischemia, valves\", \"Anemia: hemoglobin\", \"Lungs and "
  "pulmonary pressure\". A purple node below \"Brief access compression: do heart rate and output fall?\" -> YES green \"Access "
  "contributes: discuss flow reduction (banding) with the team\"; NO amber \"Look elsewhere; keep the access\". Footer: \"State the "
  "mechanism before the operation.\"",
  "Algorithm for breathlessness in a patient with an access: test competing causes, then use brief compression before flow reduction.",
  "Find the mechanism. A fall in heart rate and output with brief access compression supports an access contribution; otherwise "
  "keep the access and look elsewhere."),
 # 17
 ("vs17_a", "access-chronology", "history", "williamriveromd-infographic-skill", "Timeline", "land",
  "Reconstruct the history before the next attempt",
  "A horizontal timeline on soft gray with year ticks labeled only \"Year 1\" to \"Year 7\". Above the line, access icons with outcome "
  "chips: \"Left forearm fistula: never matured\", \"Right forearm fistula: thrombosed\", \"Left upper-arm graft: repeated stenosis\". "
  "Below the line, intervention dots \"Angioplasty\" and \"Thrombectomy\" and catheter bars \"Jugular catheter\". At the right end a "
  "panel \"What remains\" with chips \"Central veins: image first\", \"Peritoneal dialysis\", \"Transplant\", \"Supportive care\". "
  "Footer: \"Every failure had a cause. Write it down.\"",
  "Timeline of a patient&rsquo;s accesses, interventions and catheters over seven years, ending with the options that remain.",
  "Reconstruct the history before the next attempt. A dated chronology with the reason each route failed prevents repeating a known mistake."),
 ("vs17_b", "paths-when-access-is-hard", "conference", "williamriveromd-simple-figure", "E Reference card", "card",
  "When access is hard: the paths to discuss",
  "Five horizontal cards stacked, each with an icon: \"Further upper-limb access: needs patent outflow; lower odds\"; \"Lower-limb or "
  "complex reconstruction: needs expertise and rescue capacity\"; \"Peritoneal dialysis: spares the veins; daily self-care\"; "
  "\"Transplant: fitness and a donor\"; \"Long-term catheter or conservative care: an informed choice\". A people icon at the top: "
  "\"Complex access conference with the patient\". Footer: \"No modality is a punishment for difficult vessels.\"",
  "Five paths for a patient with difficult access, from further upper-limb access to conservative care.",
  "When access is hard, discuss every path with the patient at a complex access conference."),
 # 18
 ("vs18_a", "routing-map", "interfaces", "williamriveromd-algorithm-generator-skill", "A Clinical algorithm", "port",
  "Not the access? Route it",
  "Top node navy \"Access patient with another vascular problem\". Four branches to colored destination nodes: \"Rest pain, toe wound, "
  "gangrene\" -> red \"Urgent vascular service\"; \"Sudden cold, painful, pale limb\" -> dark red \"Emergency vascular surgery\"; "
  "\"Transplant recipient: new hypertension or graft dysfunction\" -> purple \"Transplant team\"; \"Resistant hypertension, flash "
  "pulmonary edema\" -> teal \"Nephrologist with vascular input\". Final node: \"Warm handoff: call, findings, urgency, confirmed acceptance\".",
  "Routing algorithm for non-access vascular problems in dialysis patients, each to its own service.",
  "Not the access? Route it. Recognizing a problem and handing it to the right team is part of good access care."),
 ("vs18_b", "protect-residual-function", "kidney", "williamriveromd-simple-figure", "C Horizontal step sequence", "land",
  "Investigate without harming the kidneys",
  "Four cards in a row with arrows. 1 teal \"Ask what result you need\". 2 green \"Duplex first when it answers the question\". 3 amber "
  "\"If angiography: lowest effective contrast\". 4 purple \"Plan timing and fluids with the renal team\". Above the row a kidney icon "
  "with a water drop labeled \"Residual kidney function: worth protecting\". Footer: \"Contrast-associated AKI is the usual worry.\"",
  "Four steps to investigate a dialysis or late chronic kidney disease patient while protecting residual kidney function.",
  "Investigate without harming the kidneys. Residual function helps control fluid and potassium; choose the least harmful test that "
  "answers the question. AKI: acute kidney injury."),
 # 19
 ("vs19_a", "patency-definitions", "measures", "williamriveromd-simple-figure", "D Single mechanism poster", "land",
  "Three kinds of patency",
  "A horizontal timeline from \"Creation\" with event markers: \"Intervention to keep it open\", \"Thrombosis\", \"Thrombectomy\", "
  "\"Abandonment\". Three colored bars run from Creation: teal bar \"Primary patency\" ends at the first intervention or thrombosis; "
  "green bar \"Assisted primary patency\" passes through interventions and ends at thrombosis or abandonment; purple bar \"Secondary "
  "patency\" passes through interventions and thrombectomy and ends at abandonment. A separate gold bar \"Functional use\" labeled "
  "\"Actually used for dialysis\". Footer: \"SVS reporting standards. Patency is a surrogate; report use too.\"",
  "Timeline showing where primary, assisted primary and secondary patency end, with functional use shown separately.",
  "Three kinds of patency, as defined by the Society for Vascular Surgery (SVS) reporting standards. Patency is a surrogate; report "
  "functional use beside it."),
 ("vs19_b", "code-is-not-payment", "record", "williamriveromd-simple-figure", "C Horizontal step sequence", "land",
  "A code is not a payment",
  "Four separate cards with gaps between them (no arrows implying one follows from the other), each with a small check box: \"Procedure "
  "code: what was done\", \"Payer classification: how it is grouped\", \"Eligibility: patient, provider, accreditation\", \"Payable "
  "amount: rules on the date of service\". Under each card a small label \"Check separately\". Footer: \"Confirm current PhilHealth "
  "circulars with the claims lead. Never teach a fixed amount.\"",
  "Four separate checks: procedure code, payer classification, eligibility and payable amount.",
  "A code is not a payment. Each of the four questions is verified on its own, against the rules in force on the date of service."),
 # 20
 ("vs20_a", "pathway-ring", "pathway", "williamriveromd-infographic-skill", "Circular workflow", "sq",
  "Every handoff needs an owner",
  "A circular ring of seven connected nodes with small owner badges: \"Referral: accepting surgeon\", \"Planning: Life-Plan shared\", "
  "\"Creation: written handoff\", \"Maturation: assessed at 2 to 6 weeks\", \"First use: written plan\", \"Maintenance: clinical "
  "monitoring\", \"Rescue: emergency pathway\". In the center a patient icon with a coordinator badge: \"Pathway owner tracks and "
  "escalates\". One node outlined in red dashes labeled \"Orphaned step = no plan\".",
  "Circular access pathway of seven steps, each with an owner, around a coordinator who tracks the patient.",
  "Every handoff needs an owner. A pathway owner tracks the patient through each step and escalates delays; an orphaned step means there is no plan."),
 ("vs20_b", "capstone-rubric", "capstone", "williamriveromd-simple-figure", "E Reference card", "card",
  "Capstone: how the plan is judged",
  "A scoring card with five rows, each with three small boxes labeled 0, 1, 2: \"Patient goals and alternatives\", \"Assessment and "
  "evidence\", \"Justified intervention and future options\", \"Safety and contingency\", \"Communication and improvement\". A total box "
  "\"Pass: 8 of 10, every emergency recognized and escalated\". Footer: \"A defensible alternative is welcome when it is explained.\"",
  "Capstone rubric: five domains scored 0 to 2, with a pass mark of 8 of 10 and every emergency escalated.",
  "Capstone rubric. Five domains scored 0 to 2; a pass is 8 of 10 with every emergency recognized and escalated. Passing grants no privileges."),
]

# ───────────────────────── heroes (circular vignette, no text) ─────────────────────────
HERO_NEG = ("busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, "
            "repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, "
            "baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, "
            "neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field")
PH, ST, AN = "photorealistic editorial photograph", "photorealistic still-life", "semi-photorealistic 3D medical illustration"
H = [  # (id or "hub", style, archetype, camera, safe side, subject, audience, goal)
 ("hub", PH, "A Editorial Portrait", "environmental portrait, eye level", "upper-left",
  "a Filipino vascular surgeon in his early 50s with a broad square face, salt-and-pepper close-cropped hair and rimless glasses, navy scrubs "
  "under an open white coat, gently supporting the forearm of a seated patient in a dialysis chair while a dialysis nurse looks on; a bright "
  "modern Philippine hemodialysis unit softly blurred behind", "Mixed", "The surgeon&rsquo;s work continues in the dialysis chair."),
 ("01", PH, "H Clinical", "over-the-shoulder, slightly high", "right",
  "a Filipina surgeon in her late 30s with a long oval face, hair in a low bun, pearl stud earrings and light-blue scrubs, on a corridor phone "
  "call while writing on a clipboard; through a glass window behind her a lit dialysis unit with two nurses is softly blurred",
  "Clinicians", "A referral is a phone call that must end with an owner."),
 ("02", PH, "E Lifestyle", "wide-angle, table level", "upper-right",
  "an 80-year-old Filipina grandmother with short white permed hair and a floral duster, her cane hooked on the chair, and her daughter in her "
  "40s with a ponytail and office blouse, seated across a small clinic table from a male nephrologist; a simple hand-drawn arm sketch on paper "
  "lies between them", "Mixed", "Access planning is a family conversation about a whole life."),
 ("03", PH, "I Object Hero", "close-up, hands-only, side light", "left",
  "the two bare forearms of a Filipino man in his late 50s resting palms-up on a white examination pillow, one slightly fuller than the other, "
  "with a surgeon&rsquo;s gloved fingers lightly palpating the wrist; a pocket Doppler probe and a soft tape measure lie beside",
  "Clinicians", "Examine both arms; compare before you cut."),
 ("04", PH, "J Environmental Storytelling", "side profile, medium distance", "upper-left",
  "a Filipino sonographer in his late 20s with a buzz cut and slim build scanning the inner upper arm of a seated woman in her late 40s with "
  "shoulder-length wavy hair, the ultrasound screen glowing with a vein image, while a surgeon marks the skin with a skin marker",
  "Clinicians", "The map is drawn for construction and for needles."),
 ("05", PH, "H Clinical", "environmental portrait, low angle", "right",
  "a pre-operative bay where a Filipina anesthesiologist in her mid 40s with a short bob and teal cap, a young male surgeon with curly hair "
  "and a nurse review a printed lab sheet beside a man in his 60s lying on a trolley with a nasal oxygen cannula",
  "Clinicians", "Readiness is checked on the day."),
 ("06", AN, "F Anatomy", "three-quarter, studio", "upper-right",
  "a clean schematic forearm with a radial artery joined to a dilated cephalic vein, the vein visibly enlarged and thick-walled downstream of "
  "the anastomosis, rendered in renal reds and soft blues on an off-white background; no operative field",
  "Clinicians", "A fistula is a vein remodeled by flow."),
 ("07", ST, "I Object Hero", "overhead, macro", "lower-left",
  "a coiled soft white synthetic vascular graft resting on a sterile pale-teal drape beside a surgical skin marker and a folded forearm "
  "diagram card with no readable writing", "Clinicians", "A graft trades maturation for maintenance."),
 ("08", AN, "F Anatomy", "frontal, slight three-quarter", "upper-left",
  "a translucent upper torso showing the right internal jugular vein, brachiocephalic veins and superior vena cava with a tunneled dual-lumen "
  "catheter tip in the right atrium, central veins highlighted in soft blue", "Clinicians", "Catheters are bridges that wear the riverbanks."),
 ("09", PH, "A Editorial Portrait", "close portrait, eye level", "right",
  "a senior Filipino dialysis nurse in his 50s with a thin mustache, rounded face and white uniform marking a straight segment on a young "
  "woman&rsquo;s forearm fistula with a skin pen while a female surgeon in her 30s with braided hair watches", "Mixed", "Patent is not the same as usable."),
 ("10", PH, "J Environmental Storytelling", "rear three-quarter", "upper-right",
  "a Filipino man in his late 50s in a gray polo seated in a dialysis chair raising his access arm while a surgeon observes the fistula; a "
  "dialysis machine display glows softly blurred beside them", "Clinicians", "Read the access against its own baseline."),
 ("11", PH, "H Clinical", "wide-angle, high angle", "lower-right",
  "an angiography suite with a fistulogram on a large monitor showing a narrowing, two clinicians in lead aprons (a stocky interventional "
  "radiologist in his 40s and a lean female surgeon in her 50s with short gray hair) discussing the image", "Clinicians",
  "Choose the device that protects the next site."),
 ("12", PH, "J Environmental Storytelling", "over-the-shoulder", "upper-left",
  "an emergency bay where a breathless Filipino man in his late 60s sits upright with nasal oxygen, a nephrologist checks a monitor showing an "
  "ECG trace, and a surgeon feels his upper-arm graft", "Clinicians", "Dialysis safety and salvage run in parallel."),
 ("13", PH, "I Object Hero", "macro, hands-only", "right",
  "two hands of a Filipina woman in her 70s side by side on a white sheet, one slightly paler and cooler-toned, a clinician&rsquo;s fingers "
  "testing fingertip sensation with a cotton wisp", "Clinicians", "A thrill reassures about the access, never the hand."),
 ("14", PH, "I Object Hero", "close-up, side light", "upper-left",
  "a gloved hand pressing two fingers firmly on a gauze pad over an upper-arm fistula of a Filipino man in his 50s, a nurse calling for help "
  "softly blurred in the background; no visible blood", "Mixed", "Two-finger pressure and a call for help."),
 ("15", PH, "H Clinical", "environmental portrait, eye level", "right",
  "a Filipina woman in her 60s with short curly hair on an emergency trolley with an IV line, blood culture bottles on a tray, a young female "
  "nurse with glasses preparing the bottles and a surgeon examining a reddened forearm", "Clinicians", "Sepsis first, then source control."),
 ("16", PH, "H Clinical", "wide-angle, table level", "upper-right",
  "a small multidisciplinary meeting room where a cardiologist in her 40s wearing a hijab, a nephrologist in his 60s with a gray beard and a "
  "surgeon review an echocardiogram and a duplex flow study on two screens", "Clinicians", "State the mechanism before the operation."),
 ("17", PH, "E Lifestyle", "top-down over a table", "lower-left",
  "a conference table seen from above with old venogram films, a hand-drawn timeline of operations on paper with no readable words, a "
  "peritoneal dialysis bag and a transplant information folder, the hands of three clinicians and a patient pointing",
  "Clinicians", "Reconstruct the history before the next attempt."),
 ("18", PH, "A Editorial Portrait", "low angle, kneeling perspective", "upper-right",
  "a Filipino surgeon in his 40s with a lean face and short side-parted hair kneeling to examine the bare foot of an older man with diabetes "
  "seated on a clinic chair, his fistula arm resting on the armrest", "Clinicians", "Notice the problem the referral did not name."),
 ("19", ST, "I Object Hero", "overhead", "upper-left",
  "a laptop on a light table showing an unlabeled run chart, beside a stack of folders, a pen and a coffee cup, viewed from above; no "
  "readable text on the screen or paper", "Clinicians", "Honest measures make improvement possible."),
 ("20", PH, "B Journey", "side profile, wide", "right",
  "a young Filipina surgeon in her early 30s with a pixie cut presenting at a whiteboard showing a simple drawn pathway of connected circles "
  "with no words to a small panel of a nephrologist, a dialysis nurse and a quality lead", "Clinicians", "Every transition needs an owner."),
]

# ───────────────────────── tile images (16:9, no text, read at 320 px) ─────────────────────────
T = {
 "card": "a dialysis access surgeon&rsquo;s hands in gloves resting beside a schematic arm model with a highlighted fistula, a stethoscope and a "
         "clipboard on a pale teal surface",
 "01": "a desk phone, a referral slip with no readable text and a clipboard arranged around a small toy relay baton on a pale teal surface",
 "02": "three small path markers (green, amber, teal) placed along a curving ribbon on a white surface, with a tiny kidney model at the end",
 "03": "two plaster forearm models side by side on a white cloth, a pocket Doppler probe and a soft tape measure between them",
 "04": "a compact ultrasound probe on a folded towel beside a printed vein-map silhouette with no readable text and a skin marker",
 "05": "a pre-operative checklist board with four empty check boxes, an ECG strip with tall T waves and an anesthesia mask on a light tray",
 "06": "a clear acrylic model of a forearm with a red artery joined to a widening blue vein, studio light on white",
 "07": "a coiled white synthetic vascular graft on a pale teal sterile drape, macro view",
 "08": "a tunneled dual-lumen dialysis catheter laid in a gentle curve on a white tray beside a small anatomical heart model",
 "09": "a skin pen and a strip of medical tape marking a straight line on a plaster forearm model with a soft glow over the vein",
 "10": "a garden hose with a gentle pinch near its end on a white surface, a small pressure gauge beside it",
 "11": "a deflated angioplasty balloon catheter and a short covered stent graft on a sterile blue-green drape, macro view, no blood",
 "12": "two parallel ribbons, one red and one teal, merging into one green ribbon on a white surface",
 "13": "two hands resting side by side on a white sheet, one paler, a cotton wisp touching a fingertip",
 "14": "a folded gauze pad under two gloved fingertips pressing on a plaster arm model, no blood",
 "15": "two blood culture bottles and a petri dish with a faint biofilm sheen on a light lab bench",
 "16": "an anatomical heart model and a schematic arm model connected by a soft dotted teal line on white",
 "17": "old X-ray films fanned on a table beside a hand-drawn timeline with no readable words and a peritoneal dialysis bag",
 "18": "a clinician&rsquo;s gloved hands examining a foot model with a small toe dressing, a fistula arm model in the background",
 "19": "an overhead laptop showing an unlabeled run chart beside folders and a pen on a light desk",
 "20": "a ring of seven small connected wooden tokens on a white table with a single central token, soft daylight",
}

# ───────────────────────── OG share cards (1200 x 630, with title text) ─────────────────────────
OG_BG = {i: x for i, x in T.items()}


def hero_prompt(i, style, arch, cam, safe, subj, aud, goal):
    slug = HUB if i == "hub" else f"{HUB}-{i}-{SLUGS[i]}"
    scaf = "Scaffold A people" if style == PH else "Scaffold B still-life" if style == ST else "Scaffold C anatomy"
    p = (f"Square 1:1 {style} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas "
         f"diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: "
         f"{arch}. Camera: {cam}. Subject: {subj}, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject "
         f"60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the {safe} side of soft "
         f"gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic "
         f"grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely "
         f"NO text of any kind: no title, caption, label, logo, or watermark.")
    human = ("Hands only; skin tone, age and hand position differ from the previous image" if "hands-only" in cam else
             "Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, "
             "expression, activity, setting, camera distance and angle" if style == PH else "No people, or hands only")
    return slug, (f"FILE NAME: images/{slug}-vignette-hero.png\nIMAGE TYPE: Circular vignette hero v3 ({scaf})\n"
                  f"ASPECT RATIO: 1:1\nPIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)\nCOMPOSITION ARCHETYPE: {arch}\nCAMERA: {cam}\n"
                  f"HUMAN VARIATION: {human}\nAUDIENCE: {aud}\nVISUAL GOAL: {goal}\n\nPROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid {HERO_NEG}.\n\n"
                  f"QUALITY CHECK:\nCircle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; "
                  f"Filipino clinical context; no text; no operative field or blood.")


def tile_prompt(i, subj):
    name = f"images/{HUB}-card.webp" if i == "card" else f"images/{HUB}-{i}-card.webp"
    p = (f"16:9 landscape {ST if 'model' in subj or 'graft' in subj or 'tray' in subj else 'photorealistic editorial still-life'} for a course "
         f"tile that is shown as small as 320 × 180 px. Subject: {subj}. One bold, instantly readable subject filling the center 60% of the "
         f"frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high "
         f"contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear "
         f"margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.")
    return name, (f"FILE NAME: {name} (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)\nIMAGE TYPE: Course tile "
                  f"(16:9, no text)\nPIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360\nVISUAL GOAL: Recognizable at thumbnail size; "
                  f"signals the module&rsquo;s one idea.\n\nPROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid clutter, small details, people&rsquo;s "
                  f"faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.\n\nQUALITY CHECK:\nReadable at "
                  f"320 px; one subject; light background; no text.")


def og_prompt(i):
    if i == "hub":
        slug, title, sub, bg = HUB, "Vascular Surgeon", "20 modules · referral to rescue", T["card"]
    else:
        slug, title, sub, bg = f"{HUB}-{i}-{SLUGS[i]}", TITLES[i], f"Vascular Surgeon · Module {int(i)} of 20", T[i]
    out = f"images/og/{slug}-og.jpg"
    p = (f"Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal "
         f"(#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can "
         f"crop to 1.91:1 without losing anything. Left 55%: text block in {FONT}. Small chip at top in teal #1a6b72 with white text "
         f"\"RENAL CARE ACADEMY · PHYSICIANS TRACK\". Title in bold navy #0f1e2e, two lines at most: \"{title}\". Subtitle in teal: \"{sub}\". "
         f"Right 45%: a clean photorealistic still-life on a light surface: {bg}, softly lit, no faces. A thin teal rule under the title. "
         f"Bottom-right: \"renalcarematters.com\" in small semi-transparent navy text. Spell every word exactly as given, American English.")
    return out, (f"FILE NAME: {out} (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)\nIMAGE TYPE: OG / social share card\n"
                 f"ASPECT RATIO: 1.91:1\nPIXEL DIMENSIONS: 1200 × 630 (final)\nAUDIENCE: Clinicians\nVISUAL GOAL: A share preview that "
                 f"names the module and shows its one idea.\n\nPROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid extra words, misspellings, "
                 f"text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people&rsquo;s faces, visible blood, "
                 f"serif or decorative fonts, more than one subject. Never omit renalcarematters.com.\n\nQUALITY CHECK:\nTitle readable at "
                 f"600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.")


def fig_file(k, desc):
    n = k[2:4]
    return f"{HUB}-{n}-{desc}.webp"


def figs_py():
    lines = ['# -*- coding: utf-8 -*-', '"""Teaching figures for the Vascular Surgeon track: key -> (file in images/, alt text, caption).',
             'Generated by tools/techcourses/vs/image_plan.py; prompts in image-prompts/vascular-surgeon-image-plan.md.',
             'A figure renders only after its image exists in images/ (until then the page carries a "figure pending" comment)."""', "", "FIGS = {"]
    for k, desc, sec, skill, scaf, size, title, body, alt, cap in F:
        lines.append(f"    {k!r}: ({fig_file(k, desc)!r},\n        {alt!r},\n        {cap!r}),")
    lines.append("}")
    return "\n".join(lines) + "\n"


def wire_modules():
    changed = 0
    for k, desc, sec, *_ in F:
        n = k[2:4]
        p = HERE / f"m{n}.py"
        s = p.read_text(encoding="utf-8")
        macro = "{{fig:" + k + "}}"
        if macro in s:
            continue
        m = re.search(r'\(\s*"' + re.escape(sec) + r'",\s*\n?\s*"[^"]*",\s*\n?\s*"[^"]*",\s*"""', s)
        if not m:
            raise SystemExit(f"section {sec} not found in m{n}.py for {k}")
        start = m.end()
        end_p = s.find("</p>", start)
        s = s[:end_p + 4] + "\n" + macro + s[end_p + 4:]
        p.write_text(s, encoding="utf-8"); changed += 1
    return changed


def book():
    o = ["# Vascular Surgeon track: image plan blueprint and GPT prompt book", "",
         "Renal Care Academy → Renal Care Physicians Track → Vascular Surgeon. Prepared November 25, 2026. American English throughout.", "",
         "## 1. Why these images", "",
         "Every picture in this track has one job: make a decision easier to understand, apply, or remember. The plan follows the "
         "track&rsquo;s teaching sequence (intuition → physiology → evidence → practice), so each module gets:", "",
         "| Image | Purpose in learning | Where it appears | Count |", "| --- | --- | --- | --- |",
         "| **Circular vignette hero** | Sets the scene and the emotional stakes (appreciation): who is involved, where, and what is at risk | Top of each module page and the course home; source of the page&rsquo;s share image if no OG card exists | 21 |",
         "| **Teaching figure A** | Mechanism or anatomy (understanding): why the decision makes physiologic sense | After the first paragraph of the physiology/mechanism section | 20 |",
         "| **Teaching figure B** | Decision tool, evidence picture or checklist (application): what to do, and how strong the evidence is | After the first paragraph of the evidence or practice section | 20 |",
         "| **Course tile** | Recognition on the syllabus and Academy landing (navigation) | Module cards on the course home; the course card | 21 |",
         "| **OG share card** | A share preview that names the module and its idea (reach) | `og:image` on Facebook, Viber, Messenger, X, LinkedIn | 21 |",
         "| **Track share-card art** | Background art for the Academy&rsquo;s composited track card | `images/academy/og-art/vascular-surgeon.webp`, text added by `build_academy_og.py` | 1 |",
         "| **Landing tile** | The Vascular Surgeon card on `academy/index.html` | `images/academy/landing/vascular-surgeon.webp` | (made from the course tile) |", "",
         "**Total: 104 prompts** (21 heroes, 40 teaching figures, 21 tiles, 21 OG cards, 1 track art).", "",
         "## 2. Rules that apply to every image", "",
         "- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c, purple #6c3d8e.",
         "- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). No serif or decorative type. American English spelling on every label.",
         "- **Attribution:** teaching figures and OG cards carry `renalcarematters.com` bottom-right (bottom-center for portrait). Heroes and tiles carry no text at all.",
         "- **Safety for a surgical track:** no visible blood, open wounds, needles in skin, or operative step sequences. Anatomy is drawn as a schematic and the caption says so. No figure carries a dose, diameter, pressure or threshold that is not written in its prompt; every number in a prompt is already in the module and verified against its source.",
         "- **People:** Filipino patients and clinicians, a different cast in every image (age, sex, face, hair, clothing, posture, camera).",
         "- **Skills used:** `williamriveromd-hero-vignette` (heroes), `williamriveromd-simple-figure`, `williamriveromd-algorithm-generator-skill`, `williamriveromd-biomedical-mechanism-figure`, `williamriveromd-organ-crosstalk-sigil-graphic` and `williamriveromd-infographic-skill` (teaching figures, tiles, OG cards).", "",
         "## 3. Production workflow", "",
         "1. Generate each prompt below in ChatGPT Image Generator. Save the PNG with the exact FILE NAME stem shown into `images/incoming/vascular-surgeon/` in the repo.",
         "2. Run `python3 tools/techcourses/vs/prep_images.py`. It converts and places every file: heroes to `images/<slug>-vignette-hero.png` + `.webp`; teaching figures to `images/<file>.webp` (+ `.png`); tiles to 640 × 360 WebP; the landing tile to 960 × 540; OG cards to 1200 × 630 JPEG ≤ 300 KB in `images/og/`; the track art to `images/academy/og-art/vascular-surgeon.webp`.",
         "3. Rebuild: `python3 generate_tech_courses.py --course vs --patch`, then `python3 build_academy_og.py --art images/academy/og-art --only vascular-surgeon --patch`, `python3 generate_rg_thumbs.py`, `python3 patch_rg_card_thumbs.py`, `python3 patch_responsive_images.py`.",
         "4. Check one module in light and dark mode, and paste one module URL into the Facebook Sharing Debugger.", "",
         "Figures are already wired into the modules (`tools/techcourses/vs/figs.py` and `{{fig:…}}` macros), so a page shows each figure as soon as its file exists.", "",
         "## 4. Image map by module", "", "| Module | Hero idea | Figure A (understand) | Figure B (apply) |", "| --- | --- | --- | --- |"]
    figmap = {}
    for k, desc, sec, skill, scaf, size, title, *_ in F:
        figmap.setdefault(k[2:4], []).append(title)
    for i, style, arch, cam, safe, subj, aud, goal in H:
        if i == "hub":
            continue
        a, b = figmap[i]
        o.append(f"| {int(i)}. {TITLES[i]} | {goal} | {a} | {b} |")
    o += ["", "## 5. Track-level images", ""]
    slug, txt = hero_prompt(*H[0])
    o += ["### Course home hero", "", "```", txt, "```", ""]
    name, txt = tile_prompt("card", T["card"])
    o += ["### Course tile and Academy landing tile", "", "Make one master; the prep script writes both `images/vascular-surgeon-card.webp` (640 × 360) and `images/academy/landing/vascular-surgeon.webp` (960 × 540).", "", "```", txt, "```", ""]
    name, txt = og_prompt("hub")
    o += ["### Course home OG card", "", "```", txt, "```", ""]
    o += ["### Track share-card art (Academy composited card)", "", "```",
          "FILE NAME: images/academy/og-art/vascular-surgeon.png (prep script writes .webp)\nIMAGE TYPE: Background art for build_academy_og.py\n"
          "PIXEL DIMENSIONS: 1536 × 1024\n\nPROMPT:\n16:9-like 3:2 landscape photorealistic editorial still-life on a light background: "
          + T["card"] + ". Keep the LEFT 45% as clean, light, empty negative space (the builder places the track title, group label and stats "
          "there). Soft daylight, gentle depth of field, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark.\n\n"
          "NEGATIVE INSTRUCTIONS:\nAvoid text, faces, clutter, dark backgrounds, visible blood, needles in skin.\n\nQUALITY CHECK:\nLeft 45% empty and light; subject on the right; no text.", "```", ""]
    o += ["## 6. Module prompts", ""]
    for i in SLUGS:
        o += [f"### Module {int(i)}: {TITLES[i]}", ""]
        h = [x for x in H if x[0] == i][0]
        slug, txt = hero_prompt(*h)
        o += ["**Hero (circular vignette)**", "", "```", txt, "```", ""]
        for k, desc, sec, skill, scaf, size, title, body, alt, cap in [x for x in F if x[0][2:4] == i]:
            ratio, px = SIZES[size]
            fn = fig_file(k, desc).replace(".webp", ".png")
            o += [f"**Figure {k[-1].upper()}: {title}**  ·  skill `{skill}`  ·  placed in section `{sec}`", "", "```",
                  f"FILE NAME: images/{fn}\nIMAGE TYPE: {scaf}\nASPECT RATIO: {ratio}\nPIXEL DIMENSIONS: {px}\nAUDIENCE: Clinicians (surgeons and trainees)\n"
                  f"VISUAL GOAL: {re.sub('<[^>]+>', '', cap).split('. ')[0]}.\n\nPROMPT:\nTitle at top: \"{title}\". {body} {STYLE}\n\n"
                  f"NEGATIVE INSTRUCTIONS:\n{FIG_NEG}\n\nQUALITY CHECK:\n{FIG_QC}", "```", "",
                  f"*On-page caption:* {cap}", f"*Alt text:* {alt}", ""]
        name, txt = tile_prompt(i, T[i])
        o += ["**Course tile**", "", "```", txt, "```", ""]
        name, txt = og_prompt(i)
        o += ["**OG share card**", "", "```", txt, "```", ""]
    o += ["## 7. Checklist before publishing", "",
          "- [ ] Every label spelled exactly as in the prompt (GPT often misspells: compare letter by letter).",
          "- [ ] No number appears on an image that is not in its prompt.",
          "- [ ] Anatomy figures show \"schematic\" and no dimensions; no blood, wounds or needles in skin.",
          "- [ ] `renalcarematters.com` visible on every teaching figure and OG card.",
          "- [ ] Heroes: circle with white margin, empty title-safe zone, no text.",
          "- [ ] Tiles readable at 320 px; OG titles readable at 600 px.",
          "- [ ] Module pages checked in light and dark mode after the rebuild."]
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    import html as _h
    md = _h.unescape(book()).replace(" -> ", " → ")
    out = ROOT / "image-prompts" / "vascular-surgeon-image-plan.md"
    out.write_text(md, encoding="utf-8")
    print("wrote", out.relative_to(ROOT), f"({md.count('FILE NAME:')} prompts)")
    if "--md-only" not in sys.argv:
        (HERE / "figs.py").write_text(figs_py(), encoding="utf-8")
        print("wrote figs.py with", len(F), "figures; wired", wire_modules(), "figure macros")
