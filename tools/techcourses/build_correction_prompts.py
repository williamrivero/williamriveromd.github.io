#!/usr/bin/env python3
"""Correction prompt pack for technician-track figures that failed the visual accuracy audit (November 23, 2026).

    python3 tools/techcourses/build_correction_prompts.py

Writes docs/tech-courses/GPT-IMAGE-PROMPTS-CORRECTIONS.md. Each corrected figure is saved under its ORIGINAL
filename, so it replaces the published image with no code change."""
import copy, importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


B = load("build_image_brief")
PREPARED = "November 23, 2026"

# id -> (problem found in the audit, overrides for the figure spec)
FIX = {
"HD-05-C": ("The bins are drawn yellow for sharps and red for infectious waste. Philippine Department of Health coding uses yellow for infectious waste and red for sharps, so the picture teaches the reverse of local practice.",
  {"truth": "Three containers drawn in NEUTRAL light gray, each with a blank colored tab left white so that no color code is asserted: a rigid puncture-resistant sharps container with a narrow opening (needles), a lidded infectious waste bin (blood-contaminated gauze, used bloodlines and dialyzers), and a lidded general waste bin (clean packaging). A gloved technician drops a used bloodline into the infectious bin. A small no-recapping symbol.",
   "negatives": ["No yellow, red, black, or green bins or bags", "No color named or implied as the code", "No hands near an open sharps opening", "No overfilled container"]}),
"HD-07-A": ("The distribution loop is a closed ring that never returns to the reverse osmosis unit, and the station is fed from the riser rather than from a drop off the loop.",
  {"truth": "Left-to-right train on one wall: feed water, sediment filter (particles), softener (hardness), carbon tank 1 then carbon tank 2 in series with a sample port after each, reverse osmosis unit with a reject line to drain. From the reverse osmosis product outlet a single distribution loop runs out along the ceiling, passes ABOVE the dialysis station where a short drop feeds the machine, and continues back to the reverse osmosis unit, ending in a clear return arrow at the reverse osmosis inlet. Arrows show one direction of flow throughout.",
   "negatives": ["No single carbon tank", "No loop that dead-ends or forms a closed ring disconnected from the reverse osmosis unit", "No station fed from anywhere but a short drop off the loop", "No numeric limits"]}),
"HD-09-B": ("The bloodlines run from the arm straight into the machine body with no blood pump or dialyzer, and the observer wears the nurse's purple scrubs.",
  {"truth": "Patient seated in a dialysis chair, access arm uncovered and resting in view, two needles taped in place. Bloodlines run from the arm to the machine front, through the roller blood pump, up to a vertically mounted dialyzer on the side of the machine, and back through the venous drip chamber to the arm (arterial line red, venous line blue). A technician in NAVY scrubs with a clipboard observes. Five numbered callouts: the patient, the access, the lines, the machine, the record. Screen values indistinct.",
   "negatives": ["No blanket covering the access", "No bloodlines entering the machine body without passing the blood pump and dialyzer", "No purple scrubs on the technician", "No readable numbers on the screen", "No needle close-up"]}),
"WATER-02-B": ("The drawing is a closed ring with no water source or treatment equipment, so the loop returns to nothing.",
  {"truth": "Clean engineering-style schematic on white, flow left to right: an inlet labeled by its symbol from a reverse osmosis unit (drawn as a simple box) feeds a pump, then a valve, a pressure gauge, and a sample port on the outgoing pipe; the loop runs right, turns, and comes back along the bottom as the loop return into the reverse osmosis box; a branch with an air gap leads down to a floor drain. A legend panel at top left explains each symbol.",
   "negatives": ["No closed ring without a source", "No manufacturer title block", "No dimensions", "No dead-end branches"]}),
"WATER-04-A": ("The required label 'Chlorine-free water out' is missing, an invented label replaces it, and the chlorine dots that show removal are not drawn.",
  {"truth": "Two carbon tank cutaways in series, flow left to right. Many small green chlorine dots in the inlet pipe, a few dots between the tanks, none in the outlet pipe. Sample port 1 between the tanks, sample port 2 after tank 2.",
   "negatives": ["No single-tank layout", "No parallel arrangement", "No label other than the verbatim list", "No numeric limits"]}),
"WATER-04-C": ("All four outcome labels differ from the plan, a reading at the limit is shown as a fail, and the tank 2 failure says HOLD rather than STOP.",
  {"canvas": "landscape",
   "truth": "Decision tree, top to bottom, large readable type filling the canvas. Top box: test after tank 1. Two branches. Left (green): at or below the limit, record and release. Right (amber): above the limit, test after tank 2 now. From the amber box two branches: tank 2 within limit (amber), report, replace the worker, test more often; tank 2 above limit (red), STOP and report, no treatments start or continue.",
   "negatives": ["No numeric limit printed", "No wording other than the verbatim labels", "No path that continues treatment after a tank 2 failure", "No small text"]}),
"WATER-08-B": ("The two good-log rows give the same port and time, so one reading is recorded as both 60 psi and 'instrument unavailable'; the corrected value also reads '60 TA'.",
  {"truth": "Left: a weak log row with ticks, 'OK', and a blank cell, crossed out in amber. Right: two strong log rows. Row 1: 60, psi, filter inlet, 07:00, Tech A, with an earlier value struck through by one line and initialed. Row 2: instrument unavailable, N/A, filter outlet, 07:05, Tech A.",
   "labels": "Ticks and OK: not evidence | Number, unit, port, time, name | Correct with one line and initials | No blanks: write why",
   "negatives": ["No real names", "No two rows with the same port and time", "No stray letters after a number", "No illegible handwriting"]}),
"WATER-09-B": ("Two required labels are missing, an invented banner replaces them, and the loop is not connected to the reverse osmosis unit or tank.",
  {"truth": "System outline: reverse osmosis unit and storage tank at left; the loop leaves the reverse osmosis unit, passes three dialysis machines, and returns to the reverse osmosis unit or tank. Map pins: loop start (just after reverse osmosis), loop return (last pipe before re-entry, pin drawn larger), tank outlet, and machines in rotation. A banner: sample before disinfection, not after.",
   "negatives": ["No frequency numbers", "No loop drawn as a closed ring without a source", "No text other than the verbatim labels"]}),
"WATER-11-A": ("The planner grid is empty, so the figure teaches no schedule.",
  {"truth": "Wall-planner graphic: six component rows (filters, softener, carbon, reverse osmosis, loop disinfection, lamps and ultrafilters) and four columns (daily, weekly, monthly, yearly). Each row has generic check markers in the columns where routine work typically falls: filters daily and monthly; softener daily and monthly; carbon daily and yearly; reverse osmosis daily and monthly; loop disinfection monthly; lamps and ultrafilters yearly. A technician holds a clipboard beside it.",
   "negatives": ["No dates", "No numbers in cells", "No empty grid"]}),
"BIOMED-04-A": ("The dialyzer has red caps at both ends, and dialysate enters at the top and leaves at the bottom, which is co-current with blood entering at the top.",
  {"truth": "Generic, unbranded hemodialysis machine shown in cutaway. Treated water enters; acid pump and bicarbonate pump add concentrate; mixing chamber; control conductivity cell; independent protective conductivity cell; then the dialysate line goes to the dialyzer. The dialyzer is vertical with a red cap at the top (blood in) and a blue cap at the bottom (blood out); fresh dialysate enters the LOWER side port and used dialysate leaves the UPPER side port, so dialysate flows upward against the downward blood flow.",
   "negatives": ["No ratios", "No millisiemens values", "No brand", "No dialysate entering the top side port", "No red caps on both ends"]}),
"BIOMED-04-C": ("The core label reads 'Conductivity reflects dissolved ions' instead of 'Conductivity = total salts', and the two meters show no matching value.",
  {"truth": "Two concentrate containers with clearly different labels (different recipes) each feeding a small beaker; two identical handheld conductivity meters show the SAME generic reading drawn as three identical bars or an identical icon, not digits. A caption tile states the point. Below: a technician reading a container label, and a reference meter checked against the machine sensor.",
   "negatives": ["No formulas or numbers on labels or meter screens", "No label other than the verbatim list"]}),
"BIOMED-05-C": ("The device is a benchtop box, and the cylinder is filled from a standalone tap instead of the machine's ultrafiltration or drain outlet.",
  {"truth": "Four or five steps with the same generic, unbranded hemodialysis machine in each: technician sets up following a manual; the machine's ultrafiltration or drain line empties into a glass measuring cylinder on a level surface; the technician compares the cylinder volume with the machine display; out of tolerance, she adjusts and repeats; she records as found and as left.",
   "negatives": ["No tolerance figures", "No benchtop box in place of a dialysis machine", "No water tap filling the cylinder", "No readable screen values"]}),
"BIOMED-08-B": ("The two visits per machine are not evenly spread (gaps vary from four to eight months), and one month has no visits at all.",
  {"truth": "Twelve-month grid (columns 1 to 12) for twelve generic machines (rows). Each machine has exactly two visits exactly six months apart, and the first visits are staggered one machine per month: machine 1 in months 1 and 7, machine 2 in months 2 and 8, through machine 6 in months 6 and 12, then machine 7 in months 1 and 7 again, continuing so every month has exactly two visits. Completed visits shown with a green check, upcoming ones with a purple calendar icon, and one overdue visit with a red exclamation mark.",
   "negatives": ["No calendar year", "No dates", "No machine with gaps other than six months", "No month without a visit"]}),
"BIOMED-12-B": ("The highlighted concentrate branch feeding the alarming machines starts from an open pipe end and is not connected to the shared concentrate main.",
  {"truth": "Row of six generic machines fed from above by three continuous horizontal mains: shared water (blue), shared concentrate (orange), shared power (gray conduit). Each machine has a drop from each main. A tee on the concentrate main feeds a highlighted orange sub-branch that serves machines 4, 5, and 6, which show red alarm lights. A technician looks along the lines.",
   "negatives": ["No pipe that starts or ends in mid-air", "No sensor replacement shown"]}),
}

MINOR = [
("HD-01-A", "Start the red used-item route at the treatment stations and end it at a labeled waste holding room, with its label on the red line."),
("HD-02-A", "End the nephron at the urine label and remove the bladder, or move it into a small separate inset."),
("HD-02-C", "Have the technician report to the dialysis nurse in purple scrubs, not to a physician in a white coat."),
("HD-03-A", "Show a dialyzer and bloodlines connected on both hemodialysis panels."),
("HD-03-C", "Place the peritoneal dialysis drain bag on the floor, clearly below the patient's abdomen."),
("HD-05-A", "Show a running countdown instead of a pause icon in step 4, and wipe the machine as well as the chair in step 3."),
("HD-06-A", "Make the diffusion arrows run only from the fibers into the surrounding dialysate."),
("HD-07-B", "Change the conductivity question to 'Is the reverse osmosis membrane separating salts?'"),
("HD-07-C", "End the bypass line at a floor drain with an air gap, not a faucet over a sink."),
("HD-08-A", "Add a closed clamp on each catheter limb."),
("HD-09-A", "Add the caption 'Evaluate completion and stability' to the nurse's after-treatment panel."),
("HD-09-C", "Put the bag or wheelchair on the scale in 'Anything extra?', and show the patient hands-free on the repeat weight."),
("HD-10-B", "Draw the collapse tile as slumped and unresponsive, not calmly asleep."),
("HD-10-C", "Make the last tile a sign-off or all-clear handover so it differs from step 3."),
("HD-12-A", "Add one assessor with a checklist in a different uniform at a station."),
("HD-12-B", "Close the steps into a loop and give 'Release: designated person only' its own color."),
("HD-12-C", "Re-render the header so the word 'competent' has no smudge."),
("WATER-01-B", "Rename the third column 'Living contaminants' and caption which barrier serves each column."),
("WATER-03-C", "Show the two brine tanks as separate side-by-side cutaways, not both plumbed to one softener."),
("WATER-05-C", "Caption the 'Flow falling' photo as the prefilter, or show a fouled membrane instead."),
("WATER-06-A", "Move 'Sample port: return' to the last pipe before the loop re-enters the reverse osmosis unit."),
("WATER-06-B", "Make the capped dead-leg branch clearly long and the correct branch clearly short."),
("WATER-07-C", "Attach a hose to the red connector in the technician's hand."),
("WATER-09-C", "Use the lesson wording: 'Above: hold and report', 'Between: act now', 'Below: continue'."),
("WATER-10-B", "Remove the flow arrows from the Dwell panel and add a timer icon."),
("WATER-11-C", "Re-lay out the steps to fill the canvas with larger text."),
("WATER-12-B", "Show dark carbon tanks and the sample taken after tank 2 in the chlorine breakthrough tile."),
("BIOMED-02-B", "Add a small legend: 'Colors show role, not your local wiring code.'"),
("BIOMED-02-C", "Show one-hand probing with the other probe clipped in the 'Test on a known source' panel."),
("BIOMED-03-A", "End the heat exchanger's orange pipes at a labeled 'used dialysate to drain' stub."),
("BIOMED-04-B", "Supply dialysate from inside the machine and send it to a closed drain line, not an open reservoir and beaker."),
("BIOMED-05-A", "Replace the arrows through the membrane with a membrane-displacement cue."),
("BIOMED-05-B", "Draw the ultrafiltration pump as a generic pump body, not a fan."),
("BIOMED-06-C", "Optional: use the lesson's verbatim label wording."),
("BIOMED-07-B", "Route the used dialysate line to the detector from the dialyzer's upper outlet consistently, and remove the orphan line."),
("BIOMED-11-A", "Draw Philippine-style grounded outlets (Type B), not UK sockets, and show the fuse visibly open."),
("BIOMED-11-C", "Add a small 'Outlet grounding verified' tag at the grounded outlet."),
]


def specs():
    out = {}
    for name, key in (("image_plan_hd", "HD"), ("image_plan_water", "WATER"), ("image_plan_biomed", "BIOMED")):
        T = load(name).TRACK
        for mod in T["modules"]:
            mid, figs = (mod["id"], mod["figs"]) if isinstance(mod, dict) else (mod[0], mod[2])
            for f in figs:
                out[f"{key}-{mid}-{f['letter']}"] = f
    return out


def main():
    S = specs()
    man = {e["id"]: e for e in json.loads((ROOT / "docs/tech-courses/image-prompts-manifest.json").read_text())}
    rows, body = [], []
    for i, (fid, (problem, ov)) in enumerate(FIX.items(), 1):
        f = copy.deepcopy(S[fid])
        for k, v in ov.items():
            if k == "labels":
                f["labels"] = [x.strip() for x in v.split("|")]
            else:
                f[k] = v
        e = man[fid]
        where = e["placement"]
        rows.append(f"| {i} | {fid} | {f['title']} | `{e['file']}` |")
        body.append(f"### {fid} — {f['title']}\n\n**Save as:** `{e['file']}` (replaces the published image) · **Canvas:** {B.CANVAS[f['canvas']]}\n\n"
                    f"**Why it is being redone:** {problem}\n\n**Alt:** {e['alt']}\n\n```text\n{B.fig_prompt(f, where)}\n```\n")
    minor = "\n".join(f"| {fid} | `{man[fid]['file']}` | {fix} |" for fid, fix in MINOR)
    md = f"""# GPT image prompts — corrections after the visual accuracy audit

**Site:** renalcarematters.com · **Prepared:** {PREPARED} · **Scope:** the 135 technician-track figures and heroes already published

## Audit result

All 135 images were checked against their specifications for technical and clinical accuracy, required labels, scope of practice, rendering defects, and American English.

| Result | Count |
|---|---|
| Heroes (26): accurate, no change needed | 26 |
| Figures accurate as published | {109 - len(FIX) - len(MINOR)} |
| Figures with a minor, cosmetic issue (publishable; optional edit below) | {len(MINOR)} |
| Figures to regenerate before relying on them (full prompts below) | {len(FIX)} |

Arithmetic in every worked example and every water-quality limit shown was correct. No figure shows a technician cannulating, connecting, or medicating a patient, and none carries a brand logo or readable patient data.

## How to use this file

1. **Part 1** (must fix): paste each gray block into a fresh ChatGPT image chat. Check the labels against the list, then save the PNG under the **same filename** as the published image, in `~/Documents/HD Technicians/Module images`. It replaces the old figure on the site with no code change.
2. **Part 2** (optional polish): open the published image in ChatGPT and paste the one-line edit request, or regenerate from the original prompt in `GPT-IMAGE-PROMPTS.md` with the edit added.
3. When the replacements are in the folder, ask for them to be processed and pushed.

# Part 1 — Regenerate ({len(FIX)})

| # | ID | Figure | File |
|---|---|---|---|
{chr(10).join(rows)}

{chr(10).join(body)}
# Part 2 — Optional edits ({len(MINOR)})

| ID | File | Edit request |
|---|---|---|
{minor}
"""
    out = ROOT / "docs" / "tech-courses" / "GPT-IMAGE-PROMPTS-CORRECTIONS.md"
    out.write_text(md, encoding="utf-8")
    print(f"{len(FIX)} to regenerate, {len(MINOR)} optional edits -> {out}")


if __name__ == "__main__":
    main()
