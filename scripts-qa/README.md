# scripts-qa — visual QA screenshot harness

`qa_render.js` batch-renders the **hero** region of guide pages for visual QA in
three states:

- `__patient.png`   — default (patient) mode hero
- `__clinician.png` — `<body class="physician-mode">` hero (skipped if the guide
  has no clinician hero)
- `__dark.png`      — patient hero with `data-theme="dark"` on `<html>`

## Usage

```bash
node scripts-qa/qa_render.js <outDir> <file1.html> [file2.html ...]
```

Each file argument may be absolute or relative to the repo root. Outputs are
named `<basename>__patient.png`, `<basename>__clinician.png`,
`<basename>__dark.png` in `<outDir>`.

Example:

```bash
node scripts-qa/qa_render.js /tmp/qa-out \
  guides/epilepsy-seizures-ckd.html guides/understanding-ckd.html
```

The harness exits non-zero if **zero** screenshots were produced.

## Requirements / notes

- Depends only on **playwright-core** (no other npm deps).
- Uses a **pre-installed Chromium** at
  `/opt/pw-browsers/chromium-1194/chrome-linux/chrome` via `executablePath`.
  There is no network for downloading browsers, so this path must exist.
- Launches with `--no-sandbox --disable-gpu`, viewport width 1180,
  `deviceScaleFactor: 2`. A single browser/page is reused across files for
  speed; body class and `data-theme` are reset between files.
- Guides lacking `.mode-physician .hero` get the clinician shot captured against
  the regular `.hero` under physician-mode (logged as a note). Guides with no
  `.hero` at all are logged and skipped without crashing the run.

This harness is QA-only; it never modifies guide HTML.
