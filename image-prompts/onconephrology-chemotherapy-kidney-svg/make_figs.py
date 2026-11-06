#!/usr/bin/env python3
"""Original code-native figures for onconephrology-chemotherapy-kidney (SVG source -> PNG master -> WebP).
Usage: python3 make_figs.py <repo-root>"""
import os, subprocess, sys
from PIL import Image

REPO = sys.argv[1]
SLUG = 'onconephrology-chemotherapy-kidney'
SRC = os.path.join(REPO, 'image-prompts', SLUG + '-svg')
IMG = os.path.join(REPO, 'images')
os.makedirs(SRC, exist_ok=True)
NAVY, TEAL, GREEN, AMBER, RED, PURPLE, SLATE = '#0f1e2e', '#1a6b72', '#1f7a4d', '#b8860b', '#b23b3b', '#4b3280', '#334155'
FONT = "Inter, sans-serif"


def T(x, y, s, size=28, w=600, fill=NAVY, anchor='start'):
    return '<text x="%d" y="%d" font-family="%s" font-size="%d" font-weight="%d" fill="%s" text-anchor="%s">%s</text>' % (x, y, FONT, size, w, fill, anchor, s)


def lines(x, y, rows, size=24, w=500, fill=SLATE, lh=1.38, anchor='start'):
    return ''.join(T(x, y + i * size * lh, r, size, w, fill, anchor) for i, r in enumerate(rows))


def box(x, y, w, h, fill, stroke, r=22, dash=False, sw=2):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (x, y, w, h, r, fill, stroke, sw, ' stroke-dasharray="10 8"' if dash else '')


def arrow(x1, y1, x2, y2, c=TEAL, sw=4, m='ah'):
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%d" marker-end="url(#%s)"/>' % (x1, y1, x2, y2, c, sw, m)


DEFS = ('<defs>'
        '<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
        '<marker id="ahr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
        '<marker id="ahn" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
        '</defs>') % (TEAL, RED, NAVY)


def svg(w, h, body, bg='#ffffff'):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s<rect width="100%%" height="100%%" fill="%s"/>%s</svg>' % (w, h, w, h, DEFS, bg, body)


def foot(w, h, anchor='end'):
    x = w - 36 if anchor == 'end' else w // 2
    return T(x, h - 28, '© renalcarematters.com', 20, 500, '#6b7280', anchor)


def kidney(cx, cy, s=1.0, fill='#e9a9a0', stroke='#b86f66'):
    return ('<g transform="translate(%d %d) scale(%s)"><path d="M-10 -120 C-110 -130 -150 -40 -140 20 C-130 100 -60 140 0 120 C40 108 30 60 10 40 C-10 20 -10 -20 10 -40 C30 -60 50 -110 -10 -120z" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M-14 -88 C-82 -90 -108 -30 -100 16 C-94 66 -50 96 -10 88" fill="none" stroke="#f7d9d4" stroke-width="10" stroke-linecap="round"/></g>') % (cx, cy, s, fill, stroke)


def drop(cx, cy, s=1.0, c='#7fb8d6'):
    return '<path transform="translate(%d %d) scale(%s)" d="M0 -40 C18 -14 30 2 30 18 A30 30 0 0 1 -30 18 C-30 2 -18 -14 0 -40z" fill="%s"/>' % (cx, cy, s, c)


files = {}

# ── 02: exit door and target (proximal tubule cell) ─────────────────────────
W, H = 1792, 1024
b = T(64, 92, 'The kidney is both the exit door and a target', 44, 700) + T(64, 136, 'How cisplatin builds up inside a proximal tubule cell', 26, 500, '#475569')
# blood side / urine side labels
b += box(64, 190, 300, 640, '#fbecec', '#e3b4b4', 20) + T(214, 236, 'BLOOD SIDE', 22, 700, RED, 'middle')
b += box(1428, 190, 300, 640, '#fdf6e3', '#e8d29a', 20) + T(1578, 236, 'URINE SIDE', 22, 700, AMBER, 'middle')
# the cell
b += box(400, 190, 990, 640, '#eef4fb', '#7d97b8', 40, sw=3) + T(895, 236, 'Proximal tubule cell', 26, 700, NAVY, 'middle')
# brush border on urine side
for i in range(16):
    y = 230 + i * 37
    b += '<rect x="1390" y="%d" width="26" height="12" rx="6" fill="#c9d6e8"/>' % y
# entry door
b += box(392, 360, 40, 120, TEAL, TEAL, 10) + T(470, 412, 'Entry door', 22, 700, TEAL) + T(470, 440, '(OCT2)', 20, 500, SLATE)
b += arrow(260, 420, 380, 420, TEAL, 6)
for (x, y) in [(150, 360), (210, 470), (130, 520), (250, 330), (180, 600)]:
    b += '<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (x, y, TEAL)
b += T(214, 700, 'Cisplatin in blood', 22, 600, SLATE, 'middle')
# exit pump (narrow)
b += box(1366, 380, 30, 80, '#8a6810', '#8a6810', 8) + T(1350, 352, 'Exit pump (MATE1)', 22, 700, '#8a6810', 'end') + T(1350, 500, 'slower', 20, 600, '#8a6810', 'end')
b += arrow(1400, 420, 1460, 420, '#8a6810', 4)
b += '<circle cx="1520" cy="420" r="11" fill="%s"/>' % TEAL
# accumulation cloud
for (x, y) in [(620, 400), (660, 450), (700, 380), (740, 470), (780, 410), (820, 360), (860, 450), (900, 400), (700, 520), (800, 520), (940, 480), (760, 330)]:
    b += '<circle cx="%d" cy="%d" r="11" fill="%s" opacity=".85"/>' % (x, y, TEAL)
b += T(780, 590, 'Drug builds up', 24, 700, NAVY, 'middle')
# mitochondria injured
for (x, y) in [(1080, 360), (1160, 470)]:
    b += '<ellipse cx="%d" cy="%d" rx="60" ry="30" fill="#f6d7c8" stroke="%s" stroke-width="3"/><path d="M%d %d q15 -18 30 0 q15 18 30 0" fill="none" stroke="%s" stroke-width="3"/>' % (x, y, RED, x - 40, y, RED)
    b += '<path d="M%d %d l12 -10 l-6 14 l14 -6" stroke="%s" stroke-width="4" fill="none"/>' % (x + 46, y - 46, RED)
b += T(1120, 560, 'Energy factories', 22, 700, RED, 'middle') + T(1120, 588, '(mitochondria) injured', 22, 600, RED, 'middle')
# magnesium leak
b += arrow(1180, 700, 1520, 700, RED, 5, 'ahr') + T(1350, 680, 'Magnesium, potassium, salt leak', 22, 700, RED, 'middle')
for i, x in enumerate([1500, 1560, 1620]):
    b += '<circle cx="%d" cy="760" r="18" fill="#fde7c2" stroke="%s" stroke-width="2"/>' % (x, AMBER) + T(x, 768, 'Mg', 16, 700, AMBER, 'middle')
# bottom flow
fy = 870
for i, (txt, bg, c) in enumerate([('Fast in, slow out', '#e6f2ef', TEAL), ('Injury and electrolyte wasting', '#fbe9e9', RED), ('Protection: fluids, magnesium, no NSAIDs', '#eaf5ee', GREEN)]):
    x = 64 + i * 560
    b += box(x, fy, 520, 64, bg, c, 32) + T(x + 260, fy + 41, txt, 23, 700, NAVY, 'middle')
    if i < 2:
        b += arrow(x + 524, fy + 32, x + 556, fy + 32, c, 4)
b += foot(W, H)
files['02-exit-door-target'] = (W, H, svg(W, H, b))

# ── 03: injury pattern map ──────────────────────────────────────────────────
W, H = 1792, 1024
b = T(64, 92, 'Where chemotherapy injures the nephron', 44, 700) + T(64, 136, 'Lesion pattern predicts the clinical picture', 26, 500, '#475569')
# simple nephron path
b += '<circle cx="300" cy="560" r="110" fill="#f4f7fb" stroke="#7d97b8" stroke-width="4"/>'
for (x, y, r) in [(270, 530, 34), (330, 526, 30), (340, 590, 32), (270, 596, 30)]:
    b += '<circle cx="%d" cy="%d" r="%d" fill="#f3d6d6" stroke="#c98b8b" stroke-width="2.5"/>' % (x, y, r)
P = 'M410 560 C560 560 600 470 720 470 C860 470 880 640 1020 640 C1160 640 1180 520 1320 520 L1480 520'
b += '<path d="%s" fill="none" stroke="#9fb3cf" stroke-width="44" stroke-linecap="round"/>' % P
b += '<path d="%s" fill="none" stroke="#eef4fb" stroke-width="30" stroke-linecap="round"/>' % P
for (x, y, a) in [(1050, 638, 20), (1090, 630, -30), (1130, 616, 60), (1190, 574, 15)]:
    b += '<g transform="translate(%d %d) rotate(%d)"><path d="M-12 0 L0 -10 L12 0 L0 10z" fill="%s"/></g>' % (x, y, a, AMBER)
for (x, y) in [(820, 700), (860, 735), (900, 705), (940, 740), (980, 712)]:
    b += '<circle cx="%d" cy="%d" r="9" fill="%s" opacity=".7"/>' % (x, y, PURPLE)
cards = [
    (64, 720, 400, 'Vessel lining (TMA)', ['Gemcitabine, mitomycin C', 'Hypertension, hematuria,', 'proteinuria, hemolysis'], RED, '#fbe9e9', (264, 720), (290, 670)),
    (520, 190, 440, 'Proximal tubule (ATI)', ['Cisplatin, ifosfamide,', 'melphalan, pemetrexed', 'Creatinine rise, Mg and K', 'wasting, Fanconi syndrome'], TEAL, '#e6f2ef', (720, 396), (720, 450)),
    (520, 780, 460, 'Interstitium', ['MTX, pemetrexed: nephritis', 'Pemetrexed: chronic fibrosis'], PURPLE, '#efeaf7', (900, 780), (900, 748)),
    (1100, 700, 420, 'Tubular lumen (crystals)', ['High-dose MTX', 'Nonoliguric AKI,', 'delayed drug clearance'], AMBER, '#fdf3df', (1240, 700), (1150, 650)),
]
for x, y, w, h, rows, c, bg, (x1, y1), (x2, y2) in cards:
    hh = 70 + 34 * len(rows)
    b += box(x, y, w, hh, bg, c, 18, sw=3) + T(x + 22, y + 44, h, 26, 700, c)
    b += lines(x + 22, y + 84, rows, 22, 500, SLATE, 1.5)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" stroke-dasharray="8 6"/>' % (x1, y1, x2, y2, c)
b += T(300, 428, 'Glomerulus', 22, 700, NAVY, 'middle') + T(1510, 528, 'to urine', 22, 600, SLATE)
b += box(1100, 190, 620, 150, '#f8fafc', '#cbd5e1', 18) + lines(1124, 236, ['Not covered by ADQI 34: checkpoint', 'inhibitors (interstitial nephritis) and', 'VEGF inhibitors (TMA, proteinuria)'], 22, 500, SLATE, 1.45)
b += T(64, 1000, 'Original schematic based on the pattern categories in ADQI 34 (Lentini et al., Kidney International 2026).', 18, 500, '#6b7280')
b += T(W - 36, 1000, '© renalcarematters.com', 18, 500, '#6b7280', 'end')
files['03-injury-pattern-map'] = (W, H, svg(W, H, b))

# ── 04: before a nephrotoxic cycle ──────────────────────────────────────────
W, H = 1792, 1024
b = T(64, 92, 'Before a nephrotoxic chemotherapy cycle', 44, 700) + T(64, 136, 'Five checks, every cycle', 26, 500, '#475569')
steps = [
    ('1', 'Kidney function method', ['Stable? Start with eGFR', 'Low muscle: add cystatin C', 'High stakes: measure GFR', 'Dose on mL/min (de-index)'], TEAL),
    ('2', 'Magnesium and potassium', ['Check and correct', 'before the dose', 'IV magnesium with', 'cisplatin hydration'], GREEN),
    ('3', 'Hydration plan', ['IV fluid before and after', 'Alkaline urine for HD-MTX', 'Respect heart failure', 'and dialysis fluid limits'], '#2563a8'),
    ('4', 'Nephrotoxin review', ['Stop NSAIDs', 'Review PPI, TMP-SMX,', 'penicillins, contrast,', 'aminoglycosides, herbals'], AMBER),
    ('5', 'Monitoring schedule', ['Creatinine, electrolytes,', 'urine every cycle', 'MTX levels for HD-MTX', 'BP, hemolysis for TMA drugs'], PURPLE),
]
for i, (n, h, rows, c) in enumerate(steps):
    x = 64 + i * 338
    b += box(x, 190, 316, 520, '#ffffff', c, 22, sw=3)
    b += '<circle cx="%d" cy="260" r="36" fill="%s"/>' % (x + 158, c) + T(x + 158, 273, n, 34, 800, '#ffffff', 'middle')
    b += lines(x + 158, 350, h.split(' ', 1) if len(h) > 16 else [h], 26, 700, NAVY, 1.25, 'middle')
    b += lines(x + 22, 470, rows, 19, 500, SLATE, 1.75)
    if i < 4:
        b += arrow(x + 318, 450, x + 336, 450, c, 4)
b += box(64, 760, 1664, 110, '#f1f5f9', '#94a3b8', 20) + T(896, 808, 'If creatinine rises: look for dehydration, obstruction, and other drugs first;', 24, 600, NAVY, 'middle') + T(896, 844, 'then delay, reduce, substitute, or rescue, as a shared oncology–nephrology decision.', 24, 600, NAVY, 'middle')
b += foot(W, H)
files['04-before-cisplatin-checklist'] = (W, H, svg(W, H, b))

# ── 05: GFR for dosing ──────────────────────────────────────────────────────
W, H = 1792, 1024
b = T(64, 92, 'Choosing a kidney-function number for anticancer dosing', 42, 700) + T(64, 136, 'Aligned with KDIGO 2024 and ADDIKD 2025', 26, 500, '#475569')
nodes = [
    (64, 200, 'Is kidney function stable?', ['Yes: continue to the right', 'No (evolving AKI): use kinetic', 'eGFR and clinical judgment'], RED, '#fbe9e9'),
    (480, 200, 'Start: CKD-EPI eGFR', ['From creatinine', '(not Cockcroft-Gault CrCl', 'for new assessments)'], TEAL, '#e6f2ef'),
    (896, 200, 'Creatinine unreliable?', ['Low muscle, amputation,', 'cachexia: add cystatin C', '(eGFRcr-cys)'], AMBER, '#fdf3df'),
    (1312, 200, 'High-stakes dose?', ['HD-MTX, high-dose cisplatin,', 'curative carboplatin, extremes', 'of body size: measure GFR'], PURPLE, '#efeaf7'),
]
for i, (x, y, h, rows, c, bg) in enumerate(nodes):
    b += box(x, y, 400, 300, bg, c, 22, sw=3) + T(x + 24, y + 52, h, 25, 700, c)
    b += lines(x + 24, y + 110, rows, 22, 500, SLATE, 1.55)
    if 0 < i < 3:
        b += arrow(x + 404, y + 150, x + 412, y + 150, c, 5)
b += arrow(464, 350, 476, 350, RED, 5)
# de-index panel
b += box(64, 560, 1664, 190, '#ffffff', NAVY, 22, sw=3)
b += T(96, 614, 'Then convert for dosing (de-index):', 28, 700, NAVY)
b += T(96, 668, 'Absolute GFR (mL/min) = eGFR (mL/min/1.73 m²) × BSA ÷ 1.73', 30, 700, TEAL)
b += T(96, 716, 'Carboplatin (Calvert): dose = target AUC × (GFR + 25); cap estimated GFR at 125 mL/min', 24, 600, SLATE)
b += box(64, 790, 1664, 120, '#f1f5f9', '#94a3b8', 20)
b += T(896, 838, 'Cystatin C-based eGFR can read falsely low with cancer, inflammation, and steroids;', 24, 600, NAVY, 'middle')
b += T(896, 874, 'when creatinine and cystatin C disagree and the decision matters, measure GFR.', 24, 600, NAVY, 'middle')
b += foot(W, H)
files['05-gfr-for-dosing'] = (W, H, svg(W, H, b))

# ── OG card 1200 x 630 ──────────────────────────────────────────────────────
W, H = 1200, 630
b = '<rect x="0" y="0" width="1200" height="630" fill="#f3f8f7"/>'
b += '<circle cx="960" cy="320" r="250" fill="#e6f2ef"/>' + kidney(930, 330, 1.35) + drop(1060, 200, 1.1, '#7fb8d6')
b += '<g transform="translate(1040 420)"><rect x="-40" y="-14" width="80" height="28" rx="14" fill="#ffffff" stroke="%s" stroke-width="3"/><rect x="-40" y="-14" width="40" height="28" rx="14" fill="%s"/></g>' % (TEAL, TEAL)
b += T(64, 90, 'ONCONEPHROLOGY', 24, 800, TEAL)
b += T(64, 190, 'Cancer Treatment', 66, 800, NAVY) + T(64, 270, 'and Your Kidneys', 66, 800, NAVY)
b += lines(64, 350, ['Kidney-safe chemotherapy: risks, prevention,', 'and dosing with CKD or dialysis'], 28, 500, SLATE, 1.4)
b += box(64, 450, 420, 56, '#ffffff', TEAL, 28) + T(274, 486, 'Patients &amp; Clinicians · EN TL CEB KAP', 20, 700, TEAL, 'middle')
b += T(64, 580, 'W Rivero, MD · renalcarematters.com', 22, 600, '#475569')
files['og'] = (W, H, svg(W, H, b))

# ── interim hero vignette 2048 x 2048 ───────────────────────────────────────
W, H = 2048, 2048
b = '<circle cx="1024" cy="1024" r="900" fill="#e8f3f1"/>'
b += '<circle cx="1024" cy="1024" r="900" fill="none" stroke="#cfe5e1" stroke-width="10"/>'
# infusion stand and bag
b += '<line x1="560" y1="420" x2="560" y2="1500" stroke="#94a3b8" stroke-width="16"/><line x1="460" y1="420" x2="660" y2="420" stroke="#94a3b8" stroke-width="14"/>'
b += '<rect x="500" y="440" width="120" height="190" rx="30" fill="#ffffff" stroke="%s" stroke-width="8"/><rect x="510" y="520" width="100" height="100" rx="24" fill="#bfe3df"/>' % TEAL
b += '<path d="M560 630 C560 820 700 900 860 980" fill="none" stroke="%s" stroke-width="6"/>' % TEAL
# chair and person (simple silhouette)
b += '<rect x="760" y="1100" width="620" height="120" rx="50" fill="#5b7fa6"/><rect x="1260" y="760" width="140" height="460" rx="60" fill="#5b7fa6"/>'
b += '<circle cx="1120" cy="760" r="120" fill="#d8a47f"/>'
b += '<path d="M940 1100 C940 930 1010 880 1120 880 C1240 880 1300 940 1300 1100z" fill="#f2c94c"/>'
b += '<path d="M940 1000 C900 1000 860 990 860 980" stroke="#d8a47f" stroke-width="44" stroke-linecap="round" fill="none"/>'
# kidney shield
b += '<circle cx="1440" cy="560" r="210" fill="#ffffff" stroke="%s" stroke-width="10"/>' % TEAL + kidney(1460, 570, 1.15)
b += '<path d="M1600 400 l40 40 l80 -100" stroke="%s" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % GREEN
b += drop(760, 1500, 2.2, '#7fb8d6')
files['vignette-hero'] = (W, H, svg(W, H, b))

for name, (w, h, s) in files.items():
    base = '%s-%s' % (SLUG, name)
    sp = os.path.join(SRC, base + '.svg')
    open(sp, 'w').write(s)
    png = os.path.join(IMG, base + '.png')
    subprocess.run(['rsvg-convert', '-w', str(w), '-h', str(h), sp, '-o', png], check=True)
    im = Image.open(png).convert('RGB')
    im.save(png, optimize=True)
    im.save(os.path.join(IMG, base + '.webp'), 'WEBP', quality=86, method=6)
    print('ok', base, w, h)
