#!/usr/bin/env node
/* Browser checks for the Nephrology Nursing & Hemodialysis course.
 *
 *   node tests/nursing-course.cjs [screenshotDir]
 *
 * Needs playwright-core (any install; set PLAYWRIGHT_CORE to its path if it is not
 * resolvable) and Google Chrome. Opens the built pages from disk, so run
 * `python3 generate_nursing_course.py --patch` first. No network is required and
 * the test asserts that the quiz makes no network requests.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
let chromium;
try { ({ chromium } = require('playwright-core')); }
catch (e) { ({ chromium } = require(process.env.PLAYWRIGHT_CORE)); }

const shots = process.argv[2];
const guides = path.join(ROOT, 'academy');
const pages = fs.readdirSync(guides).filter(f => /^nephrology-nursing.*\.html$/.test(f) && !f.includes(' ')).sort();
const modules = pages.filter(f => /^nephrology-nursing-\d\d-/.test(f));
const url = f => 'file://' + path.join(guides, f);
let failures = 0, checks = 0;
function ok(cond, msg) { checks++; if (!cond) { failures++; console.log('  FAIL: ' + msg); } }

(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });

  // 1. Every page: loads, no script errors, no dead local links or assets, no sideways scroll on a phone
  for (const f of pages) {
    const ctx = await browser.newContext({ viewport: { width: 375, height: 740 } });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    await page.goto(url(f), { waitUntil: 'load' });
    await page.waitForTimeout(300);
    ok(errors.length === 0, `${f}: script errors: ${errors.join(' | ')}`);
    const hrefs = await page.$$eval('a[href]', as => as.map(a => a.getAttribute('href')));
    for (const h of hrefs) {
      if (/^(#|[a-z][a-z0-9+.-]*:)/i.test(h)) continue;
      const clean = h.split('#')[0].split('?')[0];
      if (!clean) continue;
      const target = clean.startsWith('/') ? path.join(ROOT, clean) : path.resolve(guides, clean);
      const exists = fs.existsSync(target) || fs.existsSync(target + '.html') || fs.existsSync(path.join(target, 'index.html'));
      ok(exists, `${f}: dead link ${h}`);
    }
    const anchors = await page.$$eval('a[href^="#"]', as => as.map(a => a.getAttribute('href')).filter(h => h.length > 1 && !/^#ref-\d+$/.test(h)));
    for (const a of anchors) ok(await page.$(`[id="${a.slice(1)}"]`) !== null, `${f}: missing anchor ${a}`);
    const srcs = await page.$$eval('script[src],img[src],source[srcset]', els => els.map(e => e.getAttribute('src') || (e.getAttribute('srcset') || '').split(' ')[0]).filter(Boolean));
    for (const s of srcs) {
      if (/^https?:/.test(s)) continue;
      const target = s.startsWith('/') ? path.join(ROOT, s) : path.resolve(guides, s);
      ok(fs.existsSync(target), `${f}: missing asset ${s}`);
    }
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    ok(overflow <= 1, `${f}: page scrolls sideways by ${overflow}px at 375px`);
    const h1 = await page.$$eval('h1', h => h.length);
    ok(h1 === 1, `${f}: expected one h1, found ${h1}`);
    await ctx.close();
  }

  // 2. Quiz flow on every module
  for (const f of modules) {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
    const page = await ctx.newPage();
    const requests = [];
    await page.goto(url(f), { waitUntil: 'load' });
    await page.waitForTimeout(200);
    // only data-carrying requests count: late web-font fetches by the page shell are not the quiz
    page.on('request', r => { if (['xhr', 'fetch', 'ping', 'websocket', 'eventsource'].includes(r.resourceType()) || r.method() !== 'GET') requests.push(r.method() + ' ' + r.url()); });
    const bankN = await page.$$eval('fieldset.nc-q', q => q.length);
    const drawN = parseInt(await page.getAttribute('#nc-quiz', 'data-draw'), 10);
    ok(bankN >= 15, `${f}: question bank should hold at least 15 items, found ${bankN}`);
    const nq = await page.$$eval('fieldset.nc-q:not([hidden])', q => q.length);
    ok(nq === drawN && nq === 5, `${f}: expected 5 questions shown from the bank, found ${nq}`);
    const nums = await page.$$eval('fieldset.nc-q:not([hidden]) .nc-qn', q => q.map(x => x.textContent.trim()));
    ok(nums.every((t, i) => t === `Question ${i + 1} of ${nq}`), `${f}: shown questions not renumbered: ${nums.join(' | ')}`);
    // random draw: a reload should give a different set or order within a few tries
    const sig = () => page.$$eval('fieldset.nc-q:not([hidden])', q => q.map(x => x.getAttribute('data-q') + ':' + Array.from(x.querySelectorAll('input')).map(i => i.value).join('')).join(','));
    const first = await sig();
    let changed = false;
    for (let t = 0; t < 4 && !changed; t++) { await page.reload({ waitUntil: 'load' }); await page.waitForTimeout(100); changed = (await sig()) !== first; }
    ok(changed, `${f}: reloading did not change the drawn set`);
    const setOf = () => page.$$eval('fieldset.nc-q:not([hidden])', q => q.map(x => x.getAttribute('data-q')).sort().join(','));
    const before = await setOf();
    await page.click('[data-nc-newset]');
    ok((await setOf()) !== before, `${f}: New set did not draw a different set`);
    ok(await page.$$eval('fieldset.nc-q[hidden] input', i => i.every(x => x.disabled)), `${f}: hidden bank items are not disabled`);
    const labelled = await page.$$eval('.nc-quiz input[type=radio]', ins => ins.every(i => document.querySelector(`label[for="${i.id}"]`)));
    ok(labelled, `${f}: a radio input has no label`);
    const keyed = await page.$$eval('fieldset.nc-q', qs => qs.every(q => q.querySelectorAll('input[data-correct="1"]').length === 1 && q.querySelectorAll('input').length === 4));
    ok(keyed, `${f}: each question must have 4 options and exactly one key`);
    ok(await page.$$eval('.nc-rat', r => r.every(x => x.hidden)), `${f}: rationales visible before checking`);

    // submit with nothing answered
    await page.click('#nc-quiz button[type=submit]');
    ok(/answer every question/i.test(await page.textContent('#nc-result')), `${f}: no prompt when unanswered`);
    ok(await page.evaluate(() => { const a = document.activeElement; return a && a.closest('fieldset') === document.querySelector('fieldset.nc-q:not([hidden])'); }), `${f}: focus not moved to first unanswered question`);

    // keyboard: answer question 1 with the keyboard (focused radio + Space), then arrow keys
    const firstQ = await page.$eval('fieldset.nc-q:not([hidden])', q => Array.from(q.querySelectorAll('input')).map(i => i.id));
    await page.focus('#' + firstQ[0]);
    await page.keyboard.press('Space');
    ok(await page.isChecked('#' + firstQ[0]), `${f}: Space did not select a focused option`);
    await page.keyboard.press('ArrowDown');
    ok(await page.isChecked('#' + firstQ[1]), `${f}: arrow key did not move the selection`);

    // deliberately wrong on Q1, right on Q2 and Q3
    await page.evaluate(() => {
      document.querySelectorAll('fieldset.nc-q:not([hidden])').forEach((q, i) => {
        const pick = i === 0 ? q.querySelector('input[data-correct="0"]') : q.querySelector('input[data-correct="1"]');
        pick.checked = true;
      });
    });
    await page.click('#nc-quiz button[type=submit]');
    const res = await page.textContent('#nc-result');
    ok(res.includes(`Self-assessment complete: ${nq - 1} of ${nq}`), `${f}: wrong score text: ${res.slice(0, 80)}`);
    ok(await page.$$eval('fieldset.nc-q:not([hidden]) .nc-rat', r => r.every(x => !x.hidden) && r.length) === nq * 4, `${f}: not every option shows a rationale`);
    ok(await page.evaluate(() => document.activeElement.id === 'nc-result'), `${f}: focus not moved to the result`);
    ok(await page.getAttribute('#nc-result', 'aria-live') === 'polite', `${f}: result is not a live region`);
    ok(await page.$$eval('.nc-quiz input[type=radio]', i => i.every(x => x.disabled)), `${f}: inputs still editable after checking`);
    ok(await page.$$eval('.nc-verdict', v => v.filter(x => x.textContent.trim()).length >= 3), `${f}: verdict text missing (color alone)`);
    ok(await page.evaluate(() => localStorage.getItem('rcm-nursing-progress') === null), `${f}: progress stored without opt-in`);

    // retry
    await page.click('[data-nc-retry]');
    ok(await page.$$eval('fieldset.nc-q:not([hidden]) input[type=radio]', (i, n) => i.length === n * 4 && i.every(x => !x.checked && !x.disabled), nq), `${f}: retry did not reset`);
    ok(await page.$$eval('.nc-rat', r => r.every(x => x.hidden)), `${f}: rationales still visible after retry`);

    // opt in, all correct, stored locally
    await page.check('#nc-remember');
    await page.evaluate(() => document.querySelectorAll('fieldset.nc-q:not([hidden]) input[data-correct="1"]').forEach(i => { i.checked = true; }));
    await page.click('#nc-quiz button[type=submit]');
    ok((await page.textContent('#nc-result')).includes(`${nq} of ${nq}`), `${f}: all-correct score wrong`);
    const stored = await page.evaluate(() => JSON.parse(localStorage.getItem('rcm-nursing-progress') || 'null'));
    const id = f.match(/nursing-(\d\d)-/)[1];
    ok(stored && stored.modules && stored.modules[id] && stored.modules[id].score === nq, `${f}: opted-in progress not stored`);
    await page.click('[data-nc-retry]');
    await page.uncheck('#nc-remember');
    ok(await page.evaluate(() => localStorage.getItem('rcm-nursing-progress') === null), `${f}: unticking did not erase progress`);
    ok(requests.length === 0, `${f}: quiz made network requests: ${requests.slice(0, 3).join(', ')}`);

    // competencies: section present, at least 8 rows, every row has a level chip
    const comp = await page.$$eval('#competencies table.nc-comp tbody tr', r => r.map(x => !!x.querySelector('.nc-lv')));
    ok(comp.length >= 8 && comp.every(Boolean), `${f}: competency table missing or incomplete (${comp.length} rows)`);
    // previous / next
    const np = await page.$$eval('.nc-nextprev a', a => a.map(x => x.getAttribute('href')));
    ok(np.length === 2 && np.every(h => fs_exists(h)), `${f}: previous/next links broken`);
    await ctx.close();
  }
  function fs_exists(h) { return fs.existsSync(path.resolve(guides, h)); }

  // 3. Hub: path selector and progress display
  {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
    const page = await ctx.newPage();
    await page.goto(url('nephrology-nursing.html'), { waitUntil: 'load' });
    const order = () => page.$$eval('#nc-modules [data-module]', c => c.map(x => x.getAttribute('data-module')).join(','));
    ok(await order() === '01,02,15,03,04,05,06,07,08,09,10,11,14,16,17,12,13', 'hub: default order wrong');
    await page.focus('[data-nc-path="hd"]');
    await page.keyboard.press('Enter');
    ok(await order() === '01,06,07,08,09,14,02,03,04,05,16,10,11,15,17,12,13', 'hub: hemodialysis path order wrong: ' + await order());
    ok(await page.getAttribute('[data-nc-path="hd"]', 'aria-pressed') === 'true', 'hub: aria-pressed not updated');
    ok(await page.$$eval('#nc-modules a', a => a.length) === 17, 'hub: expected 17 module cards');
    ok(await page.isHidden('#nc-progress'), 'hub: progress bar shown without opt-in');
    ok(await page.$$eval('#progression table.nc-pm tbody tr', r => r.length) === 12, 'hub: competency map should have 12 threads');
    ok(await page.$$eval('#progression table.nc-pm thead th.nc-pm-mod', r => r.length) === 17, 'hub: competency map should have 17 module columns');
    await page.evaluate(() => localStorage.setItem('rcm-nursing-progress', JSON.stringify({ optin: true, modules: { '06': { score: 3, total: 3, date: '2026-11-23' } } })));
    await page.reload({ waitUntil: 'load' });
    ok(/1 of 17/.test(await page.textContent('#nc-progress')), 'hub: saved progress not shown');
    await page.click('#nc-progress button');
    ok(await page.evaluate(() => localStorage.getItem('rcm-nursing-progress') === null), 'hub: clear progress failed');
    await ctx.close();
  }

  // 4. Screenshots for visual review
  if (shots) {
    fs.mkdirSync(shots, { recursive: true });
    const plan = [
      ['nephrology-nursing.html', 1280, false, 'hub-desktop'],
      ['nephrology-nursing.html', 375, false, 'hub-phone'],
      [modules[5], 1280, false, 'm06-desktop'],
      [modules[5], 1280, true, 'm06-dark'],
      [modules[8], 375, false, 'm09-phone'],
      ['nephrology-nursing-educator.html', 1280, false, 'educator-desktop'],
    ];
    for (const [f, w, dark, name] of plan) {
      const ctx = await browser.newContext({ viewport: { width: w, height: 900 } });
      const page = await ctx.newPage();
      if (dark) await page.addInitScript(() => localStorage.setItem('wgmr-dark', '1'));
      await page.goto(url(f), { waitUntil: 'load' });
      await page.waitForTimeout(700);
      if (/^m0/.test(name)) {
        await page.evaluate(() => {
          document.querySelectorAll('fieldset.nc-q:not([hidden])').forEach((q, i) => {
            (i === 0 ? q.querySelector('input[data-correct="0"]') : q.querySelector('input[data-correct="1"]')).checked = true;
          });
          document.querySelector('#nc-quiz button[type=submit]').click();
        });
      }
      await page.screenshot({ path: path.join(shots, name + '.jpg'), fullPage: true, type: 'jpeg', quality: 60 });
      await ctx.close();
    }
  }

  await browser.close();
  console.log(`${checks} checks, ${failures} failed`);
  process.exit(failures ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
