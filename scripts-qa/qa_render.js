#!/usr/bin/env node
/*
 * qa_render.js — QA screenshot harness for williamriveromd.com guides.
 *
 * Batch-renders the hero region of guide pages in three states (patient,
 * clinician/physician mode, dark mode) for fast visual QA.
 *
 * Usage:
 *   node qa_render.js <outDir> <file1.html> [file2.html ...]
 *
 * Each file argument may be absolute or relative to the repo root.
 * Outputs <basename>__patient.png, <basename>__clinician.png,
 * <basename>__dark.png into <outDir>.
 *
 * Relies on a pre-installed Chromium binary (no network download). See
 * README.md in this directory.
 */

'use strict';

const fs = require('fs');
const path = require('path');

// playwright-core may live in scripts-qa/node_modules or in the scratchpad
// install. Try a normal require first, then fall back to the known scratchpad
// path.
let chromium;
try {
  ({ chromium } = require('playwright-core'));
} catch (e) {
  const FALLBACK =
    '/tmp/claude-0/-home-user-williamriveromd-github-io/' +
    '4c4bbebc-f1cf-5ec1-82e5-b0da2c1b1aeb/scratchpad/node_modules/playwright-core';
  ({ chromium } = require(FALLBACK));
}

const CHROMIUM_PATH =
  '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

// Repo root = parent of this scripts-qa/ directory.
const REPO_ROOT = path.resolve(__dirname, '..');

function resolveInput(p) {
  return path.isAbsolute(p) ? p : path.resolve(REPO_ROOT, p);
}

async function main() {
  const argv = process.argv.slice(2);
  if (argv.length < 2) {
    console.error(
      'Usage: node qa_render.js <outDir> <file1.html> [file2.html ...]'
    );
    process.exit(2);
  }

  const outDir = path.resolve(argv[0]);
  const files = argv.slice(1);
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({
    executablePath: CHROMIUM_PATH,
    args: ['--no-sandbox', '--disable-gpu'],
  });

  const context = await browser.newContext({
    viewport: { width: 1180, height: 1400 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();

  let shotsWritten = 0;

  for (const rawFile of files) {
    const filePath = resolveInput(rawFile);
    const base = path.basename(filePath).replace(/\.html?$/i, '');

    if (!fs.existsSync(filePath)) {
      console.log(`[SKIP] ${rawFile}: file not found at ${filePath}`);
      continue;
    }

    const url = 'file://' + filePath;
    console.log(`\n=== ${base} (${filePath}) ===`);

    try {
      // Reset state between files.
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      await page.evaluate(() => {
        document.body.classList.remove('physician-mode');
        document.documentElement.removeAttribute('data-theme');
      });
      // Give web fonts a moment to settle.
      await page.waitForTimeout(800);
    } catch (e) {
      console.log(`[ERROR] ${base}: failed to load (${e.message}); skipping.`);
      continue;
    }

    // --- patient hero ---
    const patientSel = (await page.$('.mode-patient .hero'))
      ? '.mode-patient .hero'
      : (await page.$('.hero'))
      ? '.hero'
      : null;

    if (!patientSel) {
      console.log(`[SKIP] ${base}: no .hero element found; skipping file.`);
      continue;
    }

    // patient
    try {
      const el = await page.$(patientSel);
      const outPath = path.join(outDir, `${base}__patient.png`);
      await el.screenshot({ path: outPath });
      shotsWritten++;
      console.log(`  [patient]   wrote ${path.basename(outPath)} (${patientSel})`);
    } catch (e) {
      console.log(`  [patient]   failed: ${e.message}`);
    }

    // clinician — enable physician mode, prefer .mode-physician .hero
    try {
      await page.evaluate(() =>
        document.body.classList.add('physician-mode')
      );
      const cliSel = (await page.$('.mode-physician .hero'))
        ? '.mode-physician .hero'
        : patientSel;
      if (cliSel === patientSel && !(await page.$('.mode-physician .hero'))) {
        console.log(
          `  [clinician] note: no '.mode-physician .hero'; ` +
            `capturing '${patientSel}' under physician-mode.`
        );
      }
      const el = await page.$(cliSel);
      if (el) {
        const outPath = path.join(outDir, `${base}__clinician.png`);
        await el.screenshot({ path: outPath });
        shotsWritten++;
        console.log(
          `  [clinician] wrote ${path.basename(outPath)} (${cliSel})`
        );
      } else {
        console.log(`  [clinician] note: selector '${cliSel}' not visible; skipped.`);
      }
    } catch (e) {
      console.log(`  [clinician] failed: ${e.message}`);
    }

    // dark — back to patient mode + dark theme
    try {
      await page.evaluate(() => {
        document.body.classList.remove('physician-mode');
        document.documentElement.setAttribute('data-theme', 'dark');
      });
      await page.waitForTimeout(150);
      const el = await page.$(patientSel);
      if (el) {
        const outPath = path.join(outDir, `${base}__dark.png`);
        await el.screenshot({ path: outPath });
        shotsWritten++;
        console.log(`  [dark]      wrote ${path.basename(outPath)} (${patientSel})`);
      } else {
        console.log(`  [dark]      note: '${patientSel}' not visible; skipped.`);
      }
    } catch (e) {
      console.log(`  [dark]      failed: ${e.message}`);
    }

    // Clean up theme for next file (also reset at top of loop).
    await page.evaluate(() => {
      document.documentElement.removeAttribute('data-theme');
      document.body.classList.remove('physician-mode');
    });
  }

  await browser.close();

  console.log(`\nTotal screenshots written: ${shotsWritten}`);
  if (shotsWritten === 0) {
    console.error('No screenshots were produced.');
    process.exit(1);
  }
}

main().catch((e) => {
  console.error('Fatal:', e);
  process.exit(1);
});
