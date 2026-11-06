#!/usr/bin/env python3
"""Original code-native figures for al-amyloidosis-kidneys (SVG source -> PNG master -> WebP)."""
import os, subprocess, sys
from PIL import Image

REPO = sys.argv[1]
SRC = os.path.join(REPO, 'image-prompts', 'al-amyloidosis-kidneys-svg')
os.makedirs(SRC, exist_ok=True)
NAVY, TEAL, GREEN, AMBER, RED = '#0f1e2e', '#1a6b72', '#1f7a4d', '#b8860b', '#b23b3b'
FONT = "Inter, 'Inter Display', sans-serif"
FOOT = lambda w, h, anchor='end', x=None: '<text x="%d" y="%d" font-family="%s" font-size="20" fill="#6b7280" text-anchor="%s">© renalcarematters.com</text>' % (x if x is not None else w - 36, h - 28, FONT, anchor)

def T(x, y, s, size=28, w=600, fill=NAVY, anchor='start', style=''):
    return '<text x="%d" y="%d" font-family="%s" font-size="%d" font-weight="%d" fill="%s" text-anchor="%s" %s>%s</text>' % (x, y, FONT, size, w, fill, anchor, style, s)

def lines(x, y, rows, size=24, w=500, fill='#334155', lh=1.38, anchor='start'):
    return ''.join(T(x, y + i * size * lh, r, size, w, fill, anchor) for i, r in enumerate(rows))

def box(x, y, w, h, fill, stroke, r=22, dash=False, sw=2):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (x, y, w, h, r, fill, stroke, sw, ' stroke-dasharray="10 8"' if dash else '')

def arrow(x1, y1, x2, y2, c=TEAL, sw=4):
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%d" marker-end="url(#ah)"/>' % (x1, y1, x2, y2, c, sw)

DEFS = '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker></defs>' % TEAL

def svg(w, h, body, bg='#ffffff'):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s<rect width="100%%" height="100%%" fill="%s"/>%s</svg>' % (w, h, w, h, DEFS, bg, body)

# ── reusable glyphs ──
def plasma_cell(cx, cy, s=1.0):
    g = '<g transform="translate(%d %d) scale(%s)">' % (cx, cy, s)
    g += '<ellipse cx="0" cy="0" rx="70" ry="56" fill="#dfe8f3" stroke="#7d97b8" stroke-width="3"/><circle cx="-18" cy="-4" r="24" fill="#9fb3cf"/>'
    for i, (dx, dy, a) in enumerate([(96, -40, -20), (112, 6, 5), (92, 50, 25), (140, -18, -8), (146, 34, 14)]):
        g += '<g transform="translate(%d %d) rotate(%d)"><path d="M-14 -10 L0 0 L14 -10 M0 0 L0 16" stroke="%s" stroke-width="4" fill="none" stroke-linecap="round"/></g>' % (dx, dy, a, RED if i > 2 else '#c26b6b')
    return g + '</g>'

def glomerulus(cx, cy, s=1.0, deposits=True, macrophage=True):
    g = '<g transform="translate(%d %d) scale(%s)">' % (cx, cy, s)
    g += '<circle r="96" fill="#f4f7fb" stroke="#7d97b8" stroke-width="3"/>'
    for (x, y, r) in [(-30, -24, 30), (24, -30, 28), (34, 22, 30), (-22, 30, 28), (0, 0, 22)]:
        g += '<circle cx="%d" cy="%d" r="%d" fill="#f3d6d6" stroke="#c98b8b" stroke-width="2.5"/>' % (x, y, r)
    if deposits:
        for (x, y, a) in [(-46, -6, 30), (10, -52, -20), (52, -4, 60), (-4, 50, 10), (-40, 40, -40), (40, 46, 35), (-12, -14, 75)]:
            g += '<g transform="translate(%d %d) rotate(%d)"><path d="M-14 0 h28 M-12 6 h24 M-10 -6 h20" stroke="%s" stroke-width="3" stroke-linecap="round"/></g>' % (x, y, a, AMBER)
    if macrophage:
        g += '<path d="M78 70 q24 -18 40 4 q20 10 6 30 q-8 22 -34 14 q-24 4 -24 -18 q-8 -20 12 -30z" fill="#d7ecd9" stroke="%s" stroke-width="3"/><circle cx="96" cy="92" r="9" fill="%s"/>' % (GREEN, GREEN)
    return g + '</g>'

def kidney(cx, cy, s=1.0, fill='#e9a9a0', stroke='#b86f66'):
    return ('<g transform="translate(%d %d) scale(%s)"><path d="M-10 -120 C-110 -130 -150 -40 -140 20 C-130 100 -60 140 0 120 C40 108 30 60 10 40 C-10 20 -10 -20 10 -40 C30 -60 50 -110 -10 -120z" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M-14 -88 C-82 -90 -108 -30 -100 16 C-94 66 -50 96 -10 88" fill="none" stroke="#f7d9d4" stroke-width="10" stroke-linecap="round"/></g>') % (cx, cy, s, fill, stroke)

def gauge(cx, cy, label, frac, col):
    import math
    a = math.pi * (1 - frac)
    x, y = cx + 60 * math.cos(a), cy - 60 * math.sin(a)
    return ('<path d="M%d %d A70 70 0 0 1 %d %d" fill="none" stroke="#e2e8f0" stroke-width="14" stroke-linecap="round"/>' % (cx - 70, cy, cx + 70, cy) +
            '<line x1="%d" y1="%d" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="6" stroke-linecap="round"/><circle cx="%d" cy="%d" r="8" fill="%s"/>' % (cx, cy, x, y, col, cx, cy, col) +
            T(cx, cy + 40, label, 21, 600, '#334155', 'middle'))

files = {}

# 002 — three parts of recovery
W, H = 1792, 1024
b = T(64, 92, 'Three parts of recovery in AL amyloidosis', 46, 700) + T(64, 138, 'Each part moves on its own clock', 26, 500, '#475569')
cols = [(64, '1', 'Light-chain production', ['Plasma-cell clone in the marrow', 'Measured in blood: free light', 'chains, immunofixation'], 'Weeks to months', '#fbe9e9', RED),
        (640, '2', 'Deposits already in the kidney', ['Amyloid fibers in the filter wall', 'Cleared slowly: macrophages and', 'processes not fully understood'], 'Months to years', '#fdf3df', AMBER),
        (1216, '3', 'Kidney function', ['Holding protein in, filtering out', 'Measured by urine protein and', 'eGFR, read together'], 'Months to years; scar may remain', '#e6f2ef', TEAL)]
for x, n, h, rows, tempo, bg, c in cols:
    b += box(x, 180, 512, 600, '#ffffff', '#94a3b8', 24, dash=True)
    b += '<circle cx="%d" cy="232" r="26" fill="%s"/>' % (x + 48, c) + T(x + 48, 241, n, 26, 700, '#ffffff', 'middle') + T(x + 88, 242, h, 27, 700)
    b += lines(x + 40, 640, rows, 23, 500)
    b += box(x + 40, 712, 432, 48, bg, c, 24) + T(x + 256, 744, tempo, 22, 600, NAVY, 'middle')
b += plasma_cell(260, 430, 1.25)
b += glomerulus(896, 430, 1.35)
b += kidney(1360, 430, 0.95) + gauge(1560, 380, 'Protein held in', 0.45, AMBER) + gauge(1560, 540, 'Filtering out', 0.7, TEAL)
b += arrow(580, 470, 630, 470) + arrow(1156, 470, 1206, 470)
fy = 830
for i, (txt, bg, c) in enumerate([('Treatment stops new light chains', '#fbe9e9', RED), ('Deposits shrink slowly, if at all', '#fdf3df', AMBER), ('Function may recover, often partly', '#e6f2ef', GREEN)]):
    x = 64 + i * 576
    b += box(x, fy, 512, 84, bg, c, 18) + T(x + 256, fy + 52, txt, 25, 700, NAVY, 'middle')
    if i < 2: b += arrow(x + 520, fy + 42, x + 568, fy + 42)
b += T(64, 976, 'Schematic for teaching; not drawn from measured data.', 20, 500, '#6b7280') + FOOT(W, H)
files['02-three-parts'] = svg(W, H, b)

# 003 — diagnosis and typing
b = T(64, 92, 'Confirming AL amyloidosis: three separate answers', 46, 700) + T(64, 138, 'A monoclonal protein answers only the third question', 26, 500, '#475569')
qs = [('1', 'Is there amyloid in tissue?', ['Congo red stain', 'Apple-green birefringence', 'under polarized light'], ['Fat pad + bone marrow', 'in most people; organ', 'biopsy when needed'], '#eef3fa', '#7d97b8'),
      ('2', 'Which protein is it?', ['Typing: laser-capture mass', 'spectrometry (preferred) or', 'expert immunostaining'], ['Separates AL from AA,', 'ATTR, LECT2, fibrinogen,', 'and other forms'], '#fdf3df', AMBER),
      ('3', 'Is there a plasma-cell clone?', ['Serum + urine immunofixation', 'Serum free light chains', 'Bone-marrow examination'], ['Finds the source that', 'treatment will target'], '#e6f2ef', TEAL)]
for i, (n, q, test, note, bg, c) in enumerate(qs):
    x = 64 + i * 576
    b += box(x, 190, 512, 560, bg, c, 26)
    b += '<circle cx="%d" cy="250" r="30" fill="%s"/>' % (x + 60, c) + T(x + 60, 260, n, 30, 700, '#ffffff', 'middle') + T(x + 104, 262, q, 27, 700)
    b += T(x + 40, 340, 'Test', 22, 700, c if c != '#7d97b8' else '#4b6386') + lines(x + 40, 380, test, 25, 500, NAVY)
    b += '<line x1="%d" y1="520" x2="%d" y2="520" stroke="%s" stroke-width="2" stroke-dasharray="6 6"/>' % (x + 40, x + 472, c)
    b += T(x + 40, 566, 'Why it matters', 22, 700, c if c != '#7d97b8' else '#4b6386') + lines(x + 40, 606, note, 25, 500, NAVY)
b += box(400, 800, 992, 92, '#e8f5ec', GREEN, 20, sw=3) + T(896, 856, 'AL amyloidosis is confirmed only when all three agree', 28, 700, NAVY, 'middle')
for i in range(3):
    b += arrow(320 + i * 576, 754, 320 + i * 576 + (896 - (320 + i * 576)) * 0.25, 796)
b += T(64, 970, 'Bone scintigraphy is not used to diagnose AL cardiac amyloidosis when a monoclonal protein is present (ASH 2026).', 20, 500, '#6b7280') + FOOT(W, H)
files['03-diagnosis-typing'] = svg(W, H, b)

# 004 — follow-up domains
b = T(64, 92, 'Five things to follow, five different questions', 46, 700) + T(64, 138, 'Keep each one comparable over time and report them separately', 26, 500, '#475569')
doms = [('Blood', ['Free light chains', 'Immunofixation'], 'Is the clone still active?', RED, '#fbe9e9'),
        ('Urine', ['24-hour protein', 'or UPCR / UACR'], 'How leaky is the filter?', AMBER, '#fdf3df'),
        ('Filtration', ['eGFR, same equation', 'stable, adult'], 'How much filtering power?', TEAL, '#e6f2ef'),
        ('Heart', ['NT-proBNP, troponin', 'echocardiography'], 'How strained is the heart?', '#6f4bb8', '#efe9fa'),
        ('Daily life', ['Weight, blood pressure', 'swelling, energy'], 'How is treatment tolerated?', GREEN, '#e8f5ec')]
for i, (h, rows, q, c, bg) in enumerate(doms):
    x = 64 + i * 336
    b += box(x, 200, 312, 600, bg, c, 26, sw=2.5)
    b += '<circle cx="%d" cy="320" r="70" fill="#ffffff" stroke="%s" stroke-width="4"/>' % (x + 156, c)
    b += [plasma_cell(x + 130, 320, 0.55), glomerulus(x + 156, 320, 0.6, True, False), kidney(x + 160, 322, 0.42),
          '<path d="M%d 300 c-30 -40 -80 0 -40 40 l40 36 l40 -36 c40 -40 -10 -80 -40 -40z" fill="#d9c9f2" stroke="#6f4bb8" stroke-width="4"/>' % (x + 156),
          '<rect x="%d" y="286" width="90" height="70" rx="12" fill="#ffffff" stroke="%s" stroke-width="4"/><line x1="%d" y1="306" x2="%d" y2="306" stroke="%s" stroke-width="4"/><line x1="%d" y1="324" x2="%d" y2="324" stroke="%s" stroke-width="4"/><line x1="%d" y1="342" x2="%d" y2="342" stroke="%s" stroke-width="4"/>' % (x + 111, GREEN, x + 125, x + 187, GREEN, x + 125, x + 187, GREEN, x + 125, x + 170, GREEN)][i]
    b += T(x + 156, 450, h, 32, 700, NAVY, 'middle') + lines(x + 156, 500, rows, 23, 500, '#334155', anchor='middle')
    b += '<line x1="%d" y1="600" x2="%d" y2="600" stroke="%s" stroke-width="2" stroke-dasharray="6 6"/>' % (x + 30, x + 282, c)
    qa, qb = q.split(' ', 2)[:2], q.split(' ', 2)[2]
    b += T(x + 156, 648, 'Asks', 20, 700, c, 'middle') + lines(x + 156, 690, [' '.join(qa), qb], 24, 600, NAVY, anchor='middle')
b += box(64, 840, 1664, 80, '#f8fafc', '#cbd5e1', 18) + T(896, 890, 'A better blood result does not prove kidney recovery; a lower urine protein with a falling eGFR needs review.', 24, 600, NAVY, 'middle')
b += FOOT(W, H)
files['04-follow-up-domains'] = svg(W, H, b)

# 005 — discordant pathway (portrait)
W2, H2 = 1024, 1536
b = T(64, 96, 'When blood, urine, and eGFR disagree', 40, 700) + T(64, 140, 'Clinician assessment workflow (practice proposal)', 24, 500, '#475569')
steps = [('Confirm comparability', 'Same test, units, complete collection, same eGFR equation, steady state', TEAL, '#e6f2ef'),
         ('Exclude reversible causes', 'Over-diuresis, new RAAS or SGLT2 drugs, hypotension, NSAIDs, contrast, sepsis', AMBER, '#fdf3df'),
         ('Re-examine the clone', 'Rising dFLC or new immunofixation: hematology review', RED, '#fbe9e9'),
         ('Assess the heart', 'NT-proBNP and troponin trends with eGFR; echocardiography', '#6f4bb8', '#efe9fa'),
         ('Reconsider the kidney diagnosis', 'Drug toxicity, renal vein thrombosis, obstruction, second process', '#4b6386', '#eef3fa'),
         ('Report each domain separately', 'Hematologic, renal, cardiac status with dates in the letter', GREEN, '#e8f5ec')]
import textwrap
for i, (h, d, c, bg) in enumerate(steps):
    y = 190 + i * 210
    b += box(80, y, 864, 168, bg, c, 22, sw=2.5)
    b += '<circle cx="146" cy="%d" r="32" fill="%s"/>' % (y + 84, c) + T(146, y + 95, str(i + 1), 30, 700, '#ffffff', 'middle')
    b += T(204, y + 62, h, 30, 700) + lines(204, y + 104, textwrap.wrap(d, 52), 22, 500, '#334155')
    if i < 5: b += arrow(512, y + 172, 512, y + 204)
b += T(512, 1470, 'Falling urine protein with falling eGFR can mean nephron loss, not repair.', 22, 600, RED, 'middle') + FOOT(W2, H2, 'middle', 512)
files['05-discordant-pathway'] = svg(W2, H2, b)

# 006 — OG card
W3, H3 = 1200, 630
b = '<rect width="1200" height="630" fill="#e9f5f1"/><rect x="0" y="0" width="14" height="630" fill="%s"/>' % TEAL
b += T(70, 120, 'GLOMERULAR DISEASE · HEMATOLOGY', 22, 700, TEAL, style='letter-spacing="3"')
b += T(70, 210, 'AL Amyloidosis', 66, 800) + T(70, 290, 'and Your Kidneys', 66, 800, TEAL)
b += lines(70, 370, ['Why blood remission is only', 'part of recovery'], 32, 500, '#334155')
b += T(70, 560, 'renalcarematters.com', 26, 700, NAVY)
b += '<circle cx="930" cy="315" r="230" fill="#ffffff"/>' + glomerulus(930, 300, 1.5) + plasma_cell(820, 470, 0.5)
files['og'] = svg(W3, H3, b)

# 001 — interim wordless hero (original illustration; replace with the generated raster when ready)
HW = 2048
c = HW / 2; R = HW * 0.88 / 2
b = '<defs><radialGradient id="hg" cx="62%%" cy="62%%" r="70%%"><stop offset="0" stop-color="#f3faf8"/><stop offset="1" stop-color="#cfe7e3"/></radialGradient><clipPath id="hc"><circle cx="%d" cy="%d" r="%d"/></clipPath></defs>' % (c, c, R)
b += '<circle cx="%d" cy="%d" r="%d" fill="url(#hg)"/>' % (c, c, R)
b += '<g clip-path="url(#hc)">'
b += '<circle cx="1420" cy="1420" r="520" fill="#ffffff" opacity="0.55"/>'
b += kidney(1270, 1180, 3.4, '#eab3aa', '#b9776e')
b += glomerulus(1590, 860, 2.2, True, True)
b += '<g opacity="0.9">' + plasma_cell(820, 1500, 1.9) + '</g>'
b += '<rect x="1430" y="1430" width="300" height="380" rx="28" fill="#ffffff" stroke="#9fb3cf" stroke-width="8" transform="rotate(8 1580 1620)"/>'
for k in range(5):
    b += '<line x1="1480" y1="%d" x2="%d" y2="%d" stroke="#cbd5e1" stroke-width="14" stroke-linecap="round" transform="rotate(8 1580 1620)"/>' % (1520 + k * 60, 1680 - (40 if k % 2 else 0), 1520 + k * 60)
b += '</g>'
files['vignette-hero'] = svg(HW, HW, b)

for name, s in files.items():
    sp = os.path.join(SRC, 'al-amyloidosis-kidneys-%s.svg' % name)
    open(sp, 'w').write(s)
    png = os.path.join(REPO, 'images', 'al-amyloidosis-kidneys-%s.png' % name)
    subprocess.run(['rsvg-convert', sp, '-o', png], check=True)
    im = Image.open(png).convert('RGB')
    im.save(png[:-4] + '.webp', 'WEBP', quality=88, method=6)
    if name == 'og':
        th = im.resize((440, 231)).crop((0, 0, 440, 231))
    print(name, im.size)
# related-guide thumbnail (220x160 crop of the OG card)
og = Image.open(os.path.join(REPO, 'images', 'al-amyloidosis-kidneys-og.png')).convert('RGB')
og.crop((560, 60, 1200, 525)).resize((440, 320)).save(os.path.join(REPO, 'images', 'al-amyloidosis-kidneys-rg-thumb.webp'), 'WEBP', quality=85)
