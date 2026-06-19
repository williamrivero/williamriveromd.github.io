# DESIGN SYSTEM HANDOFF — williamriveromd.github.io
**Version:** 2026-05-16 · Verified against source files
**Scope:** All work on `guides/medication-operational-guide.html` (Part 1 rewrite) and `guides/medication-operational-guide-2.html` (Part 2, new file)

---

## THE SITE IN 30 SECONDS

- **What it is:** Static patient-education site for Dr. William Gregory M. Rivero MD (Nephrology, Philippines)
- **~93 standalone HTML guides** — each is a complete self-contained document with inline CSS + JS
- **No build step.** Commit HTML files and push. GitHub Pages auto-deploys.
- **Live:** `https://williamriveromd.com`
- **Git rule: commit directly to `main`. No PRs, no branches unless user says "review mode."**
- **Dev preview:** `npm start` → serves at `localhost:3000`

---

## THE CSS ARCHITECTURE — READ THIS FIRST

Every guide has **exactly two `<style>` blocks** in `<head>`:

```
<style> ← BLOCK 1: MASTER CSS (~920 lines, version 2026-05-15)
  Managed ONLY via patch_master_css.py (MASTER_CSS string at line 43).
  NEVER edit directly in the guide file. It will be overwritten.
</style>

<style> ← BLOCK 2: PER-GUIDE CSS
  All guide-specific components go here.
  Safe to edit directly.
</style>
```

**After writing or editing any guide:**
```bash
python3 patch_master_css.py --guide medication-operational-guide.html
python3 patch_master_css.py --guide medication-operational-guide-2.html
```

`index.html` is excluded from patching. It has different tokens — do not conflate.

---

## COLOR TOKENS (light mode — guides only)

These are the **verified, exact values** from the master CSS file. Use CSS variables everywhere — never hardcode hex in new rules.

```css
:root {
  --navy:       #1f3864;   /* primary dark — headers, dark panels, .qref bg */
  --gold:       #b8962e;   /* accent — used sparingly */
  --gold-light: #d4af4f;   /* accent text ON dark backgrounds (.qref h4, .dstat-val) */
  --teal:       #1a6b72;   /* interactive — links, active states, badges */
  --teal-light: #e1f5f0;   /* teal wash background */

  --text:       #1e2a38;   /* 10.2:1 on white — primary body */
  --text-mid:   #2c3a4a;   /*  8.1:1 — secondary body, table cells */
  --text-muted: #4a5568;   /*  6.1:1 — labels, captions */
  --text-faint: #5c6a7e;   /*  4.7:1 — fine print, large text only */

  --bg:         #f9fafb;   /* page background, card backgrounds */
  --white:      #ffffff;   /* content area */
  --border:     #e2e6eb;   /* dividers, card borders */

  --red:        #b91c1c;   /* 5.9:1 — danger text */
  --red-soft:   #fff0f0;   /* danger wash */
  --amber:      #92400e;   /* 7.3:1 — warning text */
  --amber-soft: #fffbeb;   /* warning wash */
  --green:      #166534;   /* 8.2:1 — success text */
  --green-soft: #f0fdf4;   /* success wash */
  --purple:     #6b21a8;   /* 7.1:1 — nursing callout text */
  --purple-soft:#faf5ff;   /* nursing wash */
}
```

**WCAG rule (strictly enforced):** Every foreground/background pair must be ≥4.5:1 (normal text) or ≥3:1 (large text ≥18px or 14px bold). Verify before adding any new pair.

**Dark mode** is applied via `html[data-theme="dark"]`. Every new component needs a dark override.

Dark overrides (verified):
```css
html[data-theme="dark"] {
  /* tokens that change */
  --teal:       #2ba8b0;
  --bg:         #141c2a;
  --white:      #1a2030;
  --border:     #2a3548;
  --text:       #e8eaf0;
  --text-mid:   #dde3eb;
  --text-muted: #9baab8;
  --red:        #f87171;   --red-soft:   #2a1515;
  --amber:      #fbbf24;   --amber-soft: #2a1900;
  --green:      #4ade80;   --green-soft: #0e2a1c;
  --purple:     #c084fc;   --purple-soft:#1a1030;
}
/* body bg: #0f1520; dark panels (hero/nav): #080d16; cards: #1a2535 */
```

**Homepage tokens are different — do not use in guides:**
`--text: #111827`, `--cream: #f4f6f9`, `--teal: #145c63`

---

## TYPOGRAPHY

```html
<!-- In every guide <head> — always present -->
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
```

| Element | Font | Size | Weight | Notes |
|---|---|---|---|---|
| Body | DM Sans | 16px | 400 | line-height 1.7 |
| h1 | Lora, serif | `clamp(28px,5vw,50px)` | 600 | |
| h2 | Lora, serif | `clamp(22px,3.5vw,32px)` | 600 | |
| h3 | Lora, serif | `clamp(18px,2.5vw,24px)` | 600 | |
| Section tag | DM Sans | 11px | 600 | uppercase, letter-spacing .14em, color --teal |
| Code/mono | DM Mono, Courier New | 12.5–13px | 400 | `.fd code`, `.formula`, `.qref code` |
| `.algo-title` | Lora | `clamp(19px,2.5vw,24px)` | 600 | color --navy |
| `.drug-name` | Lora | `clamp(20px,3vw,26px)` | 600 | white on --navy |

---

## STICKY LAYER Z-INDEX STACK

```
z-index: 200   .site-header      (height ~56px, top: 0)
z-index: 140   .algo-nav / drug nav bar  (top: 56px)
z-index: 9998  .print-btn        (FAB, fixed)
z-index: 9997  .dl-fab           (FAB, fixed)
z-index: 9996  .scroll-top-btn   (FAB, fixed)

scroll-margin-top on sections: 112px  (56px header + 56px drug nav)
```

---

## HTML PAGE SKELETON (every guide)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>...</title>
  <!-- full SEO meta block: description, keywords, author, robots,
       canonical, og:*, twitter:*, article:modified_time -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>/* BLOCK 1 — master CSS, injected by patch_master_css.py */</style>
  <style>/* BLOCK 2 — per-guide CSS */</style>
</head>
<body>

<!-- LAYER 1: Sticky site header, z-index 200 -->
<header class="site-header">
  <a class="brand" href="https://williamriveromd.com">W. G. M. <strong>Rivero</strong>, MD</a>
  <div style="display:flex;align-items:center;gap:16px;">
    <button class="dark-toggle" id="darkToggle" onclick="toggleDark()" aria-label="Toggle dark mode">
      <span id="darkLabel">Dark</span>
    </button>
    <a class="back" href="index.html">← All Guides</a>
  </div>
</header>

<!-- LAYER 2: Lang toggle bar -->
<div class="guide-toggle-bar">
  <div class="guide-lang-bar">
    <span class="lang-lbl">Lang:</span>
    <button class="lang-btn-g active" id="glb-en" onclick="setGuideLang('en')">EN</button>
    <!-- add tl/ceb/kap buttons only if the guide has multilingual content -->
  </div>
</div>

<!-- LAYER 3: Hero — navy bg -->
<div class="hero">
  <div class="container">
    <div class="hero-badge-row">
      <span class="hbadge clin">⚕ Clinician Reference</span>
      <span class="hbadge kdigo">KDIGO 2024</span>
      <span class="hbadge ph">🇵🇭 Philippines Context</span>
    </div>
    <h1>Title<br><em>Italic subtitle phrase</em></h1>
    <p class="hero-sub">Lead paragraph...</p>
    <div class="hero-meta-row">
      <span>W Rivero, MD, FPCP, DPSN</span>
      <span>Last reviewed: May 2026</span>
      <span>Internal Medicine · Nephrology</span>
    </div>
    <div class="clin-banner">
      <strong>Clinical use only.</strong> These protocols are decision-support tools for licensed practitioners...
    </div>
  </div>
</div>

<!-- LAYER 4: Drug/section nav bar, sticky top: 56px, z-index: 140 -->
<nav class="algo-nav" aria-label="Section navigation">
  <div class="algo-nav-inner">
    <a class="anl" href="#section-id"><span class="anl-num">1</span>Label</a>
    ...
  </div>
</nav>

<!-- MAIN CONTENT -->
<div class="container">
  <!-- content sections -->
</div>

<!-- RELATED GUIDES (rendered from JS or static) -->

<!-- FOOTER -->
<footer class="guide-footer">
  <div class="footer-inner">
    <p>© 2026 W Rivero, MD · <a href="https://williamriveromd.com">williamriveromd.com</a></p>
    <p><a href="index.html">← All Patient Guides</a> · <a href="../index.html">Home</a></p>
  </div>
</footer>

<!-- FABs -->
<button class="print-btn" onclick="window.print()" title="Print this guide" aria-label="Print">
  <!-- printer SVG -->
</button>
<button class="scroll-top-btn" id="scrollTopBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Back to top">
  <!-- chevron-up SVG -->
</button>

<script>
  /* dark mode + scroll highlight + lang stub — see JS section */
</script>
</body>
</html>
```

---

## MASTER CSS COMPONENTS (Block 1 — available in every guide)

Never recreate these in Block 2. Use them directly.

### Layout
| Class | Description |
|---|---|
| `.container` | `max-width: 860px`, margin auto, `padding: 0 32px` |
| `.two-col` | `grid 1fr 1fr`, gap 20px → collapses to 1-col at 600px |
| `.three-col` | `auto-fit minmax(220px,1fr)` → collapses at 600px |
| `.section` | `padding: 64px 0`, border-bottom |

### Hero badges (confirmed values)
```css
.hbadge.clin  { background: rgba(196,132,60,.15); border: 1px solid rgba(196,132,60,.4); color: #f0c070; }
.hbadge.kdigo { background: rgba(26,107,114,.18); border: 1px solid rgba(26,107,114,.4); color: #5dcdd5; }
.hbadge.ph    { background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.18); color: rgba(255,255,255,.65); }
```

### Alert boxes
```html
<div class="alert alert-red">
  <span class="alert-icon">⚠</span>
  <div class="alert-body"><h4>Title</h4><p>Body</p></div>
</div>
```
Modifiers: `.alert-red` · `.alert-amber` · `.alert-green` · `.alert-teal` · `.alert-purple`

### Tables
| Class | Use |
|---|---|
| `.lab-table` `.drug-table` `.schedule-table` | General data tables — th: 11px uppercase, navy bg; td: 14px |
| `.tt` | Threshold table with row color variants |

`.tt` row variants:
```html
<tr class="tr-ok"><td>...</td></tr>       <!-- green wash -->
<tr class="tr-warn"><td>...</td></tr>     <!-- amber wash -->
<tr class="tr-urgent"><td>...</td></tr>   <!-- red wash -->
<tr class="tr-alt"><td>...</td></tr>      <!-- --bg wash -->
```

### Badges (inline status labels)
`.target-badge` `.warn-badge` `.amber-badge` `.caution-badge` `.safe-badge` `.avoid-badge` `.contraindicated-badge` `.purple-badge` `.teal-badge`

### Drug chips (inline)
```html
<span class="dc dc-ok">continue</span>
<span class="dc dc-caution">reduce dose</span>
<span class="dc dc-stop">hold</span>
<span class="dc dc-navy">monitor</span>
```

### Steps
```html
<div class="steps">
  <div class="step"><div class="step-num">1</div><div class="step-content">...</div></div>
</div>
```
`.step-num` = 36px navy circle, white text.

### Callouts
```html
<div class="intro-callout">...</div>   <!-- navy bg, white text -->
<div class="red-flags">...</div>       <!-- red-soft bg, Lora h3 in --red -->
```

### Dot indicators
`.dot` + `.dot-teal` `.dot-red` `.dot-amber` `.dot-green` `.dot-navy` `.dot-purple` `.dot-gold` `.dot-orange`

### Related guides section
```html
<div class="related-guides">
  <div class="related-cards">
    <a href="other-guide.html" class="related-card">
      <span class="related-card-tag">Category</span>
      <div class="related-card-title">Guide Title</div>
      <div class="related-card-desc">Short description.</div>
      <span class="related-card-arrow">→</span>
    </a>
  </div>
</div>
```

---

## PER-GUIDE CSS COMPONENTS (Block 2 — already in medication-operational-guide.html)

These exist in the current file. **Keep them all** in the rewrite — they are used and tested.

### Algorithm flow system
```html
<div class="flow">
  <div class="fs">
    <span class="fb fb-trigger">Trigger</span>
    <div class="fc">
      <div class="fq">Question or step title</div>
      <div class="fd">Detail text. <code>eGFR &lt;45</code></div>
    </div>
  </div>
</div>
```
`.fb` variants: `.fb-trigger` (navy) · `.fb-decision` (teal-tinted) · `.fb-action` (green) · `.fb-warn` (amber) · `.fb-stop` (red) · `.fb-refer` (navy-light)

Branch grids:
```html
<div class="fbr">           <!-- 2-col, collapses at 600px -->
  <div class="br br-yes"><div class="brl">Yes</div>...</div>
  <div class="br br-no"><div class="brl">No</div>...</div>
</div>
<div class="fbr fbr-3">    <!-- 3-col -->
  <div class="br br-a">...</div>
  <div class="br br-b">...</div>
  <div class="br br-c">...</div>
</div>
```

### Quick reference box
```html
<div class="qref">
  <h4>Quick Reference</h4>
  <ul><li>Item with <code>threshold</code></li></ul>
</div>
<div class="qref qref-grid">  <!-- 2-col layout -->
  <div>...</div><div>...</div>
</div>
```

### Titration ladder
```html
<div class="titration-ladder">
  <div class="tl-row">
    <div class="tl-week">Wk 1–4</div>
    <div class="tl-dose">
      <strong>0.25 mg SC</strong> weekly
      <div class="tl-note">With food. Monitor GI tolerance.</div>
    </div>
  </div>
</div>
```

### K+ traffic light
```html
<div class="k-ladder">
  <div class="k-row k-ok">
    <div class="k-level">K⁺ &lt;5.0</div>
    <div class="k-action"><strong>Continue RAASi.</strong> Routine monitoring.</div>
  </div>
  <div class="k-row k-amber">...</div>
  <div class="k-row k-orange">...</div>
  <div class="k-row k-red">...</div>
</div>
```

### Dose equivalence cards
```html
<div class="dose-eq">
  <div class="deq">
    <div class="deq-val">40 mg</div>
    <div class="deq-drug">Furosemide</div>
    <div class="deq-note">oral, variable absorption</div>
  </div>
</div>
```

### Algorithm nav + sections
```html
<!-- Nav link -->
<a class="anl" href="#drug-1"><span class="anl-num">1</span>SGLT2i</a>

<!-- Section (scroll-margin-top: 112px already set) -->
<section class="algo-section" id="drug-1">
  <div class="algo-hdr">
    <div class="algo-badge">1</div>
    <h2 class="algo-title">Drug Name</h2>
  </div>
  <p class="algo-subtitle">...</p>
</section>
```

### Formula display
```html
<div class="formula">GFR = 141 × min(Scr/κ, 1)^α × max(Scr/κ, 1)^−1.209 × 0.993^Age</div>
```

---

## NEW COMPONENTS TO BUILD (Part 1 & 2 redesign)

Add all to Block 2 (per-guide CSS). Each **must** have a `html[data-theme="dark"]` override.

### 1. Expandable panels

```css
/* Block 2 */
.opx-panel { border: 1px solid var(--border); border-radius: 12px; overflow: hidden; margin-bottom: 12px; }
.opx-hdr { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; cursor: pointer; background: var(--bg); user-select: none; }
.opx-hdr:hover { background: #f0f4f8; }
.opx-title { font-size: 14px; font-weight: 600; color: var(--navy); display: flex; align-items: center; gap: 10px; }
.opx-arrow { font-size: 12px; color: var(--text-muted); transition: transform .25s ease; }
.opx-panel.open .opx-arrow { transform: rotate(180deg); }
.opx-body { max-height: 0; overflow: hidden; transition: max-height .3s ease; }
.opx-body-inner { padding: 20px 24px; border-top: 1px solid var(--border); }

html[data-theme="dark"] .opx-panel { border-color: #2a3548; }
html[data-theme="dark"] .opx-hdr { background: #141c2a; }
html[data-theme="dark"] .opx-hdr:hover { background: #1a2535; }
html[data-theme="dark"] .opx-body-inner { border-color: #2a3548; }
```

```html
<div class="opx-panel" id="panel-who">
  <div class="opx-hdr" onclick="togglePanel(this)">
    <span class="opx-title">▶ Panel 1 — Who &amp; When</span>
    <span class="opx-arrow">▼</span>
  </div>
  <div class="opx-body">
    <div class="opx-body-inner">
      <!-- panel content -->
    </div>
  </div>
</div>
```

```javascript
function togglePanel(hdr) {
  const panel = hdr.closest('.opx-panel');
  const body = panel.querySelector('.opx-body');
  const isOpen = panel.classList.contains('open');
  panel.classList.toggle('open', !isOpen);
  body.style.maxHeight = isOpen ? '0' : body.scrollHeight + 'px';
}

function expandAll(btn, sectionId) {
  const section = document.getElementById(sectionId);
  const panels = section.querySelectorAll('.opx-panel');
  const allOpen = [...panels].every(p => p.classList.contains('open'));
  panels.forEach(p => {
    p.classList.toggle('open', !allOpen);
    p.querySelector('.opx-body').style.maxHeight =
      allOpen ? '0' : p.querySelector('.opx-body').scrollHeight + 'px';
  });
  btn.textContent = allOpen ? 'Expand all' : 'Collapse all';
}
```

### 2. Drug header card

```css
.drug-header { background: var(--navy); border-radius: 16px; padding: 28px 32px; margin-bottom: 28px; }
.drug-name { font-family: 'Lora', serif; font-size: clamp(20px,3vw,26px); font-weight: 600; color: white; line-height: 1.2; margin-bottom: 6px; }
.drug-tagline { font-size: 14px; color: rgba(255,255,255,.72); line-height: 1.5; }
.drug-brands { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px; }
.brand-chip { font-size: 11px; font-weight: 600; border-radius: 8px; padding: 3px 10px; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.18); color: rgba(255,255,255,.85); }
.drug-stats-row { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,.12); }
.dstat { text-align: left; }
.dstat-val { font-family: 'Lora', serif; font-size: 20px; color: #d4af4f; line-height: 1.1; }
.dstat-lbl { font-size: 10px; text-transform: uppercase; letter-spacing: .06em; color: rgba(255,255,255,.5); margin-top: 2px; }
.tier-badge { display: inline-flex; align-items: center; border-radius: 20px; padding: 3px 10px; font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 12px; }
.tier-1 { background: rgba(212,175,79,.18); border: 1px solid rgba(212,175,79,.4); color: #d4af4f; }
.tier-2 { background: rgba(26,107,114,.2); border: 1px solid rgba(26,107,114,.4); color: #5dcdd5; }

html[data-theme="dark"] .drug-header { background: #080d16; }
```

```html
<div class="drug-header">
  <span class="tier-badge tier-1">Tier 1 Drug</span>
  <div class="drug-name">SGLT2 Inhibitors</div>
  <div class="drug-tagline">Empagliflozin · Dapagliflozin — Standard of care for CKD + HF</div>
  <div class="drug-brands">
    <span class="brand-chip">Jardiance (empagliflozin)</span>
    <span class="brand-chip">Forxiga (dapagliflozin)</span>
  </div>
  <div class="drug-stats-row">
    <div class="dstat"><div class="dstat-val">eGFR ≥20</div><div class="dstat-lbl">CKD start threshold</div></div>
    <div class="dstat"><div class="dstat-val">EMPA-KIDNEY</div><div class="dstat-lbl">Key trial</div></div>
  </div>
</div>
```

### 3. Nursing callout box

```css
.nursing-box { background: rgba(107,33,168,.06); border: 1px solid rgba(107,33,168,.2); border-left: 4px solid var(--purple); border-radius: 10px; padding: 16px 20px; margin: 16px 0; }
.nursing-box-hdr { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--purple); display: flex; align-items: center; gap: 6px; margin-bottom: 10px; }
.nursing-box ul { padding-left: 18px; margin: 0; }
.nursing-box ul li { font-size: 13px; color: var(--text-mid); margin-bottom: 5px; line-height: 1.5; }

html[data-theme="dark"] .nursing-box { background: rgba(107,33,168,.12); border-color: rgba(107,33,168,.3); border-left-color: var(--purple); }
```

```html
<div class="nursing-box">
  <div class="nursing-box-hdr">🩺 Nursing Points</div>
  <ul>
    <li>Check eGFR and serum K⁺ before first dose</li>
    <li>Educate patient on genital hygiene — fungal infection risk</li>
  </ul>
</div>
```

### 4. Philippine context box

```css
.ph-box { background: rgba(0,112,60,.05); border: 1px solid rgba(0,112,60,.2); border-left: 4px solid #1a6b40; border-radius: 10px; padding: 16px 20px; margin: 16px 0; }
.ph-box-hdr { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: #1a6b40; display: flex; align-items: center; gap: 6px; margin-bottom: 10px; }
.ph-box p, .ph-box ul li { font-size: 13px; color: var(--text-mid); line-height: 1.6; }
.ph-box ul { padding-left: 18px; margin: 4px 0; }

html[data-theme="dark"] .ph-box { background: rgba(0,112,60,.1); border-color: rgba(0,112,60,.25); }
```

```html
<div class="ph-box">
  <div class="ph-box-hdr">🇵🇭 Philippine Context</div>
  <ul>
    <li><strong>Jardiance (empagliflozin 10mg):</strong> ~₱70–90/tab — no PhilHealth coverage as of 2026</li>
    <li><strong>Forxiga (dapagliflozin 10mg):</strong> ~₱60–85/tab</li>
    <li>Generic empagliflozin not yet available in PH</li>
  </ul>
</div>
```

### 5. Common mistakes box

```css
.mistake-box { background: var(--red-soft); border: 1px solid rgba(185,28,28,.2); border-left: 4px solid var(--red); border-radius: 10px; padding: 16px 20px; margin: 16px 0; }
.mistake-box-hdr { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--red); display: flex; align-items: center; gap: 6px; margin-bottom: 10px; }
.mistake-item { display: flex; gap: 10px; margin-bottom: 10px; }
.mistake-item:last-child { margin-bottom: 0; }
.mistake-x { color: var(--red); font-weight: 700; flex-shrink: 0; line-height: 1.55; }
.mistake-text { font-size: 13px; color: var(--text-mid); line-height: 1.55; }
.mistake-fix { font-size: 12px; color: var(--green); margin-top: 3px; font-weight: 500; }
.mistake-fix::before { content: '→ '; }

html[data-theme="dark"] .mistake-box { background: #2a1515; border-color: rgba(185,28,28,.3); }
```

```html
<div class="mistake-box">
  <div class="mistake-box-hdr">✗ Common Mistakes</div>
  <div class="mistake-item">
    <span class="mistake-x">✗</span>
    <div>
      <div class="mistake-text">Stopping SGLT2i when creatinine rises after starting</div>
      <div class="mistake-fix">Cr rise ≤30% from baseline is hemodynamic — expected and beneficial. Continue.</div>
    </div>
  </div>
</div>
```

### 6. Scenario card

```css
.scenario-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 18px 20px; margin: 12px 0; }
.scenario-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--teal); margin-bottom: 8px; }
.scenario-q { font-size: 14px; font-weight: 600; color: var(--navy); margin-bottom: 8px; line-height: 1.4; }
.scenario-a { font-size: 13px; color: var(--text-mid); line-height: 1.65; }

html[data-theme="dark"] .scenario-card { background: #141c2a; border-color: #2a3548; }
```

```html
<div class="scenario-card">
  <div class="scenario-label">Clinical Scenario</div>
  <div class="scenario-q">Patient's creatinine went from 1.5 → 1.9 mg/dL two weeks after starting empagliflozin. Should I stop?</div>
  <div class="scenario-a">No. This is a 27% rise — hemodynamic, expected, protective. Continue empagliflozin. Recheck in 4–6 weeks; creatinine usually stabilizes or improves.</div>
</div>
```

### 7. Clinical pearl list

```css
.pearl-list { margin: 12px 0; }
.pearl-item { display: flex; align-items: flex-start; gap: 10px; padding: 10px 0; border-bottom: 1px dashed var(--border); }
.pearl-item:last-child { border-bottom: none; }
.pearl-gem { font-size: 14px; flex-shrink: 0; line-height: 1.6; }
.pearl-text { font-size: 13px; color: var(--text-mid); line-height: 1.6; }
.pearl-text strong { color: var(--navy); }

html[data-theme="dark"] .pearl-item { border-color: #2a3548; }
```

```html
<div class="pearl-list">
  <div class="pearl-item">
    <span class="pearl-gem">💎</span>
    <div class="pearl-text"><strong>Sick day rule:</strong> Hold SGLT2i if vomiting, diarrhea, or nothing-by-mouth &gt;12 hours. Restart when eating and drinking normally.</div>
  </div>
</div>
```

### 8. Expand-all button

```css
.expand-all-btn { font-size: 12px; font-weight: 600; color: var(--teal); background: none; border: 1px solid rgba(26,107,114,.3); padding: 5px 14px; border-radius: 20px; cursor: pointer; transition: background .15s, color .15s; }
.expand-all-btn:hover { background: var(--teal); color: white; }
```

```html
<div class="drug-section-hdr">
  <h2 class="drug-section-title">SGLT2 Inhibitors</h2>
  <button class="expand-all-btn" onclick="expandAll(this, 'drug-sglt2')">Expand all</button>
</div>
```

### 9. Drug section wrapper

```css
.drug-section { padding: 48px 0; border-bottom: 2px solid var(--border); scroll-margin-top: 112px; }
.drug-section:last-of-type { border-bottom: none; }
.drug-section-hdr { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; flex-wrap: wrap; gap: 12px; }
```

### 10. Part-to-part navigation box

```css
.part-nav-box { background: var(--navy); border-radius: 16px; padding: 28px 32px; text-align: center; margin: 40px 0; }
.part-nav-box h3 { font-family: 'Lora', serif; font-size: 18px; color: #d4af4f; margin-bottom: 6px; font-weight: 500; }
.part-nav-box p { font-size: 14px; color: rgba(255,255,255,.7); }
.part-link { display: inline-flex; align-items: center; gap: 8px; margin-top: 16px; padding: 10px 24px; background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.25); border-radius: 8px; color: white; font-size: 14px; font-weight: 600; text-decoration: none; transition: background .15s; }
.part-link:hover { background: rgba(255,255,255,.2); }

html[data-theme="dark"] .part-nav-box { background: #080d16; }
```

```html
<div class="part-nav-box">
  <h3>Continue to Part 2</h3>
  <p>Anticoagulation · Pain &amp; Gout · Antibiotics · Anemia/ESA · Phosphate Binders · Statins</p>
  <a href="medication-operational-guide-2.html" class="part-link">Part 2 — Tier 2 Drugs →</a>
</div>
```

### Mobile overrides (always include)

```css
@media (max-width: 600px) {
  .drug-header { padding: 20px; border-radius: 12px; }
  .drug-stats-row { gap: 12px; }
  .opx-body-inner { padding: 14px 16px; }
  .k-level { min-width: 88px; font-size: 12px; }
  .tl-week { min-width: 64px; }
}
```

### Print overrides (always include)

```css
@media print {
  .algo-nav, .guide-toggle-bar, .site-header,
  .print-btn, .scroll-top-btn, .expand-all-btn { display: none !important; }
  .opx-body { max-height: none !important; }
  .drug-header { background: #1f3864 !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .drug-section { page-break-inside: avoid; border: none; }
  .k-ladder, .nursing-box, .ph-box, .mistake-box { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
```

---

## JAVASCRIPT (complete, verified block)

```javascript
// ── Dark mode ─────────────────────────────────────────────────────────────
const DARK_KEY = 'wgmr-dark';
function toggleDark() {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  document.documentElement.setAttribute('data-theme', isDark ? 'light' : 'dark');
  localStorage.setItem(DARK_KEY, isDark ? '' : '1');
  const btn = document.getElementById('darkLabel');
  if (btn) btn.textContent = isDark ? 'Dark' : 'Light';
}
(function() {
  if (localStorage.getItem(DARK_KEY)) {
    document.documentElement.setAttribute('data-theme', 'dark');
    const btn = document.getElementById('darkLabel');
    if (btn) btn.textContent = 'Light';
  }
})();

// ── Scroll: nav highlight + scroll-top button ─────────────────────────────
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  document.getElementById('scrollTopBtn')?.classList.toggle('visible', scrollY > 400);
  let current = '';
  document.querySelectorAll('.drug-section[id]').forEach(s => {
    if (scrollY >= s.offsetTop - 140) current = s.id;
  });
  document.querySelectorAll('.anl').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === '#' + current);
  });
}, { passive: true });

// ── Language stub ─────────────────────────────────────────────────────────
const GLANG_KEY = 'wgmr-lang';
function setGuideLang(lang) { localStorage.setItem(GLANG_KEY, lang); }
(function() { localStorage.getItem(GLANG_KEY) || 'en'; })();

// ── Expandable panels ─────────────────────────────────────────────────────
function togglePanel(hdr) {
  const panel = hdr.closest('.opx-panel');
  const body = panel.querySelector('.opx-body');
  const isOpen = panel.classList.contains('open');
  panel.classList.toggle('open', !isOpen);
  body.style.maxHeight = isOpen ? '0' : body.scrollHeight + 'px';
}

function expandAll(btn, sectionId) {
  const section = document.getElementById(sectionId);
  const panels = section.querySelectorAll('.opx-panel');
  const allOpen = [...panels].every(p => p.classList.contains('open'));
  panels.forEach(p => {
    p.classList.toggle('open', !allOpen);
    p.querySelector('.opx-body').style.maxHeight =
      allOpen ? '0' : p.querySelector('.opx-body').scrollHeight + 'px';
  });
  btn.textContent = allOpen ? 'Expand all' : 'Collapse all';
}
```

---

## MULTILINGUAL PATTERN

The medication guide redesign is **English only** — no multilingual spans needed.

If you ever add multilingual content to any guide:
```html
<span data-lang="en">English</span>
<span data-lang="tl" class="lang-hidden">Tagalog</span>
<span data-lang="ceb" class="lang-hidden">Cebuano</span>
<span data-lang="kap" class="lang-hidden">Kapampangan</span>
```
- Guide buttons use prefix `glb-` → `id="glb-en"` `id="glb-tl"` etc.
- Homepage buttons use prefix `lb-` → `id="lb-en"` etc.

---

## PENDING TASK: THE REDESIGN

### File 1: `guides/medication-operational-guide.html` — COMPLETE REWRITE

**Title:** Applied Clinical Therapeutics in CKD & Cardiometabolic Medicine
**Subtitle:** Operational protocols for the multidisciplinary Filipino clinician
**Part:** 1 of 2 — Tier 1 Drugs

**5 drug sections, each with exactly 3 expandable panels:**

| # | Drug | Panel 1 | Panel 2 | Panel 3 |
|---|---|---|---|---|
| 1 | SGLT2 Inhibitors | Who & When (eGFR ≥20, CIs, pre-start checklist) | Start Protocol + Cr dip + sick-day rules | Troubleshooting + PH brands/cost |
| 2 | GLP-1 / Dual Agonists | Who & When (CKD dose adj, CIs) | Titration ladder (sema/dula/tirz) | Nausea mgmt + cold chain + PH |
| 3 | Insulin in CKD | Principles (dose↓ by eGFR, avoid NPH G4-5) | Dose table by eGFR + monitoring + A1c caveat | Hypo mgmt + post-HD risk + PH |
| 4 | ACEi / ARB / RAAS + Finerenone | Who & When + starting doses | Cr rise interpretation (≤30% = OK, do NOT stop) | Hyperkalemia ladder + finerenone + PH |
| 5 | Diuretics | Loop principles + dose equivalences | Sequential nephron blockade protocol | Diuretic resistance + electrolytes + PH |

**Nav links to use:**
```html
<a class="anl" href="#drug-sglt2"><span class="anl-num">1</span>SGLT2i</a>
<a class="anl" href="#drug-glp1"><span class="anl-num">2</span>GLP-1</a>
<a class="anl" href="#drug-insulin"><span class="anl-num">3</span>Insulin</a>
<a class="anl" href="#drug-raas"><span class="anl-num">4</span>ACEi/ARB/RAAS</a>
<a class="anl" href="#drug-diuretics"><span class="anl-num">5</span>Diuretics</a>
```

**Section IDs to use:** `drug-sglt2`, `drug-glp1`, `drug-insulin`, `drug-raas`, `drug-diuretics`

---

### File 2: `guides/medication-operational-guide-2.html` — NEW FILE

**Title:** Applied Clinical Therapeutics in CKD — Part 2
**Subtitle:** Tier 2 drug protocols: anticoagulation, pain, antibiotics, anemia, binders, statins
**Part:** 2 of 2 — Tier 2 Drugs

**6 sections (condensed format — 2 panels each):**
1. Anticoagulation in CKD (DOACs dose adjustment, bridging, reversal agents)
2. Pain & Gout in CKD (avoid NSAIDs, acetaminophen dosing, colchicine, allopurinol)
3. Antibiotics in CKD Dose Adjustment (key drug table)
4. CKD Anemia / ESA (darbepoetin, epoetin, iron targets, hemoglobin goals)
5. Phosphate Binders (calcium-based vs sevelamer vs lanthanum, timing with meals)
6. Statins in CKD (which to use, avoid in dialysis per SHARP, rosuvastatin preferred)

---

## CLINICAL FACTS — DO NOT GET WRONG

### SGLT2 Inhibitors
- Start threshold: **eGFR ≥20** (CKD benefit, HF benefit). Not eGFR ≥30.
- Creatinine dip after starting: **≤30% rise is hemodynamic, acceptable, do NOT stop.** Most common error.
- Sick-day rule: **Hold** if vomiting, diarrhea, or NPO >12h. Restart when eating normally.
- Euglycemic DKA: can occur even with normal glucose. Educate patient.
- Pre-op: hold **3 days** before elective surgery with general anesthesia.
- **Not** for eGFR <20 (glycosuric benefit lost; CV/kidney benefit still possible but off-label).

### GLP-1 / Dual Agonists
- CKD dose adjustment: **No dose adjustment needed** for semaglutide, dulaglutide in any CKD stage.
- Titration rule: **Do NOT escalate dose if patient is still nauseated** at current dose.
- Ozempic pen: refrigerate until first use, then room temp ≤6 weeks (pen in use).
- Rybelsus (oral semaglutide): requires **30 min fasting** before dose, with ≤120mL water only.
- Tirzepatide (Mounjaro): limited PH availability; ~₱12,000–20,000/pen.

### Insulin in CKD
- Dose reduction thresholds: eGFR 45–60 → ↓10–15%; eGFR 30–44 → ↓25%; eGFR 15–29 → ↓50%; ESRD/dialysis → ↓50–75%
- **Avoid NPH in CKD G4–G5** (Insulatard): active metabolites accumulate → prolonged hypoglycemia.
- A1c is **unreliable in ESRD** (falsely low due to hemolysis, erythropoietin use). Use fructosamine instead.
- Post-HD hypoglycemia: common within 4–6h of dialysis. Reduce pre-meal dose on dialysis days.

### ACEi / ARB / RAAS + Finerenone
- **Creatinine rise ≤30% = hemodynamic, BENEFICIAL — do NOT stop.** Stopping is the #1 clinical error.
- Acceptable Cr rise = intrarenal hemodynamics responding correctly. Recheck in 2–4 weeks.
- **Dual RAAS blockade (ACEi + ARB together) = HARMFUL** — hyperkalemia + AKI risk. Never combine.
- Cough on ACEi → switch to ARB (losartan, valsartan).
- Finerenone (Kerendia): start only if K⁺ <5.0. Recheck K⁺ at 4 weeks then every 3 months.
- K⁺ management ladder:
  - K⁺ <5.0: continue RAASi, routine monitoring
  - K⁺ 5.0–5.4: diet counseling (low-K foods), recheck 2–4 weeks, continue RAASi
  - K⁺ 5.5–5.9: add patiromer 8.4g QD with food (separate from other meds ≥3h) OR SZC 10g TID ×48h → 5g QD; continue RAASi
  - K⁺ ≥6.0: hold RAASi, emergency management

### Diuretics
- Dose equivalences (bioequivalent): **furosemide 40mg = torsemide 20mg = bumetanide 1mg**
- Bioavailability: torsemide ~80–90% (predictable) vs furosemide 40–70% (variable absorption in CKD)
- **HCTZ (hydrochlorothiazide) is ineffective when eGFR <30** → use metolazone instead
- Sequential nephron blockade: **metolazone 2.5–5mg given 30–60 min BEFORE** loop diuretic dose
- Monitor: Na⁺, K⁺, Cr after any diuretic dose change. Aggressive diuresis → AKI risk.

---

## PHILIPPINE DRUG BRANDS & COSTS (2026)

| Drug | Brand / Generic | Approx Cost | Notes |
|---|---|---|---|
| Empagliflozin 10mg | Jardiance | ₱70–90/tab | No generic available |
| Dapagliflozin 10mg | Forxiga | ₱60–85/tab | No generic available |
| Canagliflozin | Invokana | ₱70–95/tab | Less CKD data |
| Semaglutide SC | Ozempic 0.25/0.5/1mg pen | ₱3,500–6,000/pen | Refrigerate until use |
| Oral semaglutide | Rybelsus 3/7/14mg | ₱2,800–5,000/30 tabs | 30 min fasting required |
| Dulaglutide | Trulicity 0.75/1.5mg | ₱2,500–4,500/pen | Weekly SC |
| Tirzepatide | Mounjaro | ₱12,000–20,000/pen | Limited availability |
| Glargine 100 | Lantus, Basaglar | ₱1,500–2,000/vial | Preferred basal in CKD |
| Regular insulin | Actrapid, Humulin R | ₱400–600/vial | |
| NPH insulin | Insulatard | ₱300–450/vial | AVOID in CKD G4–5 |
| Lisinopril 5/10mg | Zestril, generic | ₱5–15/tab | Cheapest ACEi |
| Enalapril 5/10mg | Enacard, generic | ₱5–10/tab | |
| Losartan 50/100mg | Cozaar, generic | ₱12–25/tab | First-line ARB |
| Finerenone 10/20mg | Kerendia | ₱150–250/tab | New; no PhilHealth |
| Furosemide 40mg | Lasix, generic | ₱3–8/tab | Cheapest loop diuretic |
| Torsemide 10/20mg | Demadex, generic | ₱40–70/tab | Preferred in HF |
| Bumetanide 1mg | Bumex | ₱50–90/tab | |
| Metolazone 2.5/5mg | Zaroxolyn | ₱35–60/tab | With loop diuretic |

PhilHealth coverage note: As of 2026, most branded CKD drugs (SGLT2i, GLP-1, finerenone) are NOT covered. Generic ACEi/ARBs and furosemide are covered under Z-package or outpatient benefit.

---

## AFTER WRITING EACH FILE

```bash
# 1. Inject master CSS into the guide
python3 patch_master_css.py --guide medication-operational-guide.html
python3 patch_master_css.py --guide medication-operational-guide-2.html

# 2. Add Part 2 entries (Part 1 already exists):
#    - guides/index.html: new tile in "Advanced & Emerging Topics" section
#    - sitemap.xml: new <url> block, priority 0.8, lastmod 2026-05-16
#    - related_guides.json: cross-links between Part 1, Part 2, and related guides

# 3. Commit and push
git add guides/medication-operational-guide.html guides/medication-operational-guide-2.html guides/index.html sitemap.xml related_guides.json
git commit -m "Redesign medication guide as two-part Applied Clinical Therapeutics reference"
git push origin main
```

### guides/index.html tile format (copy/adapt)
```html
<a href="guides/medication-operational-guide-2.html" class="guide-card" data-text="...keywords...">
  <div class="card-img-wrap">
    <img src="images/medication-operational-guide-2.webp" alt="..." loading="lazy" />
  </div>
  <div class="card-body">
    <span class="card-tag">Pharmacology</span>
    <h3 class="card-title">Applied Clinical Therapeutics — Part 2</h3>
    <p class="card-desc">Anticoagulation, pain, antibiotics, anemia/ESA, phosphate binders, and statins in CKD.</p>
  </div>
</a>
```

### sitemap.xml entry format
```xml
<url>
  <loc>https://williamriveromd.com/guides/medication-operational-guide-2.html</loc>
  <lastmod>2026-05-16</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

---

## DESIGN PRINCIPLES (non-negotiable)

1. **Never edit Block 1 (master CSS) directly** — use `patch_master_css.py`
2. **Use CSS tokens everywhere** — never hardcode hex in new rules
3. **WCAG AA on every new color pair** — verify ≥4.5:1 before adding
4. **Mobile-first** — all grids collapse to 1-col at 600px; test at 375px
5. **Dark mode** — every new component must have `html[data-theme="dark"]` override
6. **Print** — every new component needs `@media print` override (or inherits from master)
7. **No feature creep** — 3 panels per drug, not 20 sections
8. **No comments in HTML/CSS** except section separator lines (`/* ── NAME ─── */`)
9. **No multilingual spans** — medication guide redesign is English only
10. **Always read a file before editing it**
