#!/usr/bin/env python3
"""Build the prompt pack for NEW figures (image_plan_hd_new.py) and a status list of every planned image
that has not been produced yet.

    python3 tools/techcourses/build_new_image_prompts.py

Writes docs/tech-courses/GPT-IMAGE-PROMPTS-NEW.md and docs/tech-courses/image-prompts-new-manifest.json
Run build_image_brief.py first so image-prompts-manifest.json is current."""
import importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


B = load("build_image_brief")
NEW = load("image_plan_hd_new").NEW
DOCS = ROOT / "docs" / "tech-courses"
PRE = "hemodialysis-technician"


def main():
    hd = B.hd_slugs()
    manifest, rows, prompts = [], [], []
    for mid, title, figs in NEW:
        page = hd[mid]
        prompts.append(f"\n## Module {int(mid)} — {title}\n")
        for f in figs:
            fid = f"HD-{mid}-{f['letter']}"
            file = f"images/{PRE}-{mid}-{f['slug']}.png"
            where = f"academy/{page}.html, section `{f['section']}`"
            star = "★" if f["core"] else "○"
            manifest.append({"id": fid, "track": "hd", "module": mid, "kind": f["kind"], "core": f["core"], "title": f["title"],
                             "file": file, "canvas": B.CANVAS[f["canvas"]], "placement": where, "job": f["job"], "alt": f["alt"],
                             "review": "Dr. Rivero; head nurse"})
            rows.append((fid, star, f["title"], file, f["kind"]))
            head = (f"### {fid} {star} — {f['title']}\n\n**File:** `{file}` · **Canvas:** {B.CANVAS[f['canvas']]} · "
                    f"**Placement:** {where}\n\n**Job:** {f['job']}\n\n**Alt:** {f['alt']}\n")
            if f["kind"] == "circuit":
                labels = "; ".join(f["labels"])
                prompts.append(head + "\n> **Circuit figure.** Do not write a new layout. Generate this prompt with the "
                               "`dialysis-circuit-schematic` skill (modality: intermittent hemodialysis), which locks the port colors, "
                               f"flow directions, and pressure points. Content to add: {f['truth']} Labels: {labels}. "
                               f"Footer: `{B.FOOTER}`.\n")
            else:
                prompts.append(head + f"\n```text\n{B.fig_prompt(f, where)}\n```\n")
    # status of the first set
    main_manifest = json.loads((DOCS / "image-prompts-manifest.json").read_text(encoding="utf-8"))
    missing, flat = [], []
    for e in main_manifest:
        p = ROOT / e["file"]
        if e.get("replaces"):
            flat.append(e)
        elif not p.exists():
            missing.append(e)
    n = len(manifest); core = sum(1 for m in manifest if m["core"])
    table = "\n".join(f"| {i} | {a} {b} | {c} | `{d}` | {e} |" for i, (a, b, c, d, e) in enumerate(rows, 1))

    def status_table(items):
        return "\n".join(f"| {e['id']} {'★' if e['core'] else '○'} | {e['title']} | `{e['file']}` | {e['kind']} |" for e in items)

    by_track = {}
    for e in missing:
        by_track.setdefault(e["track"], []).append(e)
    names = {"hd": "Hemodialysis Technician", "water": "Water Treatment Technician", "wt": "Water Treatment Technician",
             "biomed": "Dialysis Biomedical Technician", "bm": "Dialysis Biomedical Technician"}
    miss_md = []
    for t, items in by_track.items():
        miss_md.append(f"\n### {names.get(t, t)} — {len(items)} not yet produced "
                       f"({sum(1 for e in items if e['core'])} core)\n\n| ID | Figure | File | Type |\n|---|---|---|---|\n{status_table(items)}\n")
    head = f"""# GPT image prompts — new and missing figures

**Site:** renalcarematters.com · **Prepared:** {B.PREPARED} · **Tracks:** Renal Care Academy technician tracks

This file has two parts.

- **Part 1** holds complete prompts for **{n} new figures** ({core} core ★, {n - core} optional ○) that illustrate the lessons added to the Hemodialysis Technician track. These are not in the first prompt pack.
- **Part 2** lists every figure from the first prompt pack (`GPT-IMAGE-PROMPTS.md`) that has **not been produced yet**: {len(missing)} files that do not exist, plus {len(flat)} flat teaching diagrams that are waiting to be replaced. Their prompts are already written; find each one in `GPT-IMAGE-PROMPTS.md` by its ID.

## How to produce

1. One figure per chat. Paste one gray block into a fresh ChatGPT image chat and ask for the canvas size on the entry.
2. Check the text first: compare every label with the verbatim list. If one word is wrong, ask for that word to be fixed, not for a new image.
3. Reject an image with an invented number, a brand, a dark background, flat clip-art rendering, or a missing or altered footer (`{B.FOOTER}`).
4. The one circuit figure is generated with the `dialysis-circuit-schematic` skill, not from a prompt in this file.
5. Save as PNG under the exact filename into `images/`. New figures are not yet referenced by a lesson: after saving, add a key for the file in `tools/techcourses/figs.py` and place it in the lesson with `{{{{fig:key}}}}`, then run `python3 generate_tech_courses.py --patch`.
6. Every figure needs Dr. Rivero's review before publication.

# Part 1 — New figures

## Production list

| # | ID | Figure | File | Type |
|---|---|---|---|---|
{table}
"""
    part2 = f"""
# Part 2 — Planned figures not yet produced

Prompts for these are in `GPT-IMAGE-PROMPTS.md` under the same ID. ★ core, ○ optional.
{''.join(miss_md)}
### Flat teaching diagrams waiting to be replaced — {len(flat)}

These files exist as flat diagrams. Saving the new illustrated figure under the same filename swaps it in with no code change.

| ID | Figure | File | Type |
|---|---|---|---|
{status_table(flat)}
"""
    (DOCS / "GPT-IMAGE-PROMPTS-NEW.md").write_text(head + "\n".join(prompts) + part2, encoding="utf-8")
    (DOCS / "image-prompts-new-manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{n} new figures ({core} core); {len(missing)} planned figures not yet produced; {len(flat)} flat diagrams to replace.")


if __name__ == "__main__":
    main()
