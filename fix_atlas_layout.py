#!/usr/bin/env python3
"""
Clean up guides/nephrology-atlas.html:
  1. Remove floating index sidebar
  2. Remove section-hdr divs
  3. Remove orphaned card-body blocks + their extra </div>
  4. Merge consecutive thumb-grids within anatomy/conditions/procedures into one
  5. Rebuild embryology panel: keep timeline strip, wrap all 8 cards in one grid
  6. Clean up sidebar CSS and JS
"""
import re
from pathlib import Path

GUIDE = Path('guides/nephrology-atlas.html')
html = GUIDE.read_text(encoding='utf-8')

# ── 1. Remove sidebar block ──────────────────────────────────────────────────
html = re.sub(
    r'\n  <!-- ═══ FLOATING INDEX SIDEBAR ═══ -->.*?</aside>\n',
    '\n',
    html,
    flags=re.DOTALL
)

# ── 2. Remove section-hdr blocks ────────────────────────────────────────────
# section-hdr is at 6-space indent; only nested div is section-hdr-line at
# 8-space indent, so the first \n      </div> at 6 spaces is the outer close.
html = re.sub(
    r'\n      <div class="section-hdr">.*?\n      </div>',
    '',
    html,
    flags=re.DOTALL
)

# ── 3. Remove orphaned card-body + trailing extra </div> ─────────────────────
# Per card: thumb-card one-liner (8sp), card-body (10sp), old card close (8sp)
html = re.sub(
    r'(</div>)\n {10}<div class="card-body">.*?</div>\n {8}</div>',
    r'\1',
    html,
    flags=re.DOTALL
)

# ── 4. Merge consecutive thumb-grids in anatomy / conditions / procedures ────
# After steps 2-3, grids in these tabs are separated by:
#   \n      </div>\n\n      <div class="thumb-grid">
# We target only anatomy/conditions/procedures by restricting to patterns
# where the </div> is immediately preceded by a thumb-card's closing </div>
# (at 8-space indent).  The embryology timeline strip close is at 8-space
# indent too, BUT it's followed by the outer timeline div at 6 spaces then
# the blank + thumb-grid — same indentation chain, so we must exclude embryology.
#
# Strategy: process each non-embryology tab panel independently.
def merge_grids_in_panel(panel_html):
    """Remove consecutive thumb-grid separators within a single tab panel."""
    return re.sub(
        r'</div>\n\n      <div class="thumb-grid">',
        '',
        panel_html
    )

def process_panel(m):
    panel_id = m.group(1)
    content  = m.group(2)
    if panel_id != 'panel-embryology':
        content = merge_grids_in_panel(content)
    return f'<div class="tab-panel{" active" if panel_id == "panel-anatomy" else ""}" id="{panel_id}">{content}</div>'

# Match each tab-panel div and its content (non-greedy)
# panel-anatomy has class "active", others don't
html = re.sub(
    r'<div class="tab-panel(?: active)?" id="(panel-\w+)">(.*?)</div>(?=\s*\n\s*(?:<div class="tab-panel|</main>))',
    process_panel,
    html,
    flags=re.DOTALL
)

# ── 5. Rebuild embryology: keep timeline strip, wrap cards in one grid ───────
# Find the embryology panel and reconstruct it
def rebuild_embryology(m):
    content = m.group(1)
    # Extract the timeline strip block
    ts_match = re.search(
        r'(      <!-- Timeline strip -->\n      <div[^>]*>.*?      </div>\n)',
        content,
        re.DOTALL
    )
    timeline = ts_match.group(1) if ts_match else ''
    # Extract all thumb-cards
    cards = re.findall(
        r'        <div class="thumb-card accent-purple"[^>]*>.*?</div>',
        content,
        re.DOTALL
    )
    cards_html = '\n'.join('        ' + c.strip() for c in cards)
    new_content = f'\n{timeline}\n      <div class="thumb-grid">\n{cards_html}\n      </div>\n\n    '
    return f'<div class="tab-panel" id="panel-embryology">{new_content}</div>'

html = re.sub(
    r'<div class="tab-panel" id="panel-embryology">(.*?)</div>(?=\s*\n\s*</main>)',
    rebuild_embryology,
    html,
    flags=re.DOTALL
)

# ── 6. Simplify atlas-body CSS ───────────────────────────────────────────────
html = re.sub(
    r'(\.atlas-body \{[^}]*?)  display: flex;\n  gap: 28px;\n  align-items: flex-start;\n  position: relative;\n',
    r'\1',
    html,
    flags=re.DOTALL
)

# Remove sidebar CSS block
html = re.sub(
    r'/\* ─── FLOATING INDEX SIDEBAR ─── \*/.*?(?=/\* ─── CONTENT AREA ─── \*/)',
    '',
    html,
    flags=re.DOTALL
)

# Make content-area simple block
html = html.replace(
    '.content-area {\n  flex: 1;\n  min-width: 0;\n  padding-top: 24px;\n}',
    '.content-area {\n  padding-top: 24px;\n}'
)

# Remove mobile index-sidebar override
html = re.sub(r'  \.index-sidebar \{[^}]*\}\n', '', html)

# ── 7. Strip sidebar-only JS ─────────────────────────────────────────────────
html = re.sub(
    r'\n// ─── INDEX ACTIVE STATE ───\nfunction setActiveIndex.*?\n}',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'\n// ─── INDEX FILTER / SEARCH ───\nfunction filterIndex.*?\n}',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r"  document\.querySelectorAll\('\.index-panel'\)\.forEach\(p => p\.classList\.remove\('active'\)\);\n",
    '',
    html
)
html = re.sub(
    r"  document\.getElementById\('index-' \+ tab\)\.classList\.add\('active'\);\n",
    '',
    html
)
html = re.sub(
    r"  const firstItem = document\.querySelector\('#index-' \+ tab \+ ' \.index-item'\);.*?  }\n",
    '',
    html,
    flags=re.DOTALL
)

# ── Write and report ──────────────────────────────────────────────────────────
GUIDE.write_text(html, encoding='utf-8')

thumb_cards   = len(re.findall(r'class="thumb-card', html))
orphaned      = len(re.findall(r'class="card-body"', html))
sect_hdrs     = len(re.findall(r'class="section-hdr"', html))
sidebar       = 'id="indexSidebar"' in html

# Count thumb-grids per panel
panels = re.findall(r'id="(panel-\w+)"(.*?)</div>(?=\s*\n\s*(?:<div class="tab-panel|</main>))', html, re.DOTALL)
print(f'Thumb cards       : {thumb_cards}  (expected 48)')
print(f'Section headers   : {sect_hdrs}  (expected 0)')
print(f'Orphaned card-body: {orphaned}  (expected 0)')
print(f'Sidebar present   : {sidebar}  (expected False)')
for pid, pcontent in panels:
    grids = len(re.findall(r'class="thumb-grid"', pcontent))
    cards = len(re.findall(r'class="thumb-card', pcontent))
    print(f'  {pid}: {grids} grid(s), {cards} card(s)')
print(f'File size         : {len(html)//1024} KB')
