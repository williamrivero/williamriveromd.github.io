#!/usr/bin/env python3
"""Round 2 correction prompts: figures that still failed after the first correction round (November 23, 2026).

    python3 tools/techcourses/build_correction_prompts_r2.py

Writes docs/tech-courses/GPT-IMAGE-PROMPTS-CORRECTIONS-2.md. Reuses the round 1 specs and adds a hard lock on wording,
because in round 1 the generator rephrased the labels again."""
import copy, importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


R1 = load("build_correction_prompts")
B = R1.B

AUDIT = [
("HD-05-C", "Pass", "Neutral gray bins, no color code asserted; labels verbatim."),
("HD-07-A", "Pass", "Correct train order; station fed from a drop off the loop; loop returns to the reverse osmosis outlet junction."),
("HD-09-B", "Pass", "Technician in navy; access and lines uncovered; lines leave the frame, so no impossible equipment. The machine appears as a separate screen inset."),
("WATER-02-B", "Pass", "Reverse osmosis unit feeds the loop; pump, valve, gauge, and sample port in order; drain with an air gap; loop returns to the source."),
("WATER-04-A", "Pass (note)", "Chlorine dots now dense, sparse, then none. The label 'Chlorine-free water out' is still replaced by 'Test total chlorine at the outlet', which is accurate."),
("WATER-04-C", "Fail", "Labels were rephrased again: 'action point' instead of 'limit', a reading exactly at the limit counts as a fail (the lesson passes it), and 'replace the worker, test more often' is missing."),
("WATER-08-B", "Pass", "Rows now differ by port and time; the correction reads as 62 struck through, initialed TA, corrected to 60."),
("WATER-09-B", "Fail", "Loop now connects to the reverse osmosis unit, but 'Loop return: usually highest' and 'Sample before disinfection, not after' are still missing, and an invented banner appears again."),
("WATER-11-A", "Pass", "Planner now carries markers in the expected columns."),
("BIOMED-04-A", "Pass", "Red cap at the top and blue at the bottom; dialysate enters the lower port and leaves the upper port (countercurrent)."),
("BIOMED-04-C", "Fail", "The key label still reads 'Conductivity reflects dissolved ions' instead of 'Conductivity = total salts'."),
("BIOMED-05-C", "Pass", "Generic dialysis machine; the cylinder fills from the machine's outlet line."),
("BIOMED-08-B", "Pass", "Every machine has two visits six months apart; each month has two visits; one overdue mark."),
("BIOMED-12-B", "Pass", "Highlighted branch now tees off the shared concentrate main."),
]

LOCK = ("WORDING LOCK: every text element in the image must be copied character for character from the label list below. "
        "Do not paraphrase, shorten, translate, or 'improve' any label. Do not add any title, banner, caption, or sentence "
        "that is not in the list. If a label does not fit, make the box larger, not the wording different.")

EXTRA = {
"WATER-04-C": "The four outcome boxes carry exactly these words and no others: 'At or below the limit: record and release' (green); "
              "'Above the limit: test after tank 2 now' (amber); 'Tank 2 within limit: report, replace the worker, test more often' (amber); "
              "'Tank 2 above limit: STOP and report' (red). Never use the words 'action point', 'protocol', or 'procedure'.",
"WATER-09-B": "The loop return pin carries the full label 'Loop return: usually highest'. Across the top, a single banner carries exactly "
              "'Sample before disinfection, not after'. There is no other banner and no mention of sampling plans.",
"BIOMED-04-C": "The large caption tile carries exactly 'Conductivity = total salts', with the equals sign. Never write 'reflects', 'dissolved', or 'ions'.",
}


def main():
    S = R1.specs()
    man = {e["id"]: e for e in json.loads((ROOT / "docs/tech-courses/image-prompts-manifest.json").read_text())}
    fails = [a for a in AUDIT if a[1] == "Fail"]
    rows, body = [], []
    for i, (fid, _, why) in enumerate(fails, 1):
        f = copy.deepcopy(S[fid])
        for k, v in R1.FIX[fid][1].items():
            f[k] = [x.strip() for x in v.split("|")] if k == "labels" else v
        f["truth"] = LOCK + "\n" + EXTRA[fid] + "\n" + f["truth"]
        f["negatives"] = list(f["negatives"]) + ["No reworded label", "No invented banner or caption"]
        e = man[fid]
        rows.append(f"| {i} | {fid} | {f['title']} | `{Path(e['file']).name}` |")
        body.append(f"### {fid} — {f['title']}\n\n**Save as:** `{Path(e['file']).name}` · **Canvas:** {B.CANVAS[f['canvas']]}\n\n"
                    f"**Why it failed again:** {why}\n\n**Tip:** after generating, compare every word with the label list. If one label is reworded, "
                    f"reply in the same chat: *Change the text \"…\" to exactly \"…\" and change nothing else.*\n\n"
                    f"```text\n{B.fig_prompt(f, e['placement'])}\n```\n")
    audit = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in AUDIT)
    md = f"""# GPT image prompts — corrections, round 2

**Site:** renalcarematters.com · **Prepared:** {R1.PREPARED} · **Source:** `~/Documents/HD Technicians/Corrected images` (14 regenerated figures)

## Audit of the corrected images

| ID | Result | Finding |
|---|---|---|
{audit}

**{len(AUDIT) - len(fails)} passed and are published. {len(fails)} failed again**, each because the generator reworded a required label. The failed images were still published, because each is better than the version it replaced, but they should be regenerated. The prompts below add a wording lock and spell out each box's text.

## Regenerate ({len(fails)})

| # | ID | Figure | Save as |
|---|---|---|---|
{chr(10).join(rows)}

Save each new PNG (with its WebP) into `~/Documents/HD Technicians/Corrected images` under the same filename, then ask for the folder to be processed and pushed.

{chr(10).join(body)}"""
    out = ROOT / "docs" / "tech-courses" / "GPT-IMAGE-PROMPTS-CORRECTIONS-2.md"
    out.write_text(md, encoding="utf-8")
    print(f"{len(fails)} prompts -> {out}")


if __name__ == "__main__":
    main()
