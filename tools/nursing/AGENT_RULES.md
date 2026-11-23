# Rules for agents writing nursing-course content (Renal Care Academy)

Owner: Dr. Rivero, Philippine nephrologist and dialysis-center medical director. Audience: Philippine registered nurses. Teaching style: physiology first — plain mental model, then mechanism, then evidence, then bedside action.

## Tools and files
- Repo: /Users/williamgregoryriveromd/Documents/williamriveromd.github.io (user's Mac). Load Desktop Commander via ToolSearch:
  `select:mcp__remote-devices__plugin_desktop-commander_desktop-commander__read_file,mcp__remote-devices__plugin_desktop-commander_desktop-commander__write_file,mcp__remote-devices__plugin_desktop-commander_desktop-commander__start_process`
- Content files live in tools/nursing/content/. Exemplars: m13.py (base MODULE dict, every field), m13_x.py / m13_x2.py (expansion files: OBJECTIVES, EXTRA, QUIZ, TERMS, FLAGS, NEW_REFS), m09_q.py (extra QUIZ items), m13_c.py (COMPETENCIES + MILESTONE). Read them fully before writing.
- common.py holds ABBR, MANUAL_REFS, PUBMED_REFS (reference keys), COMPETENCY_LEVELS / COMPETENCY_THREADS / COMPETENCY_EVIDENCE.
- Write ONLY the files named in your brief. No git, no `--patch`, do not run fetch_refs.py, do not edit common.py / display.py / the generator. List anything you need from those in your report.

## Content rules
- American English. Never copy any external syllabus or program (PSN, ANNA, NNCC, EDTNA) — no quoted titles, numbering or schedules. Our own words throughout.
- HTML exactly as in the exemplars: `<p>`, `<ul>/<ol>`, `<strong>`, `<em>`, tables wrapped in `<div class="table-wrap">`. No headings, links, images or inline styles.
- Citations as `[[key]]`, only keys that exist in common.py or that you add to NEW_REFS after verifying the PMID on PubMed (author, year, journal, title, finding). Never invent a reference, trial name, number or grade. Attach citations to the statements they support.
- Data gaps: when no Philippine figure exists, adopt United States data (then other international data) as the working estimate, and label its source in the sentence ("in United States studies, ...").
- Calibrated verbs: "reduces/prevents" only for randomized evidence on that outcome; "is associated with" for observational data; "may" for mechanism.
- No drug doses, alarm limits or device settings; write "per order", "per protocol", "per the unit's target". Nurses never prescribe, start, stop or change doses — they assess, check, hold and notify per order or protocol, teach, document, report and refer.
- Abbreviations: only those listed in your brief, each expanded at first use in the module; spell out everything else.
- Quiz items: format of m13_x2.py; each item's "objective" string must match one of that file's OBJECTIVES (or the base objectives for m NN.py / mNN_q.py) exactly; exactly one correct answer; a rationale for every option.
- Competencies: thread keys from COMPETENCY_THREADS; level K/S/D/I per COMPETENCY_LEVELS (S = simulation, role-play or teach-back; D = observed in supervised practice; I only for truly independent, sign-off items).
- Readings: only site guides that exist in guides/ (check with ls). Calculators: leave "calcs": [] and list wanted calculators (file, plain title, one line) in your report.

## Verify before reporting
- `python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" <file>` for each file.
- `cd <repo> && NC_DRAFT=1 /opt/homebrew/bin/python3.13 generate_nursing_course.py --check` — errors only about your NEW_REFS PMIDs missing from refs_pubmed_raw.json (or JOURNALS / TITLE_OVERRIDES) are expected; fix every other error naming your module.

## Report back (short)
Sections with word counts; NEW_REFS with what you verified; every number you stated and its source; readings and calculators to add; FLAGS; uncertainties.
