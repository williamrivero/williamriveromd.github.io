#!/usr/bin/env python3
"""
Transform guides/nephrology-atlas.html cards to thumbnail-grid + lightbox layout.
Run from repo root: python3 patch_atlas_lightbox.py
"""
import re, json, html as H
from pathlib import Path

SRC = Path('guides/nephrology-atlas.html')
text = SRC.read_text('utf-8')

# ── helpers ────────────────────────────────────────────────────────────────

def striptags(s):
    return re.sub(r'<[^>]+>', '', s).strip()

def card_end(text, pos):
    """Return index after the closing </div> matching <div at pos."""
    depth = 0
    i = pos
    while i < len(text):
        if text[i:i+4] == '<div':
            depth += 1; i += 4
        elif text[i:i+6] == '</div>':
            depth -= 1
            if depth == 0: return i + 6
            i += 6
        else:
            i += 1
    return len(text)

def parse_card(blob):
    d = {}
    m = re.search(r'\bid="(\w+)"', blob)
    d['id'] = m.group(1) if m else ''
    m = re.search(r'<span class="card-num">(.*?)</span>', blob, re.DOTALL)
    d['num'] = striptags(m.group(1)) if m else ''
    m = re.search(r'<span class="card-title">(.*?)</span>', blob, re.DOTALL)
    d['title'] = H.unescape(striptags(m.group(1))) if m else ''
    m = re.search(r'card-header (\w+)-accent', blob)
    d['accent'] = m.group(1) if m else 'teal'
    m = re.search(r'<source srcset="([^"]+)" type="image/webp">', blob)
    d['webp'] = m.group(1) if m else ''
    m = re.search(r'<img src="([^"]+)" alt="([^"]*)"', blob)
    d['png'], d['alt'] = (m.group(1), H.unescape(m.group(2))) if m else ('', '')
    m = re.search(r'<p class="card-desc">(.*?)</p>', blob, re.DOTALL)
    d['desc'] = H.unescape(striptags(m.group(1))) if m else ''
    raw_steps = re.findall(r'<li><span class="step-num">\d+</span>(.*?)</li>', blob, re.DOTALL)
    d['steps'] = [H.unescape(striptags(s)) for s in raw_steps]
    raw_tags = re.findall(r'<span class="ctag (ct-\w+)">(.*?)</span>', blob, re.DOTALL)
    d['tags'] = [{'cls': c, 'text': H.unescape(striptags(t))} for c, t in raw_tags]
    return d

def thumb_html(d):
    steps_json = H.escape(json.dumps(d['steps'], ensure_ascii=False))
    tags_json  = H.escape(json.dumps(d['tags'],  ensure_ascii=False))
    return (
        f'<div class="thumb-card accent-{d["accent"]}" id="{d["id"]}"'
        f' data-num="{H.escape(d["num"])}"'
        f' data-title="{H.escape(d["title"])}"'
        f' data-webp="{d["webp"]}"'
        f' data-png="{d["png"]}"'
        f' data-alt="{H.escape(d["alt"])}"'
        f' data-desc="{H.escape(d["desc"])}"'
        f' data-steps="{steps_json}"'
        f' data-tags="{tags_json}"'
        f' onclick="openLightbox(this)">'
        f'<div class="thumb-img-wrap">'
        f'<picture><source srcset="{d["webp"]}" type="image/webp">'
        f'<img src="{d["png"]}" alt="{H.escape(d["alt"])}" loading="lazy"></picture>'
        f'<div class="thumb-overlay"><span class="thumb-zoom-icon">⊕</span></div>'
        f'</div>'
        f'<div class="thumb-info">'
        f'<span class="thumb-num">{H.escape(d["num"])}</span>'
        f'<span class="thumb-title">{H.escape(d["title"])}</span>'
        f'</div></div>'
    )

# ── 1. Replace each illus-card / wide-card with thumb-card ─────────────────

def replace_cards(text):
    out = []
    i = 0
    while i < len(text):
        # look for start of an illus-card or wide-card
        m_illus = re.search(r'<div class="illus-card"', text[i:])
        m_wide  = re.search(r'<div class="wide-card"',  text[i:])
        if m_illus and (not m_wide or m_illus.start() <= m_wide.start()):
            start = i + m_illus.start()
        elif m_wide:
            start = i + m_wide.start()
        else:
            out.append(text[i:])
            break

        out.append(text[i:start])
        end = card_end(text, start)
        blob = text[start:end]
        d = parse_card(blob)
        out.append(thumb_html(d))
        i = end
    return ''.join(out)

text = replace_cards(text)

# ── 2. Replace cards-grid wrappers with thumb-grid ────────────────────────

text = re.sub(r'<div class="cards-grid[^"]*">', '<div class="thumb-grid">', text)

# ── 3. Inject new CSS before </style> ─────────────────────────────────────

NEW_CSS = """
/* ─── THUMBNAIL GRID ─── */
.thumb-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
  gap: 14px;
  margin-bottom: 28px;
}
.thumb-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.18s, box-shadow 0.18s;
  display: flex;
  flex-direction: column;
}
.thumb-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 28px rgba(11,26,46,0.14);
}
.thumb-card:hover .thumb-overlay { opacity: 1; }
.thumb-img-wrap {
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
  background: #edf0f6;
  flex-shrink: 0;
}
.thumb-img-wrap picture,
.thumb-img-wrap img {
  width: 100%; height: 100%;
  object-fit: cover; display: block;
}
.thumb-overlay {
  position: absolute; inset: 0;
  background: rgba(11,26,46,0.42);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: opacity 0.18s;
}
.thumb-zoom-icon {
  color: #fff; font-size: 2rem; line-height: 1;
  font-family: 'DM Mono', monospace;
}
.thumb-info {
  padding: 9px 11px 11px;
  border-top: 1px solid var(--border);
  flex: 1;
  display: flex; flex-direction: column; gap: 3px;
}
.thumb-num {
  font-family: 'DM Mono', monospace;
  font-size: 8.5px; color: var(--muted); letter-spacing: 0.5px;
}
.thumb-title {
  font-size: 0.77rem; font-weight: 600;
  color: var(--navy); line-height: 1.3;
}
/* accent stripe */
.thumb-card.accent-teal    .thumb-img-wrap::before,
.thumb-card.accent-amber   .thumb-img-wrap::before,
.thumb-card.accent-green   .thumb-img-wrap::before,
.thumb-card.accent-red     .thumb-img-wrap::before,
.thumb-card.accent-navy    .thumb-img-wrap::before,
.thumb-card.accent-purple  .thumb-img-wrap::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px; z-index: 1;
}
.thumb-card.accent-teal   .thumb-img-wrap::before { background: var(--teal); }
.thumb-card.accent-amber  .thumb-img-wrap::before { background: var(--amber); }
.thumb-card.accent-green  .thumb-img-wrap::before { background: var(--green); }
.thumb-card.accent-red    .thumb-img-wrap::before { background: var(--red); }
.thumb-card.accent-navy   .thumb-img-wrap::before { background: var(--navy3); }
.thumb-card.accent-purple .thumb-img-wrap::before { background: #6b3fa0; }

/* ─── LIGHTBOX ─── */
#lightbox {
  position: fixed; inset: 0;
  background: rgba(5,10,20,0.93);
  z-index: 9999;
  display: none; align-items: center; justify-content: center;
  padding: 16px;
}
#lightbox.open { display: flex; }
.lb-wrap {
  background: var(--surface);
  border-radius: 14px;
  max-width: 980px; width: 100%;
  max-height: 92vh; overflow-y: auto;
  position: relative;
  box-shadow: 0 24px 80px rgba(0,0,0,0.55);
  display: flex; flex-direction: column;
}
.lb-img-panel {
  background: #0b1a2e;
  border-radius: 14px 14px 0 0;
  overflow: hidden; position: relative;
  flex-shrink: 0;
}
.lb-img-panel picture, .lb-img-panel img {
  width: 100%; max-height: 52vh;
  object-fit: contain; display: block;
}
.lb-attribution {
  position: absolute; bottom: 6px; right: 10px;
  font-family: 'DM Mono', monospace; font-size: 8px;
  color: rgba(255,255,255,0.3);
}
.lb-nav {
  position: absolute; top: 50%; transform: translateY(-50%);
  background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2);
  color: #fff; font-size: 1.5rem;
  width: 40px; height: 40px; border-radius: 50%;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: background 0.15s; z-index: 2;
}
.lb-nav:hover { background: rgba(255,255,255,0.28); }
.lb-prev { left: 10px; }
.lb-next { right: 10px; }
.lb-info-panel { padding: 18px 22px 22px; }
.lb-toprow {
  display: flex; align-items: flex-start;
  justify-content: space-between; gap: 12px; margin-bottom: 12px;
}
.lb-title-block { flex: 1; }
.lb-num {
  font-family: 'DM Mono', monospace; font-size: 9px;
  color: var(--muted); display: block; margin-bottom: 4px; letter-spacing: 0.5px;
}
#lb-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.35rem; font-weight: 700;
  color: var(--navy); line-height: 1.2;
}
.lb-close {
  background: var(--bg); border: 1px solid var(--border);
  border-radius: 50%; width: 34px; height: 34px;
  font-size: 1.1rem; cursor: pointer; color: var(--text);
  display: flex; align-items: center; justify-content: center;
  transition: background 0.15s; flex-shrink: 0;
}
.lb-close:hover { background: #dde3ec; }
#lb-desc {
  font-size: 0.86rem; color: var(--muted);
  line-height: 1.65; margin-bottom: 14px;
}
#lb-steps {
  list-style: none; padding: 0; margin: 0 0 14px;
}
#lb-steps li {
  display: flex; gap: 10px; align-items: flex-start;
  font-size: 0.83rem; color: var(--text);
  padding: 5px 0; border-bottom: 1px solid #f0f2f6; line-height: 1.45;
}
#lb-steps li:last-child { border-bottom: none; }
#lb-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }
.lb-counter {
  font-family: 'DM Mono', monospace; font-size: 9px;
  color: var(--muted); text-align: right; margin-top: 8px;
}
@media (max-width: 600px) {
  .thumb-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
  .lb-wrap { border-radius: 10px; }
  .lb-img-panel img { max-height: 40vh; }
  .lb-nav { width: 32px; height: 32px; font-size: 1.1rem; }
}
"""

text = text.replace('</style>', NEW_CSS + '\n</style>', 1)

# ── 4. Inject lightbox HTML before </body> ────────────────────────────────

LIGHTBOX_HTML = """
<!-- ═══ LIGHTBOX ═══ -->
<div id="lightbox" onclick="lbBgClick(event)">
  <div class="lb-wrap" onclick="event.stopPropagation()">
    <div class="lb-img-panel">
      <picture id="lb-picture">
        <source id="lb-source" srcset="" type="image/webp">
        <img id="lb-img" src="" alt="">
      </picture>
      <button class="lb-nav lb-prev" onclick="lightboxNav(-1)">&#8249;</button>
      <button class="lb-nav lb-next" onclick="lightboxNav(1)">&#8250;</button>
      <div class="lb-attribution">© renalcarematters.com</div>
    </div>
    <div class="lb-info-panel">
      <div class="lb-toprow">
        <div class="lb-title-block">
          <span class="lb-num" id="lb-num"></span>
          <div id="lb-title"></div>
        </div>
        <button class="lb-close" onclick="closeLightbox()" title="Close (Esc)">&#x2715;</button>
      </div>
      <div id="lb-desc"></div>
      <ol id="lb-steps"></ol>
      <div id="lb-tags"></div>
      <div class="lb-counter" id="lb-counter"></div>
    </div>
  </div>
</div>
"""

text = text.replace('</body>', LIGHTBOX_HTML + '\n</body>', 1)

# ── 5. Replace JS block with updated version ──────────────────────────────

OLD_JS_START = '<script>'
OLD_JS_END   = '</script>\n</body>'

NEW_JS = """<script>
// ─── TAB SWITCHING ───
function switchTab(tab, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.index-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + tab).classList.add('active');
  document.getElementById('index-' + tab).classList.add('active');
  btn.classList.add('active');
  btn.dataset.tab = tab;
  const firstItem = document.querySelector('#index-' + tab + ' .index-item');
  if (firstItem) {
    document.querySelectorAll('#index-' + tab + ' .index-item').forEach(i => i.classList.remove('active'));
    firstItem.classList.add('active');
  }
}
// stamp data-tab on all tab buttons on load
document.querySelectorAll('.tab-btn').forEach(btn => {
  const m = btn.getAttribute('onclick').match(/switchTab\\('(\\w+)'/);
  if (m) btn.dataset.tab = m[1];
});

// ─── INDEX ACTIVE STATE ───
function setActiveIndex(el) {
  const panel = el.closest('.index-panel');
  if (panel) panel.querySelectorAll('.index-item').forEach(i => i.classList.remove('active'));
  el.classList.add('active');
}

// ─── INDEX FILTER / SEARCH ───
function filterIndex(input, panelId) {
  const query = input.value.toLowerCase();
  const panel = document.getElementById(panelId);
  panel.querySelectorAll('.index-item').forEach(item => {
    const text = item.querySelector('.index-item-text').textContent.toLowerCase();
    item.style.display = text.includes(query) ? '' : 'none';
  });
  panel.querySelectorAll('.index-group-label').forEach(label => {
    let next = label.nextElementSibling;
    let anyVisible = false;
    while (next && !next.classList.contains('index-group-label')) {
      if (next.style.display !== 'none') anyVisible = true;
      next = next.nextElementSibling;
    }
    label.style.display = anyVisible ? '' : 'none';
  });
}

// ─── EMBRYOLOGY TIMELINE HIGHLIGHT ───
function highlightStage(chip, targetId) {
  document.querySelectorAll('.embryo-stage-chip').forEach(c => c.classList.remove('active'));
  chip.classList.add('active');
  const target = document.getElementById(targetId);
  if (target) {
    target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    target.style.outline = '2px solid var(--teal)';
    setTimeout(() => target.style.outline = '', 2000);
  }
  const indexItem = document.querySelector('#index-embryology a[href="#' + targetId + '"]');
  if (indexItem) {
    document.querySelectorAll('#index-embryology .index-item').forEach(i => i.classList.remove('active'));
    indexItem.classList.add('active');
  }
}

// ─── SCROLL SPY ───
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    const activeBtn = document.querySelector('.tab-btn.active');
    if (!activeBtn) return;
    const tabName = activeBtn.dataset.tab;
    if (!tabName) return;
    const link = document.querySelector('#index-' + tabName + ' a[href="#' + id + '"]');
    if (link) {
      document.querySelectorAll('#index-' + tabName + ' .index-item').forEach(i => i.classList.remove('active'));
      link.classList.add('active');
    }
  });
}, { threshold: 0.3, rootMargin: '-10% 0px -60% 0px' });
document.querySelectorAll('[id]').forEach(el => {
  if (/^[acpe]\\d+/.test(el.id)) observer.observe(el);
});

// ─── LIGHTBOX ───
let lbTabCards = [];
let lbCurrentIdx = 0;

function getTabCards() {
  const activeBtn = document.querySelector('.tab-btn.active');
  const tab = activeBtn ? activeBtn.dataset.tab : 'anatomy';
  const panel = document.getElementById('panel-' + tab);
  return panel ? Array.from(panel.querySelectorAll('.thumb-card')) : [];
}

function openLightbox(el) {
  lbTabCards = getTabCards();
  lbCurrentIdx = lbTabCards.indexOf(el);
  populate(el);
  document.getElementById('lightbox').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('open');
  document.body.style.overflow = '';
}

function lbBgClick(e) {
  if (e.target === document.getElementById('lightbox')) closeLightbox();
}

function lightboxNav(dir) {
  if (!lbTabCards.length) return;
  lbCurrentIdx = (lbCurrentIdx + dir + lbTabCards.length) % lbTabCards.length;
  populate(lbTabCards[lbCurrentIdx]);
}

function populate(el) {
  const d = el.dataset;
  const img = document.getElementById('lb-img');
  const src = document.getElementById('lb-source');
  img.src = d.png; img.alt = d.alt || '';
  src.srcset = d.webp;
  document.getElementById('lb-num').textContent = d.num;
  document.getElementById('lb-title').textContent = d.title;
  document.getElementById('lb-desc').textContent = d.desc || '';

  const stepsEl = document.getElementById('lb-steps');
  stepsEl.innerHTML = '';
  if (d.steps && d.steps !== '[]') {
    try {
      JSON.parse(d.steps).forEach((s, i) => {
        const li = document.createElement('li');
        const numSpan = document.createElement('span');
        numSpan.className = 'step-num';
        numSpan.textContent = i + 1;
        li.appendChild(numSpan);
        li.appendChild(document.createTextNode(s));
        stepsEl.appendChild(li);
      });
    } catch(e) {}
  }

  const tagsEl = document.getElementById('lb-tags');
  tagsEl.innerHTML = '';
  if (d.tags && d.tags !== '[]') {
    try {
      JSON.parse(d.tags).forEach(t => {
        const span = document.createElement('span');
        span.className = 'ctag ' + t.cls;
        span.textContent = t.text;
        tagsEl.appendChild(span);
      });
    } catch(e) {}
  }

  document.getElementById('lb-counter').textContent =
    (lbCurrentIdx + 1) + ' / ' + lbTabCards.length;
}

document.addEventListener('keydown', e => {
  const lb = document.getElementById('lightbox');
  if (!lb.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') lightboxNav(1);
  else if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   lightboxNav(-1);
});
</script>"""

# Find and replace the last <script>...</script> block before </body>
last_script = text.rfind('<script>')
last_script_end = text.rfind('</script>')
if last_script != -1 and last_script_end != -1:
    text = text[:last_script] + NEW_JS + text[last_script_end + 9:]

# ── 6. Update header stat pills to match actual counts ────────────────────
# Anatomy:10, Conditions:14, Procedures:18, Embryology:8
text = re.sub(r'(<div class="stat-pill">.*?<div class="stat-num">)\d+(</div><div class="stat-label">Anatomy)',
              r'\g<1>10\2', text, flags=re.DOTALL)
text = re.sub(r'(<div class="stat-pill">.*?<div class="stat-num">)\d+(</div><div class="stat-label">Conditions)',
              r'\g<1>14\2', text, flags=re.DOTALL)
text = re.sub(r'(<div class="stat-pill">.*?<div class="stat-num">)\d+(</div><div class="stat-label">Procedures)',
              r'\g<1>18\2', text, flags=re.DOTALL)

# ── 7. Update tab counts ──────────────────────────────────────────────────
text = re.sub(r'(Anatomy\s*<span class="tab-count">)\d+', r'\g<1>10', text)
text = re.sub(r'(Medical Conditions\s*<span class="tab-count">)\d+', r'\g<1>14', text)  # won't match multi-line
text = re.sub(r'(Procedures\s*<span class="tab-count">)\d+', r'\g<1>18', text)
text = re.sub(r'(Embryology\s*<span class="tab-count">)\d+', r'\g<1>8', text)

# ── write ──────────────────────────────────────────────────────────────────
SRC.write_text(text, encoding='utf-8')

# verify
n_thumb = text.count('class="thumb-card ')
n_lb    = text.count('id="lightbox"')
n_old   = text.count('class="illus-card"') + text.count('class="wide-card"')
print(f"Thumbnail cards generated : {n_thumb}")
print(f"Lightbox injected         : {n_lb}")
print(f"Old card divs remaining   : {n_old}")
print(f"File size                 : {len(text)//1024} KB")
