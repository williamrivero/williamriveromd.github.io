# Voice and teaching standard for the nursing modules (rewrite pass)

The owner likes the voice of the Physician on Duty (POD) modules. Read the two samples beside this file
(POD-VOICE-SAMPLE-m13.py, POD-VOICE-SAMPLE-m11.py) before you write. Then rewrite the nursing prose in that voice,
for a registered nurse instead of a physician, while meeting the owner's medical teaching standard
(read /root/.claude/skills/synced/e7f3cdd9-a361-44a3-a710-a92e74c17604_d5a9b0e0-f0c3-4377-8b81-f15e9ba9cc14/medical-teaching-standard/SKILL.md
and its references/appraisal.md and references/grading-systems.md — these are in your own workspace, use the Read tool).

## The voice, in practice
- Talk to the reader: "you", "your shift", "your unit's protocol". The nurse is the actor; say what you notice, do, report.
- Short, declarative sentences. One idea per sentence. Plain words first, the technical term after, glossed once.
- Open the model section with a plain picture (an everyday analogy), then immediately say where the picture stops being true ("The picture has a limit. …") and give the real physiology.
- State the job of the module in one or two sentences near the top ("Most episodes are … A few are … Your work is to …").
- Mechanism as a causal chain, not a list of findings: what normally happens, what breaks, what you see at the bedside.
- Tables that turn mechanism into observation: e.g. "Defense | What weakens it | What you may notice".
- One bolded take-home line per major section, written as a rule the nurse can carry ("At every episode, ask which … failed").
- Cases: a named Filipino patient and nurse, concrete time ("Hour three"), concrete bedside values that the module text supports (illustrative values are fine in a fictional case; never present them as targets), and what has already been done.
- Evidence sentences say how strong the evidence is and what it does not show: "The analysis was observational and does not show that preventing X prolongs life." Name the study design and size when you name a study.
- Guideline statements keep the source's own grading vocabulary (KDIGO 1A–2D, "practice point", "ungraded", "conference statement, not a graded recommendation"). Never invent or translate a grade; if you do not have the grade verified, do not state one.
- Where a relative effect is given, add the absolute numbers (event rates, absolute difference, number needed to treat) when the source gives them; otherwise say only what the source gives.
- Label surrogate outcomes as surrogates (a lab value, walk distance, Kt/V) and distinguish them from outcomes patients feel.
- Warm and steady, never alarmist; respect for patients and families.

## Hard rules (unchanged from AGENT_RULES.md — read it too)
- Do NOT change: section ids, "after" keys, section order, the number of sections, figure placement anchors, file names, MODULE keys, competency thread/level keys, the image dict, reference keys. You may improve section "nav"/"title" wording only if the id stays the same.
- Keep every fact you keep correct. Do not add new facts, numbers, trials or grades unless you verify them (PubMed for studies, the guideline text for grades) and cite them with existing keys or verified NEW_REFS. When in doubt, cut rather than add.
- Quizzes: keep bank size (base 5, each _x file its count, _q files their count). You may reword stems, options and rationales into the same voice; each item still has exactly one correct answer, and its "objective" string must match an objective EXACTLY — if you reword an objective, update every quiz item that uses it (in all of that module's files).
- Keep all citations attached to the statements they support; do not orphan or move them onto different claims.
- Abbreviations: same rules as before (expand at first use in the module; only those already used by the module).
- American English. No PSN syllabus wording. Nurses never prescribe or change doses.
- Length: roughly the same as now (±15%). This is a voice and rigor pass, not an expansion.

## Verify before reporting
- ast.parse every file you touched.
- `cd /Users/williamgregoryriveromd/Documents/williamriveromd.github.io && /opt/homebrew/bin/python3.13 generate_nursing_course.py --check` must report no errors for your modules (other agents are editing other modules at the same time; ignore errors that name only their modules, and re-run once if a file of theirs is mid-write).
- Report: per module, what changed (voice, evidence sentences fixed, grades corrected or removed, absolute numbers added, surrogates labeled), any fact you removed because you could not verify it, and any NEW_REFS.
