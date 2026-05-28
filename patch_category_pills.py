#!/usr/bin/env python3
"""
patch_category_pills.py — williamriveromd.com
Adds clinical-category nav pills (Glomerular Dse, Hypertension, Diabetes,
Pre-Dialysis, Calculus, Nutrition, Transplant, System Nav, Prevention) to
every applicable guide tile in guides/index.html.

Also:
  - Adds CSS + dark-mode CSS for all new tag classes
  - Adds mobile filter pills + new sidebar "Filter by clinical topic" section
  - Fixes tag-nutrition (had no CSS rule)
  - Normalises "Clinician tab" → "Clinician" on every tile
  - Normalises tag-clin → tag-clinician (class name inconsistency)
"""

import re, sys

PATH = 'guides/index.html'

# ── guide → [(slug, label), ...] ──────────────────────────────────────────
NEW_GUIDE_TAGS = {
    # Glomerular Disease
    'hematuria-blood-in-urine.html':          [('glomerular',   'Glomerular Dse')],
    'glomerulonephritis.html':                 [('glomerular',   'Glomerular Dse')],
    'igan-guide.html':                         [('glomerular',   'Glomerular Dse')],
    'lupus-nephritis.html':                    [('glomerular',   'Glomerular Dse')],
    'hivan-hiv-kidney-disease.html':           [('glomerular',   'Glomerular Dse')],

    # Hypertension
    'hypertensive-kidney-disease.html':        [('hypertension', 'Hypertension'),
                                                ('pre-dialysis', 'Pre-Dialysis')],
    'managing-hypertension.html':              [('hypertension', 'Hypertension')],
    'heart-kidney-connection.html':            [('hypertension', 'Hypertension')],
    'sodium-salt-reduction-ckd.html':          [('hypertension', 'Hypertension'),
                                                ('nutrition',    'Nutrition')],
    'cardiac-rehab-ckd-post-mi.html':          [('hypertension', 'Hypertension')],

    # Diabetes
    'diabetes-kidneys.html':                   [('diabetes',     'Diabetes'),
                                                ('pre-dialysis', 'Pre-Dialysis')],
    'filipino-diabetic-diet.html':             [('diabetes',     'Diabetes')],
    'gdm-nutrition-nephrology.html':           [('diabetes',     'Diabetes'),
                                                ('nutrition',    'Nutrition')],
    'glp1-ozempic-ckd.html':                   [('diabetes',     'Diabetes'),
                                                ('pre-dialysis', 'Pre-Dialysis')],
    'vinegar-acv-guide.html':                  [('diabetes',     'Diabetes')],
    'obesity-ckd.html':                        [('diabetes',     'Diabetes'),
                                                ('nutrition',    'Nutrition')],

    # Pre-Dialysis
    'understanding-ckd.html':                  [('pre-dialysis', 'Pre-Dialysis')],
    'kidney-physiology.html':                  [('pre-dialysis', 'Pre-Dialysis')],
    'metabolic-acidosis-ckd.html':             [('pre-dialysis', 'Pre-Dialysis')],
    'slowing-ckd-progression.html':            [('pre-dialysis', 'Pre-Dialysis')],
    'proteins-proteinuria.html':               [('pre-dialysis', 'Pre-Dialysis')],
    'ckd-top5-mistakes.html':                  [('pre-dialysis', 'Pre-Dialysis')],
    'ckd-and-pregnancy.html':                  [('pre-dialysis', 'Pre-Dialysis')],
    'ckd-children-young-adults.html':          [('pre-dialysis', 'Pre-Dialysis')],
    'polycystic-kidney-disease.html':          [('pre-dialysis', 'Pre-Dialysis')],
    'first-nephrology-visit-guide.html':       [('pre-dialysis', 'Pre-Dialysis'),
                                                ('system-nav',   'System Nav')],
    'acute-kidney-injury-on-ckd.html':         [('pre-dialysis', 'Pre-Dialysis')],
    'nsaid-kidney-injury.html':                [('pre-dialysis', 'Pre-Dialysis'),
                                                ('prevention',   'Prevention')],
    'contrast-nephropathy.html':               [('pre-dialysis', 'Pre-Dialysis'),
                                                ('prevention',   'Prevention')],
    'new-therapeutic-agents-ckd.html':         [('pre-dialysis', 'Pre-Dialysis')],
    'dialysis-coming-pre-eskd.html':           [('pre-dialysis', 'Pre-Dialysis'),
                                                ('system-nav',   'System Nav')],
    'recurrent-uti-ckd.html':                  [('pre-dialysis', 'Pre-Dialysis'),
                                                ('prevention',   'Prevention')],
    'hantavirus-ckd.html':                     [('pre-dialysis', 'Pre-Dialysis'),
                                                ('prevention',   'Prevention')],
    'dengue-aki-kidney.html':                  [('pre-dialysis', 'Pre-Dialysis'),
                                                ('prevention',   'Prevention')],

    # Calculus (kidney stones / urolithiasis)
    'managing-kidney-stones.html':             [('calculus',     'Calculus')],
    'gout-uric-acid.html':                     [('calculus',     'Calculus')],
    'preventing-uti.html':                     [('calculus',     'Calculus'),
                                                ('prevention',   'Prevention')],
    'prostate-enlargement.html':               [('calculus',     'Calculus')],

    # Nutrition (adds visual pill; some already have nutrition in data-tags)
    'nutrition-kidney-patients.html':          [('nutrition',    'Nutrition')],
    'kain-pa-rin.html':                        [('nutrition',    'Nutrition')],
    'eating-on-dialysis.html':                 [('nutrition',    'Nutrition')],
    'ckd-dri-calculator.html':                 [('nutrition',    'Nutrition')],
    'ckd-recipe-analyzer.html':                [('nutrition',    'Nutrition')],
    'ckd-label-scanner.html':                  [('nutrition',    'Nutrition')],
    'ckd-friendly-recipes.html':               [('nutrition',    'Nutrition')],
    'understanding-iron.html':                 [('nutrition',    'Nutrition')],
    'nutrition-labels-ckd.html':               [('nutrition',    'Nutrition')],
    'meal-prep-fastfood-ckd.html':             [('nutrition',    'Nutrition')],
    'ckd-friendly-recipes-regional.html':      [('nutrition',    'Nutrition')],
    'ketogenic-chrononutrition-ckd.html':      [('nutrition',    'Nutrition')],
    'phosphorus-ckd.html':                     [('nutrition',    'Nutrition')],
    'food-kidney-toxins.html':                 [('nutrition',    'Nutrition'),
                                                ('prevention',   'Prevention')],
    'uremic-toxin-precursors.html':            [('nutrition',    'Nutrition')],
    'cooking-oils-fats-guide.html':            [('nutrition',    'Nutrition')],
    'cholesterol-diet-guide.html':             [('nutrition',    'Nutrition')],
    'ketoanalogue-supplementation.html':       [('nutrition',    'Nutrition')],
    'muscle-building-supplements-ckd.html':    [('nutrition',    'Nutrition')],
    'buko-juice-alkaline-water-ckd.html':      [('nutrition',    'Nutrition'),
                                                ('prevention',   'Prevention')],
    'natural-supplements-kidney.html':         [('nutrition',    'Nutrition'),
                                                ('prevention',   'Prevention')],

    # Transplant
    'kidney-transplant.html':                  [('transplant',   'Transplant')],
    'transplant-allograft-failure.html':       [('transplant',   'Transplant')],
    'organ-donation-philippines.html':         [('transplant',   'Transplant'),
                                                ('system-nav',   'System Nav')],
    'philhealth-z-packages.html':              [('transplant',   'Transplant'),
                                                ('system-nav',   'System Nav')],

    # System Nav
    'ckd-statistics-philippines.html':         [('system-nav',   'System Nav')],
    'understanding-lab-results.html':          [('system-nav',   'System Nav')],
    'medication-operational-guide.html':       [('system-nav',   'System Nav')],
    'practical-outpatient-algorithms.html':    [('system-nav',   'System Nav')],
    'hemodialysis-transfer-guide.html':        [('system-nav',   'System Nav')],
    'ckd-financial-stress.html':               [('system-nav',   'System Nav')],
    'zero-balance-billing-philhealth.html':    [('system-nav',   'System Nav')],
    'caregiver-guide-ckd.html':                [('system-nav',   'System Nav')],
    'advance-care-planning-dialysis.html':     [('system-nav',   'System Nav')],
    'travel-dialysis-ckd.html':                [('system-nav',   'System Nav')],

    # Prevention (not already covered above)
    'herbal-nephropathy.html':                 [('prevention',   'Prevention')],
    'ckd-alternative-holistic-medicine.html':  [('prevention',   'Prevention')],
    'viral-infections-vaccinations-ckd.html':  [('prevention',   'Prevention')],
    'tuberculosis-kidney-disease.html':        [('prevention',   'Prevention')],
    'leptospirosis-nephropathy.html':          [('prevention',   'Prevention')],
    'alcohol-ckd.html':                        [('prevention',   'Prevention')],
    'dyslipidemia-2026.html':                  [('prevention',   'Prevention')],
    'exercise-guide-ckd.html':                 [('prevention',   'Prevention')],
}

# ── CSS to insert ──────────────────────────────────────────────────────────
NEW_TAG_CSS = """
  .tag-nutrition    { background: #ecfdf5; color: #065f46; }
  .tag-hypertension { background: #fef2f2; color: #b91c1c; }
  .tag-diabetes     { background: #fffbeb; color: #b45309; }
  .tag-pre-dialysis { background: #f0fdf4; color: #166534; }
  .tag-calculus     { background: #fef3c7; color: #78350f; }
  .tag-transplant   { background: #eff6ff; color: #1d4ed8; }
  .tag-glomerular   { background: #fce7f3; color: #9d174d; }
  .tag-system-nav   { background: #f1f5f9; color: #334155; }
  .tag-prevention   { background: #f7fee7; color: #3f6212; }"""

NEW_TAG_DARK_CSS = """
  body.dark-mode .tag-nutrition    { background: rgba(6,95,70,.25);   color: #6ee7b7; }
  body.dark-mode .tag-hypertension { background: rgba(185,28,28,.22); color: #fca5a5; }
  body.dark-mode .tag-diabetes     { background: rgba(180,83,9,.22);  color: #fcd34d; }
  body.dark-mode .tag-pre-dialysis { background: rgba(22,101,52,.25); color: #86efac; }
  body.dark-mode .tag-calculus     { background: rgba(120,53,15,.25); color: #fcd34d; }
  body.dark-mode .tag-transplant   { background: rgba(29,78,216,.25); color: #93c5fd; }
  body.dark-mode .tag-glomerular   { background: rgba(157,23,77,.25); color: #f9a8d4; }
  body.dark-mode .tag-system-nav   { background: rgba(51,65,85,.35);  color: #94a3b8; }
  body.dark-mode .tag-prevention   { background: rgba(63,98,18,.25);  color: #bef264; }"""

# ── sidebar "Filter by clinical topic" section HTML ────────────────────────
SIDEBAR_CATEGORY_SECTION = """    <div class="sidebar-section">
      <div class="sidebar-heading">Filter by clinical topic</div>
      <button class="filter-btn" data-filter="pre-dialysis">
        <span class="filter-dot" style="background:#166534"></span>Pre-Dialysis<span class="count">21</span>
      </button>
      <button class="filter-btn" data-filter="dialysis">
        <span class="filter-dot" style="background:var(--navy)"></span>Dialysis<span class="count">16</span>
      </button>
      <button class="filter-btn" data-filter="hypertension">
        <span class="filter-dot" style="background:#b91c1c"></span>Hypertension<span class="count">5</span>
      </button>
      <button class="filter-btn" data-filter="diabetes">
        <span class="filter-dot" style="background:#b45309"></span>Diabetes<span class="count">6</span>
      </button>
      <button class="filter-btn" data-filter="nutrition">
        <span class="filter-dot" style="background:#065f46"></span>Nutrition<span class="count">26</span>
      </button>
      <button class="filter-btn" data-filter="transplant">
        <span class="filter-dot" style="background:#1d4ed8"></span>Transplant<span class="count">4</span>
      </button>
      <button class="filter-btn" data-filter="glomerular">
        <span class="filter-dot" style="background:#9d174d"></span>Glomerular Dse<span class="count">5</span>
      </button>
      <button class="filter-btn" data-filter="calculus">
        <span class="filter-dot" style="background:#78350f"></span>Calculus<span class="count">4</span>
      </button>
      <button class="filter-btn" data-filter="system-nav">
        <span class="filter-dot" style="background:#334155"></span>System Nav<span class="count">14</span>
      </button>
      <button class="filter-btn" data-filter="prevention">
        <span class="filter-dot" style="background:#3f6212"></span>Prevention<span class="count">17</span>
      </button>
    </div>"""

# ── mobile filter pills to append ─────────────────────────────────────────
MOBILE_PILLS_ADD = """\
  <button class="mf-pill" data-filter="pre-dialysis">Pre-Dialysis</button>
  <button class="mf-pill" data-filter="hypertension">Hypertension</button>
  <button class="mf-pill" data-filter="diabetes">Diabetes</button>
  <button class="mf-pill" data-filter="nutrition">Nutrition</button>
  <button class="mf-pill" data-filter="transplant">Transplant</button>
  <button class="mf-pill" data-filter="glomerular">Glomerular Dse</button>
  <button class="mf-pill" data-filter="calculus">Calculus</button>
  <button class="mf-pill" data-filter="system-nav">System Nav</button>
  <button class="mf-pill" data-filter="prevention">Prevention</button>
</div>"""

# ══════════════════════════════════════════════════════════════════════════
def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── 1. Fix Clinician tab label & tag-clin class ────────────────────
    html = html.replace('>Clinician tab<', '>Clinician<')
    html = html.replace('class="meta-tag tag-clin"', 'class="meta-tag tag-clinician"')

    # ── 2. CSS: new tag colours ────────────────────────────────────────
    ANCHOR_CSS = '  .tag-download { background: #fef9ec; color: #92710a; border: 1px solid #f5d97a; }'
    if ANCHOR_CSS in html:
        html = html.replace(ANCHOR_CSS, ANCHOR_CSS + NEW_TAG_CSS)
    else:
        print('WARNING: CSS anchor not found — new tag CSS not inserted', file=sys.stderr)

    # ── 3. CSS: dark-mode variants ─────────────────────────────────────
    DARK_ANCHOR = '  body.dark-mode .tag-decision { background: rgba(109,63,192,.25); color: #c4b5fd; border-color: rgba(109,63,192,.35); }'
    if DARK_ANCHOR in html:
        html = html.replace(DARK_ANCHOR, DARK_ANCHOR + NEW_TAG_DARK_CSS)
    else:
        print('WARNING: dark-mode CSS anchor not found', file=sys.stderr)

    # ── 4. Mobile filter bar: append new pills before closing </div> ───
    OLD_MOBILE_END = '  <button class="mf-pill" data-filter="download">Downloads</button>\n</div>'
    NEW_MOBILE_END = '  <button class="mf-pill" data-filter="download">Downloads</button>\n' + MOBILE_PILLS_ADD
    if OLD_MOBILE_END in html:
        html = html.replace(OLD_MOBILE_END, NEW_MOBILE_END)
    else:
        print('WARNING: mobile filter bar end not found', file=sys.stderr)

    # ── 5. Sidebar: insert category section before "Jump to section" ──
    JUMP_SECTION_ANCHOR = '    <div class="sidebar-section">\n      <div class="sidebar-heading">Jump to section</div>'
    if JUMP_SECTION_ANCHOR in html:
        html = html.replace(JUMP_SECTION_ANCHOR,
                            SIDEBAR_CATEGORY_SECTION + '\n' + JUMP_SECTION_ANCHOR)
    else:
        print('WARNING: sidebar jump-to-section anchor not found', file=sys.stderr)

    # ── 6. Per-tile: update data-tags + add visual tag spans ──────────
    for href, tag_list in NEW_GUIDE_TAGS.items():
        escaped = re.escape(href)
        # Match the whole <a ...> ... </a> tile block for this guide
        pattern = rf'(<a\s+href="{escaped}")((?:[^>]*?)data-tags="([^"]*)")((?:[^>]*?)>)(.*?)(</a>)'

        def make_replacer(tag_list=tag_list):
            def replacer(m):
                pre_tags   = m.group(1)   # <a href="..."
                mid_tags   = m.group(2)   # rest of attrs up to data-tags="..."
                cur_tags   = m.group(3)   # current data-tags value
                post_open  = m.group(4)   # rest of opening tag + >
                body       = m.group(5)   # tile body
                closing    = m.group(6)   # </a>

                # Update data-tags attribute
                tags = cur_tags.split() if cur_tags.strip() else []
                for slug, _ in tag_list:
                    if slug not in tags:
                        tags.append(slug)
                new_tags_val = ' '.join(tags)
                mid_updated = mid_tags.replace(
                    f'data-tags="{cur_tags}"',
                    f'data-tags="{new_tags_val}"'
                )

                # Build spans to add (skip if slug already present in body)
                new_spans = ''
                for slug, label in tag_list:
                    if f'tag-{slug}"' not in body:
                        new_spans += f'<span class="meta-tag tag-{slug}">{label}</span>'

                # Insert new spans into tile-meta
                def fix_meta(mm):
                    inner = mm.group(1)
                    return f'<div class="tile-meta">{inner}{new_spans}</div>'

                new_body = re.sub(
                    r'<div class="tile-meta">(.*?)</div>',
                    fix_meta, body, count=1, flags=re.DOTALL
                )

                return pre_tags + mid_updated + post_open + new_body + closing
            return replacer

        new_html, count = re.subn(pattern, make_replacer(), html, flags=re.DOTALL)
        if count == 0:
            print(f'WARNING: tile not found for {href}', file=sys.stderr)
        else:
            html = new_html

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Done. Patched {len(NEW_GUIDE_TAGS)} guide tiles in {PATH}.')

if __name__ == '__main__':
    main()
