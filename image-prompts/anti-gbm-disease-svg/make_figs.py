#!/usr/bin/env python3
"""Original code-native figures for anti-gbm-disease (SVG source -> PNG master -> WebP).
Usage: python3 make_figs.py <repo-root>  (interim figures; production prompts in image-prompts/anti-gbm-disease-image-plan.md)
Numbers drawn on figure 05 come from Floyd et al. (2023) JASN 34(3):505-514 (abstract, verified on PubMed)."""
import os, subprocess, sys, math
from PIL import Image

REPO = sys.argv[1]
SLUG = 'anti-gbm-disease'
SRC = os.path.join(REPO, 'image-prompts', SLUG + '-svg')
os.makedirs(SRC, exist_ok=True)
NAVY, TEAL, GREEN, AMBER, RED, PURPLE = '#0f1e2e', '#1a6b72', '#1f7a4d', '#9a6b00', '#b23b3b', '#5b3fa0'
FONT = "Inter, 'Inter Display', sans-serif"
MUTED = '#475569'

def FOOT(w, h):
    return '<text x="%d" y="%d" font-family="%s" font-size="20" fill="#6b7280" text-anchor="end">© renalcarematters.com</text>' % (w - 36, h - 28, FONT)

def T(x, y, s, size=28, w=600, fill=NAVY, anchor='start'):
    return '<text x="%d" y="%d" font-family="%s" font-size="%d" font-weight="%d" fill="%s" text-anchor="%s">%s</text>' % (x, y, FONT, size, w, fill, anchor, s)

def lines(x, y, rows, size=24, w=500, fill='#334155', lh=1.36, anchor='start'):
    return ''.join(T(x, y + i * size * lh, r, size, w, fill, anchor) for i, r in enumerate(rows))

def box(x, y, w, h, fill, stroke, r=22, dash=False, sw=2):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (x, y, w, h, r, fill, stroke, sw, ' stroke-dasharray="10 8"' if dash else '')

def arrow(x1, y1, x2, y2, c=TEAL, sw=4):
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%d" marker-end="url(#ah)"/>' % (x1, y1, x2, y2, c, sw)

DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0 0L10 5L0 10z" fill="%s"/></marker></defs>') % TEAL

def svg(w, h, body, bg='#ffffff'):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s<rect width="100%%" height="100%%" fill="%s"/>%s</svg>' % (w, h, w, h, DEFS, bg, body)

# ── glyphs ──
def kidney(cx, cy, s=1.0, fill='#e9a9a0', stroke='#b86f66'):
    return ('<g transform="translate(%d %d) scale(%s)"><path d="M-10 -120 C-110 -130 -150 -40 -140 20 C-130 100 -60 140 0 120 C40 108 30 60 10 40 C-10 20 -10 -20 10 -40 C30 -60 50 -110 -10 -120z" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M-14 -88 C-82 -90 -108 -30 -100 16 C-94 66 -50 96 -10 88" fill="none" stroke="#f7d9d4" stroke-width="10" stroke-linecap="round"/></g>') % (cx, cy, s, fill, stroke)

def lungs(cx, cy, s=1.0, fill='#f1c4c4', stroke='#b97b7b', bleed=False):
    g = '<g transform="translate(%d %d) scale(%s)">' % (cx, cy, s)
    g += '<path d="M0 -110 L0 -30 M0 -30 C-10 -20 -30 -14 -44 -6 M0 -30 C10 -20 30 -14 44 -6" stroke="#9fb3cf" stroke-width="10" fill="none" stroke-linecap="round"/>'
    g += '<path d="M-20 -60 C-70 -90 -130 -40 -130 40 C-130 110 -90 130 -40 120 C-20 116 -16 90 -18 60 Z" fill="%s" stroke="%s" stroke-width="4"/>' % (fill, stroke)
    g += '<path d="M20 -60 C70 -90 130 -40 130 40 C130 110 90 130 40 120 C20 116 16 90 18 60 Z" fill="%s" stroke="%s" stroke-width="4"/>' % (fill, stroke)
    if bleed:
        for (x, y, r) in [(-80, 30, 12), (-60, 70, 9), (-95, 75, 8), (75, 40, 11), (90, 80, 8), (60, 85, 7)]:
            g += '<circle cx="%d" cy="%d" r="%d" fill="%s" opacity="0.8"/>' % (x, y, r, RED)
    return g + '</g>'

def glomerulus(cx, cy, s=1.0, crescent=False, linear=True):
    g = '<g transform="translate(%d %d) scale(%s)">' % (cx, cy, s)
    g += '<circle r="100" fill="#f4f7fb" stroke="#7d97b8" stroke-width="3"/>'
    if crescent:
        g += '<path d="M-100 0 A100 100 0 0 1 60 -80 A86 86 0 0 0 -84 10 Z" fill="#d9c9f2" stroke="%s" stroke-width="3"/>' % PURPLE
    for (x, y, r) in [(-24, -20, 28), (26, -26, 26), (32, 24, 28), (-20, 32, 26), (2, 2, 20)]:
        g += '<circle cx="%d" cy="%d" r="%d" fill="#f3d6d6" stroke="%s" stroke-width="%s"/>' % (x, y, r, TEAL if linear else '#c98b8b', 5 if linear else 2.5)
    return g + '</g>'

def antibody(x, y, a=0, c=RED, s=1.0):
    return '<g transform="translate(%d %d) rotate(%d) scale(%s)"><path d="M-14 -12 L0 0 L14 -12 M0 0 L0 18" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/></g>' % (x, y, a, s, c)

def hexamer(cx, cy, r=38, open_=False):
    g = ''
    cols = ['#9fd3d6', '#c8b6ea', '#f3c9a4', '#9fd3d6', '#c8b6ea', '#f3c9a4']
    for i in range(6):
        ang = math.pi / 3 * i
        dx = (r + (16 if open_ and i in (0, 3) else 0)) * math.cos(ang)
        dy = (r + (16 if open_ and i in (0, 3) else 0)) * math.sin(ang)
        g += '<circle cx="%.0f" cy="%.0f" r="24" fill="%s" stroke="#475569" stroke-width="2"/>' % (cx + dx, cy + dy, cols[i])
    if open_:
        g += '<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (cx + r + 16, cy, RED)
        g += '<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (cx - r - 16, cy, RED)
    else:
        g += '<circle cx="%d" cy="%d" r="8" fill="#94a3b8"/>' % (cx, cy)
    return g

files = {}
W, H = 1792, 1024

# 02 — mechanism
b = T(64, 88, 'How anti-GBM disease injures the kidney and lung', 44, 700) + T(64, 132, 'One hidden target, two organs, one race against time', 26, 500, MUTED)
# panel 1 organs
b += box(64, 170, 380, 560, '#ffffff', '#94a3b8', 24, dash=True)
b += T(254, 214, 'Two filters share one mesh', 24, 700, NAVY, 'middle')
b += kidney(180, 360, 0.75) + lungs(340, 360, 0.62, bleed=True)
b += lines(254, 520, ['Kidney filters (glomeruli)', 'and lung air sacs (alveoli)', 'are lined by basement', 'membrane with the same', 'collagen IV α3 chain'], 21, 500, '#334155', anchor='middle')
# panel 2 hexamer
b += box(476, 170, 400, 560, '#eef6f7', TEAL, 24)
b += T(676, 214, 'The target is normally hidden', 24, 700, NAVY, 'middle')
b += hexamer(566, 330) + T(566, 412, 'Intact NC1 hexamer', 19, 600, MUTED, 'middle')
b += hexamer(786, 330, open_=True) + T(786, 412, 'Hexamer opens', 19, 600, MUTED, 'middle')
b += arrow(632, 330, 700, 330)
b += antibody(840, 296, -40) + antibody(732, 296, 40)
b += lines(676, 470, ['Cross-links (sulfilimine bonds)', 'normally bury the α3 epitopes', 'EA and EB. Once exposed, IgG', 'autoantibodies bind them;', 'smoking or infection may', 'help antibodies reach the lung'], 20, 500, '#334155', anchor='middle')
# panel 3 injury
b += box(908, 170, 400, 560, '#fbe9e9', RED, 24)
b += T(1108, 214, 'Inflammation breaks the filter', 24, 700, NAVY, 'middle')
b += glomerulus(1010, 340, 0.8, linear=True) + T(1010, 448, 'Linear IgG', 19, 600, TEAL, 'middle')
b += arrow(1092, 340, 1132, 340, RED)
b += glomerulus(1222, 340, 0.8, crescent=True, linear=False) + T(1222, 448, 'Crescent', 19, 600, PURPLE, 'middle')
b += lines(1108, 500, ['Complement and white cells', 'rupture the capillary wall;', 'blood and fibrin leak into', 'Bowman space; cells pile up', 'as a crescent that scars', 'within days to weeks'], 20, 500, '#334155', anchor='middle')
# panel 4 treatment
b += box(1340, 170, 388, 560, '#e8f5ec', GREEN, 24)
b += T(1534, 214, 'Treatment has three jobs', 24, 700, NAVY, 'middle')
jobs = [('1', 'Remove antibodies', 'plasma exchange'), ('2', 'Stop new antibodies', 'cyclophosphamide, steroids'), ('3', 'Calm the injury', 'steroids; support organs')]
for i, (n, h, s) in enumerate(jobs):
    y = 270 + i * 140
    b += '<circle cx="1392" cy="%d" r="24" fill="%s"/>' % (y, GREEN) + T(1392, y + 9, n, 24, 700, '#ffffff', 'middle')
    b += T(1430, y - 4, h, 23, 700) + T(1430, y + 26, s, 20, 500, MUTED)
b += lines(1534, 690, ['Started before the crescents', 'scar, kidney function can be saved'], 19, 600, GREEN, anchor='middle')
# bottom flow
fy = 780
for i, (txt, bg, c) in enumerate([('Hidden α3 target exposed', '#eef6f7', TEAL), ('Antibodies attack kidney ± lung', '#fbe9e9', RED), ('Crescents form within days', '#efe9fa', PURPLE), ('Early treatment saves filters', '#e8f5ec', GREEN)]):
    x = 64 + i * 420
    b += box(x, fy, 384, 84, bg, c, 18) + T(x + 192, fy + 52, txt, 23, 700, NAVY, 'middle')
    if i < 3:
        b += arrow(x + 388, fy + 42, x + 414, fy + 42)
b += T(64, 950, 'Schematic for teaching. NC1, noncollagenous domain 1; EA and EB, the two main antibody-binding regions of α3(IV)NC1.', 20, 500, '#6b7280') + FOOT(W, H)
files['02-mechanism'] = svg(W, H, b)

# 03 — variant map
b = T(64, 88, 'Variant forms of anti-GBM disease', 44, 700) + T(64, 132, 'Four groups proposed by Kuang et al. (2026); each changes testing, treatment, or follow-up', 26, 500, MUTED)
groups = [
    ('1', 'Overlapping autoimmune disease', TEAL, '#eef6f7', ['With ANCA vasculitis ("double-positive"):', 'about one in three patients', 'With membranous nephropathy', 'With IgA nephropathy'], 'Plan long-term follow-up; maintenance', 'therapy when ANCA is also positive'),
    ('2', 'Immunologically distinct', PURPLE, '#efe9fa', ['Alport syndrome after transplant:', 'alloantibodies to the α5 chain', 'Seronegative or atypical: blood test', 'negative, linear IgG on biopsy'], 'Standard blood tests can miss both;', 'the biopsy and genetics guide care'),
    ('3', 'Different clinical pattern', AMBER, '#fdf3df', ['Relapse in the native kidney (rare;', 'often lung bleeding, often smokers)', 'Older adults: more ANCA, worse survival', 'Normal kidney function, lung-first'], 'Smoking cessation; balance treatment', 'intensity against infection risk'),
    ('4', 'Medication- or trigger-associated', RED, '#fbe9e9', ['Alemtuzumab', 'Immune checkpoint inhibitors', 'Reported after infection epidemics', 'and SARS-CoV-2 vaccination'], 'Check anti-GBM promptly if kidney', 'function falls on these drugs')]
for i, (n, h, c, bg, rows, m1, m2) in enumerate(groups):
    x = 64 + (i % 2) * 840
    y = 170 + (i // 2) * 380
    b += box(x, y, 800, 350, bg, c, 26, sw=2.5)
    b += '<circle cx="%d" cy="%d" r="28" fill="%s"/>' % (x + 52, y + 50, c) + T(x + 52, y + 60, n, 28, 700, '#ffffff', 'middle') + T(x + 96, y + 61, h, 29, 700)
    b += lines(x + 40, y + 120, rows, 23, 500, '#334155')
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" stroke-dasharray="6 6"/>' % (x + 40, y + 252, x + 760, y + 252, c)
    b += lines(x + 40, y + 292, [m1, m2], 22, 700, NAVY)
b += T(64, 950, 'ANCA, antineutrophil cytoplasmic antibody. Associations with drugs and vaccines are reported cases; cause has not been proven.', 20, 500, '#6b7280') + FOOT(W, H)
files['03-variant-map'] = svg(W, H, b)

# 04 — algorithm (taller)
W4, H4 = 1600, 1800
b = T(64, 90, 'Suspected anti-GBM disease: the first 24 hours', 44, 700) + T(64, 134, 'Do not let the biopsy schedule delay treatment', 26, 500, MUTED)
steps = [
    (RED, '#fbe9e9', 'Suspect it', ['Rapidly rising creatinine with blood and protein in the urine,', 'with or without coughing blood or new lung shadows']),
    (TEAL, '#eef6f7', 'Same-day tests', ['Anti-GBM antibody AND ANCA (MPO, PR3) together; urinalysis', 'and sediment, creatinine, potassium, CBC; chest X-ray or CT']),
    (AMBER, '#fdf3df', 'High suspicion? Start now', ['Glucocorticoids; plasma exchange if it can start, even before', 'results return (KDIGO Practice Point 11.2.1)']),
    (TEAL, '#eef6f7', 'Kidney biopsy, early', ['Linear IgG confirms; crescent count and normal glomeruli', 'guide prognosis. Add 300-600 mL fresh plasma within 3 days of biopsy']),
    (GREEN, '#e8f5ec', 'Full course', ['Daily plasma exchange until antibody negative (about 14 days);', 'oral cyclophosphamide 2-3 months; steroids about 6 months']),
    (PURPLE, '#efe9fa', 'Decide on the edge cases', ['Dialysis-dependent + 100% crescents or &gt;50% sclerosis + no lung', 'bleeding: KDIGO exception; consider a short trial or supportive care']),
    (NAVY, '#e8edf5', 'Follow-up', ['Double-positive: maintenance as for ANCA vasculitis. No smoking.', 'Transplant only after antibodies are negative for 6 months or more'])]
y = 180
for i, (c, bg, h, rows) in enumerate(steps):
    b += box(64, y, 1472, 176, bg, c, 22, sw=2.5)
    b += '<circle cx="124" cy="%d" r="34" fill="%s"/>' % (y + 88, c) + T(124, y + 100, str(i + 1), 32, 700, '#ffffff', 'middle')
    b += T(190, y + 62, h, 32, 700) + lines(190, y + 110, rows, 25, 500, '#334155')
    if i < len(steps) - 1:
        b += arrow(800, y + 178, 800, y + 210, c)
    y += 214
b += T(64, 1700, 'Summary of KDIGO 2021 Chapter 11 and McAdoo &amp; Pusey (2025). Individualize for each patient.', 21, 500, '#6b7280') + FOOT(W4, H4)
files['04-first-24-hours'] = svg(W4, H4, b)

# 05 — Floyd four-group renal survival
W5, H5 = 1600, 900
b = T(64, 88, 'Kidney survival at 3 years depends on two things at diagnosis', 40, 700) + T(64, 130, 'Need for dialysis and the share of normal glomeruli on biopsy (174 patients)', 25, 500, MUTED)
data = [('No dialysis', '≥10% normal', 96.4, GREEN), ('No dialysis', '&lt;10% normal', 74.0, TEAL), ('Dialysis', '≥10% normal', 42.3, AMBER), ('Dialysis', '&lt;10% normal', 14.1, RED)]
L, B0, T0 = 200, 720, 200
b += ''.join('<line x1="%d" x2="1500" y1="%d" y2="%d" stroke="#e2e8f0" stroke-width="2"/>' % (L, B0 - g * (B0 - T0) / 100, B0 - g * (B0 - T0) / 100) + T(L - 16, B0 - g * (B0 - T0) / 100 + 8, '%d%%' % g, 22, 500, MUTED, 'end') for g in range(0, 101, 25))
for i, (a, bb, v, c) in enumerate(data):
    cx = L + 160 + i * 320
    h = v / 100 * (B0 - T0)
    b += '<rect x="%d" y="%.0f" width="180" height="%.0f" rx="8" fill="%s"/>' % (cx - 90, B0 - h, h, c)
    b += T(cx, B0 - h - 16, ('%.1f%%' % v), 30, 700, NAVY, 'middle')
    b += T(cx, B0 + 40, a, 24, 700, NAVY, 'middle') + T(cx, B0 + 72, bb, 22, 500, MUTED, 'middle')
b += '<line x1="%d" x2="1500" y1="%d" y2="%d" stroke="#334155" stroke-width="3"/>' % (L, B0, B0)
b += T(64, 860, 'Floyd et al., JASN 2023; retrospective international cohort. Group estimates, not individual predictions.', 20, 500, '#6b7280') + FOOT(W5, H5)
files['05-kidney-survival'] = svg(W5, H5, b)

# OG card
W3, H3 = 1200, 630
b = '<rect width="1200" height="630" fill="#eef6f7"/>'
b += T(70, 190, 'Anti-GBM Disease', 66, 800) + T(70, 268, '(Goodpasture Disease)', 44, 700, TEAL)
b += lines(70, 350, ['A kidney and lung emergency:', 'why treatment must start within hours'], 30, 500, '#334155')
b += T(70, 560, 'renalcarematters.com', 26, 700, NAVY)
b += '<circle cx="935" cy="315" r="225" fill="#ffffff"/>' + glomerulus(930, 240, 1.0, crescent=True, linear=False) + kidney(850, 430, 0.6) + lungs(1030, 430, 0.5, bleed=True)
files['og'] = svg(W3, H3, b)

# 01 — interim wordless hero (original; replace with generated raster when ready)
HW = 2048
c = HW / 2
R = HW * 0.88 / 2
b = '<defs><radialGradient id="hg" cx="40%%" cy="40%%" r="75%%"><stop offset="0" stop-color="#f4faf9"/><stop offset="1" stop-color="#cfe6e4"/></radialGradient><clipPath id="hc"><circle cx="%d" cy="%d" r="%d"/></clipPath></defs>' % (c, c, R)
b += '<circle cx="%d" cy="%d" r="%d" fill="url(#hg)"/><g clip-path="url(#hc)">' % (c, c, R)
b += '<circle cx="1380" cy="1180" r="560" fill="#ffffff" opacity="0.55"/>'
b += lungs(1400, 820, 2.6, '#f3cccc', '#bf8484', bleed=False)
b += kidney(1180, 1460, 2.5, '#eab3aa', '#b9776e')
b += glomerulus(1540, 1400, 1.9, crescent=False, linear=True)
for (x, y, a) in [(1420, 1220, 20), (1660, 1250, -30), (1730, 1430, 60), (1420, 1590, -60), (1600, 1600, 10)]:
    b += antibody(x, y, a, '#c26b6b', 2.2)
b += '</g>'
files['vignette-hero'] = svg(HW, HW, b)

for name, s in files.items():
    sp = os.path.join(SRC, '%s-%s.svg' % (SLUG, name))
    open(sp, 'w').write(s)
    png = os.path.join(REPO, 'images', '%s-%s.png' % (SLUG, name))
    subprocess.run(['rsvg-convert', sp, '-o', png], check=True)
    im = Image.open(png).convert('RGB')
    im.save(png[:-4] + '.webp', 'WEBP', quality=88, method=6)
    print(name, im.size)
og = Image.open(os.path.join(REPO, 'images', SLUG + '-og.png')).convert('RGB')
og.crop((620, 60, 1200, 482)).resize((440, 320)).save(os.path.join(REPO, 'images', SLUG + '-rg-thumb.webp'), 'WEBP', quality=85)
print('thumb ok')
