#!/usr/bin/env python3
"""
patch_nut_tools.py — Insert SGA / MIS / SNAQ nutrition-screening calculators
into the four target guides.

Safe to re-run: each insertion point is checked first.
"""
import sys, re

# ─── Shared CSS ──────────────────────────────────────────────────────────────
NT_CSS = """/* ── Nutrition Screening Tools (nt-) ─────────────────────────────── */
.nt-section{margin:40px 0;padding:0;}
.nt-section-tag{display:inline-block;background:var(--teal,#1a6b72);color:#fff;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 10px;border-radius:6px;margin-bottom:10px;}
.nt-section h2{font-size:clamp(1.25rem,3vw,1.6rem);color:var(--text,#1e2a38);margin:0 0 6px;}
.nt-section .nt-sub{color:var(--text-muted,#6b7a8d);font-size:14px;margin:0 0 20px;}
.nt-demo-row{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;background:var(--bg,#f9fafb);border:1px solid var(--border,#e2e6eb);border-radius:10px;padding:16px 20px;margin-bottom:18px;}
.nt-demo-row label{font-size:13px;font-weight:600;color:var(--text,#1e2a38);display:flex;flex-direction:column;gap:4px;}
.nt-demo-row input,.nt-demo-row select{border:1px solid var(--border,#e2e6eb);border-radius:6px;padding:6px 10px;font-size:13px;background:#fff;color:var(--text,#1e2a38);}
.nt-demo-today{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:var(--text,#1e2a38);cursor:pointer;padding-bottom:2px;}
html[data-theme="dark"] .nt-demo-row{background:#1a2535;border-color:#2a3548;}
html[data-theme="dark"] .nt-demo-row input,html[data-theme="dark"] .nt-demo-row select{background:#141c2a;border-color:#2a3548;color:#e8eaf0;}
html[data-theme="dark"] .nt-demo-row label,html[data-theme="dark"] .nt-demo-today{color:#e8eaf0;}
.nt-tabs{display:flex;gap:0;border-bottom:2px solid var(--border,#e2e6eb);margin-bottom:24px;}
.nt-tab{padding:8px 20px;font-size:14px;font-weight:600;color:var(--text-muted,#6b7a8d);background:transparent;border:none;border-bottom:2px solid transparent;margin-bottom:-2px;cursor:pointer;transition:color .15s,border-color .15s;}
.nt-tab:hover{color:var(--teal,#1a6b72);}
.nt-tab.nt-active{color:var(--teal,#1a6b72);border-bottom-color:var(--teal,#1a6b72);}
html[data-theme="dark"] .nt-tabs{border-color:#2a3548;}
html[data-theme="dark"] .nt-tab{color:#8090a0;}
html[data-theme="dark"] .nt-tab.nt-active{color:#4db8c0;border-bottom-color:#4db8c0;}
.nt-panel{display:none;}.nt-panel.nt-show{display:block;}
.nt-card{background:var(--bg,#f9fafb);border:1px solid var(--border,#e2e6eb);border-radius:12px;padding:20px 24px;margin-bottom:20px;}
html[data-theme="dark"] .nt-card{background:#1a2535;border-color:#2a3548;}
.nt-q{margin-bottom:18px;}
.nt-q-label{font-size:14px;font-weight:600;color:var(--text,#1e2a38);margin-bottom:8px;display:block;}
html[data-theme="dark"] .nt-q-label{color:#e8eaf0;}
.nt-q-hint{font-size:12px;color:var(--text-muted,#6b7a8d);margin-bottom:8px;display:block;}
.nt-radio-row{display:flex;gap:10px;flex-wrap:wrap;}
.nt-radio-row label{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--text,#1e2a38);cursor:pointer;}
html[data-theme="dark"] .nt-radio-row label{color:#dde3eb;}
.nt-select{width:100%;max-width:320px;border:1px solid var(--border,#e2e6eb);border-radius:6px;padding:7px 10px;font-size:13px;background:#fff;color:var(--text,#1e2a38);}
html[data-theme="dark"] .nt-select{background:#141c2a;border-color:#2a3548;color:#e8eaf0;}
.nt-subgroup{background:rgba(26,107,114,.04);border-left:3px solid var(--teal,#1a6b72);border-radius:0 8px 8px 0;padding:14px 18px;margin-bottom:16px;}
html[data-theme="dark"] .nt-subgroup{background:rgba(77,184,192,.07);}
.nt-subgroup-title{font-size:12px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--teal,#1a6b72);margin-bottom:12px;}
.nt-result-box{display:none;border-radius:10px;padding:18px 22px;margin-top:16px;border:1px solid transparent;}
.nt-result-box.nt-show{display:block;}
.nt-result-box.nt-normal{background:var(--green-soft,#e6f4ea);border-color:#b2dfdb;}
.nt-result-box.nt-moderate{background:var(--amber-soft,#fff8e1);border-color:#ffe082;}
.nt-result-box.nt-severe{background:var(--red-soft,#fdecea);border-color:#f5c6cb;}
html[data-theme="dark"] .nt-result-box.nt-normal{background:#1a2e24;border-color:#2d5a48;}
html[data-theme="dark"] .nt-result-box.nt-moderate{background:#2a2410;border-color:#5a4a00;}
html[data-theme="dark"] .nt-result-box.nt-severe{background:#2e1a1a;border-color:#6b2020;}
.nt-result-score{font-size:2rem;font-weight:800;color:var(--teal,#1a6b72);margin-bottom:4px;}
html[data-theme="dark"] .nt-result-score{color:#4db8c0;}
.nt-result-label{font-size:1rem;font-weight:700;color:var(--text,#1e2a38);margin-bottom:6px;}
html[data-theme="dark"] .nt-result-label{color:#e8eaf0;}
.nt-result-desc{font-size:13px;color:var(--text-muted,#6b7a8d);line-height:1.6;}
html[data-theme="dark"] .nt-result-desc{color:#b0bcc8;}
.nt-btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px;}
.nt-calc-btn{background:var(--teal,#1a6b72);color:#fff;border:none;border-radius:8px;padding:10px 22px;font-size:14px;font-weight:600;cursor:pointer;transition:opacity .15s;}
.nt-calc-btn:hover{opacity:.85;}
.nt-reset-btn{background:transparent;color:var(--text-muted,#6b7a8d);border:1px solid var(--border,#e2e6eb);border-radius:8px;padding:10px 18px;font-size:14px;font-weight:600;cursor:pointer;transition:background .15s;}
.nt-reset-btn:hover{background:var(--bg,#f9fafb);}
html[data-theme="dark"] .nt-reset-btn{border-color:#2a3548;color:#8090a0;}
html[data-theme="dark"] .nt-reset-btn:hover{background:#1a2535;}
.nt-print-btn{background:transparent;color:var(--teal,#1a6b72);border:1px solid var(--teal,#1a6b72);border-radius:8px;padding:10px 18px;font-size:14px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:background .15s;}
.nt-print-btn:hover{background:rgba(26,107,114,.08);}
html[data-theme="dark"] .nt-print-btn{color:#4db8c0;border-color:#4db8c0;}
.nt-sga-global{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px;}
.nt-sga-pill{padding:8px 18px;border-radius:20px;border:2px solid var(--border,#e2e6eb);font-size:14px;font-weight:600;cursor:pointer;transition:all .15s;color:var(--text,#1e2a38);background:#fff;}
.nt-sga-pill:hover{border-color:var(--teal,#1a6b72);color:var(--teal,#1a6b72);}
.nt-sga-pill.nt-selected{border-color:var(--teal,#1a6b72);background:var(--teal,#1a6b72);color:#fff;}
html[data-theme="dark"] .nt-sga-pill{background:#141c2a;border-color:#2a3548;color:#dde3eb;}
html[data-theme="dark"] .nt-sga-pill.nt-selected{background:var(--teal,#1a6b72);color:#fff;}
.nt-ref{font-size:11px;color:var(--text-muted,#6b7a8d);margin-top:14px;line-height:1.5;}
html[data-theme="dark"] .nt-ref{color:#8090a0;}
"""

# ─── HTML section ────────────────────────────────────────────────────────────
NT_HTML = """
<!-- ============================================================
     NUTRITION SCREENING TOOLS  (SGA / MIS / SNAQ)
     ============================================================ -->
<section class="section" id="nut-tools">
  <div class="nt-section">
    <span class="nt-section-tag">Nutrition Screening</span>
    <h2>Nutrition Assessment Tools</h2>
    <p class="nt-sub">Validated tools for identifying malnutrition risk in CKD and dialysis patients: SNAQ (quick 3-question screen), MIS (10-item scored assessment), and SGA (clinician-administered global rating).</p>

    <!-- Demographics -->
    <div class="nt-demo-row" id="nt-demo">
      <label>Patient Name
        <input type="text" id="nt-name" placeholder="Optional" style="width:160px;">
      </label>
      <label>Age
        <input type="number" id="nt-age" placeholder="yrs" style="width:70px;" min="1" max="120">
      </label>
      <label>Sex
        <select id="nt-sex">
          <option value="">--</option>
          <option value="M">Male</option>
          <option value="F">Female</option>
        </select>
      </label>
      <label>Date
        <input type="date" id="nt-date" style="width:150px;">
      </label>
      <label class="nt-demo-today">
        <input type="checkbox" id="nt-today" onchange="ntSetToday(this)"> Today
      </label>
    </div>

    <!-- Tab bar -->
    <div class="nt-tabs" role="tablist">
      <button class="nt-tab nt-active" onclick="ntTab('snaq')" id="nt-tab-snaq" role="tab" aria-selected="true" aria-controls="nt-panel-snaq">SNAQ</button>
      <button class="nt-tab" onclick="ntTab('mis')" id="nt-tab-mis" role="tab" aria-selected="false" aria-controls="nt-panel-mis">MIS</button>
      <button class="nt-tab" onclick="ntTab('sga')" id="nt-tab-sga" role="tab" aria-selected="false" aria-controls="nt-panel-sga">SGA</button>
    </div>

    <!-- ── SNAQ panel ─────────────────────────────────── -->
    <div class="nt-panel nt-show" id="nt-panel-snaq" role="tabpanel" aria-labelledby="nt-tab-snaq">
      <div class="nt-card">
        <div class="nt-q">
          <span class="nt-q-label">Q1 — Did you unintentionally lose more than 4 kg in the past 6 months?</span>
          <div class="nt-radio-row">
            <label><input type="radio" name="snaq1" value="3" onchange="ntSnaqUpdate()"> Yes (+3)</label>
            <label><input type="radio" name="snaq1" value="0" onchange="ntSnaqUpdate()"> No (0)</label>
          </div>
        </div>
        <div class="nt-q">
          <span class="nt-q-label">Q2 — Did you unintentionally lose more than 2 kg in the past month?</span>
          <div class="nt-radio-row">
            <label><input type="radio" name="snaq2" value="2" onchange="ntSnaqUpdate()"> Yes (+2)</label>
            <label><input type="radio" name="snaq2" value="0" onchange="ntSnaqUpdate()"> No (0)</label>
          </div>
        </div>
        <div class="nt-q">
          <span class="nt-q-label">Q3 — Did you eat less than usual over the past month due to decreased appetite?</span>
          <div class="nt-radio-row">
            <label><input type="radio" name="snaq3" value="1" onchange="ntSnaqUpdate()"> Yes (+1)</label>
            <label><input type="radio" name="snaq3" value="0" onchange="ntSnaqUpdate()"> No (0)</label>
          </div>
        </div>
        <div class="nt-result-box" id="snaq-result">
          <div class="nt-result-score" id="snaq-score">—</div>
          <div class="nt-result-label" id="snaq-label">—</div>
          <div class="nt-result-desc" id="snaq-desc"></div>
        </div>
        <p class="nt-ref">Reference: Kruizenga HM et al. <em>Clin Nutr</em> 2005;24(1):75–82. SNAQ validated for hospitalized patients; adapted for CKD screening.</p>
      </div>
      <div class="nt-btn-row">
        <button class="nt-print-btn" onclick="ntPrint('snaq')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          Print / Save PDF
        </button>
        <button class="nt-reset-btn" onclick="ntReset()">Reset all</button>
      </div>
    </div>

    <!-- ── MIS panel ──────────────────────────────────── -->
    <div class="nt-panel" id="nt-panel-mis" role="tabpanel" aria-labelledby="nt-tab-mis">
      <div class="nt-card">
        <div class="nt-subgroup">
          <div class="nt-subgroup-title">Clinical / Dietary (Items 1–5)</div>

          <div class="nt-q">
            <span class="nt-q-label">1. Dry weight change (past 3–6 months)</span>
            <select class="nt-select" id="mis1" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">No change or gain (0)</option>
              <option value="1">Loss &lt;0.5 kg (1)</option>
              <option value="2">Loss 0.5–1 kg (2)</option>
              <option value="3">Loss &gt;1 kg (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">2. Dietary intake</span>
            <select class="nt-select" id="mis2" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">Good / normal (0)</option>
              <option value="1">Suboptimal solids (1)</option>
              <option value="2">Full liquid diet (2)</option>
              <option value="3">Very poor / starvation (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">3. GI symptoms (past 2 weeks)</span>
            <select class="nt-select" id="mis3" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">None / few (0)</option>
              <option value="1">Occasional nausea or vomiting (1)</option>
              <option value="2">Frequent nausea / vomiting (2)</option>
              <option value="3">Diarrhea, severe vomiting, or anorexia (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">4. Functional capacity</span>
            <select class="nt-select" id="mis4" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">Normal (0)</option>
              <option value="1">Occasional fatigue / difficulty (1)</option>
              <option value="2">Difficulty with ADLs (2)</option>
              <option value="3">Bedbound (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">5. Comorbidities / dialysis duration</span>
            <select class="nt-select" id="mis5" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">On dialysis &lt;1 yr, no comorbidities (0)</option>
              <option value="1">Mild comorbidity (1)</option>
              <option value="2">Moderate comorbidity (2)</option>
              <option value="3">Severe comorbidity or dialysis ≥4 yr (3)</option>
            </select>
          </div>
        </div>

        <div class="nt-subgroup">
          <div class="nt-subgroup-title">Physical Exam &amp; Labs (Items 6–10)</div>

          <div class="nt-q">
            <span class="nt-q-label">6. Subcutaneous fat loss (periorbital, triceps, biceps, chest)</span>
            <select class="nt-select" id="mis6" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">Normal (0)</option>
              <option value="1">Mild loss (1)</option>
              <option value="2">Moderate loss (2)</option>
              <option value="3">Severe loss (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">7. Muscle wasting signs (temples, clavicle, shoulder, ribs, quads, knee)</span>
            <select class="nt-select" id="mis7" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">Normal (0)</option>
              <option value="1">Mild (1)</option>
              <option value="2">Moderate (2)</option>
              <option value="3">Severe (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">8. BMI (kg/m²)</span>
            <select class="nt-select" id="mis8" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">≥20 (0)</option>
              <option value="1">18–19.9 (1)</option>
              <option value="2">16–17.9 (2)</option>
              <option value="3">&lt;16 (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">9. Serum albumin (g/dL)</span>
            <select class="nt-select" id="mis9" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">≥4.0 (0)</option>
              <option value="1">3.5–3.9 (1)</option>
              <option value="2">3.0–3.4 (2)</option>
              <option value="3">&lt;3.0 (3)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">10. TIBC (mg/dL)</span>
            <select class="nt-select" id="mis10" onchange="ntMisUpdate()">
              <option value="">— select —</option>
              <option value="0">≥250 (0)</option>
              <option value="1">200–249 (1)</option>
              <option value="2">150–199 (2)</option>
              <option value="3">&lt;150 (3)</option>
            </select>
          </div>
        </div>

        <div class="nt-result-box" id="mis-result">
          <div class="nt-result-score" id="mis-score">—</div>
          <div class="nt-result-label" id="mis-label">—</div>
          <div class="nt-result-desc" id="mis-desc"></div>
        </div>
        <p class="nt-ref">Reference: Kalantar-Zadeh K et al. <em>Am J Kidney Dis</em> 2001;38(6):1251–1263. MIS validated for maintenance hemodialysis patients. Score range 0–30.</p>
      </div>
      <div class="nt-btn-row">
        <button class="nt-print-btn" onclick="ntPrint('mis')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          Print / Save PDF
        </button>
        <button class="nt-reset-btn" onclick="ntReset()">Reset all</button>
      </div>
    </div>

    <!-- ── SGA panel ──────────────────────────────────── -->
    <div class="nt-panel" id="nt-panel-sga" role="tabpanel" aria-labelledby="nt-tab-sga">
      <div class="nt-card">
        <div class="nt-subgroup">
          <div class="nt-subgroup-title">A — Weight History</div>
          <div class="nt-q">
            <span class="nt-q-label">% Weight loss in past 6 months</span>
            <select class="nt-select" id="sga-a1" onchange="ntSgaUpdate()">
              <option value="">— select —</option>
              <option value="a">&lt;5% loss (minimal)</option>
              <option value="b">5–10% loss (significant)</option>
              <option value="c">&gt;10% loss (severe)</option>
            </select>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">2-week trend</span>
            <select class="nt-select" id="sga-a2" onchange="ntSgaUpdate()">
              <option value="">— select —</option>
              <option value="gain">Gaining</option>
              <option value="stable">Stable</option>
              <option value="loss">Losing</option>
            </select>
          </div>
        </div>

        <div class="nt-subgroup">
          <div class="nt-subgroup-title">B — Dietary Intake</div>
          <div class="nt-q">
            <span class="nt-q-label">Current dietary intake (compared to normal)</span>
            <select class="nt-select" id="sga-b" onchange="ntSgaUpdate()">
              <option value="">— select —</option>
              <option value="a">No change / adequate</option>
              <option value="b">Suboptimal solids</option>
              <option value="b2">Full liquid diet</option>
              <option value="c">Hypocaloric liquid / starvation</option>
            </select>
          </div>
        </div>

        <div class="nt-subgroup">
          <div class="nt-subgroup-title">C — GI Symptoms (≥2 weeks)</div>
          <div class="nt-q">
            <span class="nt-q-label">Persistent GI symptoms</span>
            <select class="nt-select" id="sga-c" onchange="ntSgaUpdate()">
              <option value="">— select —</option>
              <option value="a">None</option>
              <option value="b">One symptom (nausea, vomiting, diarrhea, or anorexia)</option>
              <option value="c">Multiple or daily symptoms</option>
            </select>
          </div>
        </div>

        <div class="nt-subgroup">
          <div class="nt-subgroup-title">D — Functional Capacity</div>
          <div class="nt-q">
            <span class="nt-q-label">Current functional status</span>
            <select class="nt-select" id="sga-d" onchange="ntSgaUpdate()">
              <option value="">— select —</option>
              <option value="a">Normal / full</option>
              <option value="b">Mild impairment (working suboptimally)</option>
              <option value="c">Severe impairment (bed- or chair-bound)</option>
            </select>
          </div>
        </div>

        <div class="nt-subgroup">
          <div class="nt-subgroup-title">E — Physical Signs</div>
          <div class="nt-q">
            <span class="nt-q-label">Subcutaneous fat loss</span>
            <div class="nt-radio-row">
              <label><input type="radio" name="sga-e1" value="0" onchange="ntSgaUpdate()"> None (0)</label>
              <label><input type="radio" name="sga-e1" value="1" onchange="ntSgaUpdate()"> Mild (1+)</label>
              <label><input type="radio" name="sga-e1" value="2" onchange="ntSgaUpdate()"> Moderate (2+)</label>
              <label><input type="radio" name="sga-e1" value="3" onchange="ntSgaUpdate()"> Severe (3+)</label>
            </div>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">Muscle wasting</span>
            <div class="nt-radio-row">
              <label><input type="radio" name="sga-e2" value="0" onchange="ntSgaUpdate()"> None (0)</label>
              <label><input type="radio" name="sga-e2" value="1" onchange="ntSgaUpdate()"> Mild (1+)</label>
              <label><input type="radio" name="sga-e2" value="2" onchange="ntSgaUpdate()"> Moderate (2+)</label>
              <label><input type="radio" name="sga-e2" value="3" onchange="ntSgaUpdate()"> Severe (3+)</label>
            </div>
          </div>
          <div class="nt-q">
            <span class="nt-q-label">Edema / ascites</span>
            <div class="nt-radio-row">
              <label><input type="radio" name="sga-e3" value="0" onchange="ntSgaUpdate()"> None (0)</label>
              <label><input type="radio" name="sga-e3" value="1" onchange="ntSgaUpdate()"> Mild (1+)</label>
              <label><input type="radio" name="sga-e3" value="2" onchange="ntSgaUpdate()"> Moderate (2+)</label>
              <label><input type="radio" name="sga-e3" value="3" onchange="ntSgaUpdate()"> Severe (3+)</label>
            </div>
          </div>
        </div>

        <!-- Global Rating -->
        <div class="nt-q">
          <span class="nt-q-label" style="font-size:15px;">Global Rating — Clinician Assessment</span>
          <span class="nt-q-hint">Select the overall nutritional status rating based on all components above.</span>
          <div class="nt-sga-global" id="sga-global-btns">
            <button class="nt-sga-pill" onclick="ntSgaGlobal('A',this)">A — Well Nourished</button>
            <button class="nt-sga-pill" onclick="ntSgaGlobal('B',this)">B — Mild/Moderate Malnutrition</button>
            <button class="nt-sga-pill" onclick="ntSgaGlobal('C',this)">C — Severe Malnutrition</button>
          </div>
        </div>

        <div class="nt-result-box" id="sga-result">
          <div class="nt-result-score" id="sga-score">—</div>
          <div class="nt-result-label" id="sga-label">—</div>
          <div class="nt-result-desc" id="sga-desc"></div>
        </div>
        <p class="nt-ref">References: Detsky AS et al. <em>JPEN J Parenter Enteral Nutr</em> 1987;11(1):8–13. Steiber A et al. <em>J Ren Nutr</em> 2004;14(1):1–7 (CKD validation).</p>
      </div>
      <div class="nt-btn-row">
        <button class="nt-print-btn" onclick="ntPrint('sga')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          Print / Save PDF
        </button>
        <button class="nt-reset-btn" onclick="ntReset()">Reset all</button>
      </div>
    </div>

  </div>
</section>
"""

# ─── JavaScript ──────────────────────────────────────────────────────────────
NT_JS = """<script>
/* ── Nutrition Screening Tools (nt-) ─────────────────── */
var NT_SGA_GLOBAL_SELECTED = null;

function ntSetToday(cb) {
  var d = document.getElementById('nt-date');
  if (!d) return;
  if (cb.checked) {
    var now = new Date();
    var mm = ('0' + (now.getMonth() + 1)).slice(-2);
    var dd = ('0' + now.getDate()).slice(-2);
    d.value = now.getFullYear() + '-' + mm + '-' + dd;
    d.disabled = true;
  } else {
    d.disabled = false;
  }
}

function ntTab(name) {
  var tabs = ['snaq', 'mis', 'sga'];
  for (var i = 0; i < tabs.length; i++) {
    var t = document.getElementById('nt-tab-' + tabs[i]);
    var p = document.getElementById('nt-panel-' + tabs[i]);
    if (!t || !p) continue;
    if (tabs[i] === name) {
      t.classList.add('nt-active');
      t.setAttribute('aria-selected', 'true');
      p.classList.add('nt-show');
    } else {
      t.classList.remove('nt-active');
      t.setAttribute('aria-selected', 'false');
      p.classList.remove('nt-show');
    }
  }
}

function ntSnaqUpdate() {
  var q1 = document.querySelector('input[name="snaq1"]:checked');
  var q2 = document.querySelector('input[name="snaq2"]:checked');
  var q3 = document.querySelector('input[name="snaq3"]:checked');
  if (!q1 || !q2 || !q3) return;
  var score = parseInt(q1.value, 10) + parseInt(q2.value, 10) + parseInt(q3.value, 10);
  var box = document.getElementById('snaq-result');
  var sc = document.getElementById('snaq-score');
  var lb = document.getElementById('snaq-label');
  var ds = document.getElementById('snaq-desc');
  if (!box) return;
  sc.textContent = 'Score: ' + score + ' / 6';
  box.classList.remove('nt-normal', 'nt-moderate', 'nt-severe');
  if (score <= 1) {
    box.classList.add('nt-normal');
    lb.textContent = 'Not Malnourished';
    ds.textContent = 'Score 0–1. No nutritional intervention required at this time. Re-screen monthly or if clinical condition changes.';
  } else if (score === 2) {
    box.classList.add('nt-moderate');
    lb.textContent = 'Moderate Risk';
    ds.textContent = 'Score 2. Dietary counseling recommended. Consult dietitian for individualized nutritional plan. Monitor weight and intake closely.';
  } else {
    box.classList.add('nt-severe');
    lb.textContent = 'Severe Risk — Nutritional Support Indicated';
    ds.textContent = 'Score ≥3. Immediate nutrition support indicated. Refer to dietitian and consider oral nutritional supplements (ONS) or intradialytic parenteral nutrition (IDPN) if on dialysis.';
  }
  box.classList.add('nt-show');
}

function ntMisUpdate() {
  var ids = ['mis1','mis2','mis3','mis4','mis5','mis6','mis7','mis8','mis9','mis10'];
  var total = 0;
  var allFilled = true;
  for (var i = 0; i < ids.length; i++) {
    var el = document.getElementById(ids[i]);
    if (!el || el.value === '') { allFilled = false; continue; }
    total += parseInt(el.value, 10);
  }
  if (!allFilled) return;
  var box = document.getElementById('mis-result');
  var sc = document.getElementById('mis-score');
  var lb = document.getElementById('mis-label');
  var ds = document.getElementById('mis-desc');
  if (!box) return;
  sc.textContent = 'Score: ' + total + ' / 30';
  box.classList.remove('nt-normal', 'nt-moderate', 'nt-severe');
  if (total <= 5) {
    box.classList.add('nt-normal');
    lb.textContent = 'Normal / Mild Malnutrition';
    ds.textContent = 'MIS 0–5. Acceptable nutritional status. Continue routine monitoring. Re-assess at each clinic or dialysis visit.';
  } else if (total <= 10) {
    box.classList.add('nt-moderate');
    lb.textContent = 'Moderate Malnutrition';
    ds.textContent = 'MIS 6–10. Moderate protein-energy wasting (PEW). Initiate dietary intervention, optimize dialysis adequacy, and consider oral nutritional supplements.';
  } else if (total <= 20) {
    box.classList.add('nt-severe');
    lb.textContent = 'Moderately Severe Malnutrition';
    ds.textContent = 'MIS 11–20. Significant PEW. Prompt dietitian referral, nutritional supplementation (ONS/IDPN), and evaluation for reversible contributors (inadequate dialysis, acidosis, inflammation).';
  } else {
    box.classList.add('nt-severe');
    lb.textContent = 'Severe Malnutrition';
    ds.textContent = 'MIS 21–30. Severe PEW — high mortality risk. Urgent multidisciplinary nutritional intervention. Consider enteral/parenteral support and address underlying inflammation and comorbidities.';
  }
  box.classList.add('nt-show');
}

function ntSgaUpdate() {
  /* Update guidance but result shown only after global rating */
}

function ntSgaGlobal(rating, btn) {
  NT_SGA_GLOBAL_SELECTED = rating;
  var pills = document.querySelectorAll('#sga-global-btns .nt-sga-pill');
  for (var i = 0; i < pills.length; i++) pills[i].classList.remove('nt-selected');
  btn.classList.add('nt-selected');

  var box = document.getElementById('sga-result');
  var sc = document.getElementById('sga-score');
  var lb = document.getElementById('sga-label');
  var ds = document.getElementById('sga-desc');
  if (!box) return;
  box.classList.remove('nt-normal', 'nt-moderate', 'nt-severe');
  if (rating === 'A') {
    sc.textContent = 'SGA — A';
    lb.textContent = 'Well Nourished';
    ds.textContent = 'No significant nutritional deficits. Maintain current diet. Re-assess at next visit.';
    box.classList.add('nt-normal');
  } else if (rating === 'B') {
    sc.textContent = 'SGA — B';
    lb.textContent = 'Mildly / Moderately Malnourished';
    ds.textContent = 'Evidence of mild-to-moderate protein-energy wasting. Initiate dietary counseling, optimize protein/energy intake, and re-assess in 4–6 weeks.';
    box.classList.add('nt-moderate');
  } else {
    sc.textContent = 'SGA — C';
    lb.textContent = 'Severely Malnourished';
    ds.textContent = 'Severe protein-energy wasting. Urgent dietitian referral. Consider oral nutritional supplements, IDPN, or enteral nutrition. Address underlying disease burden.';
    box.classList.add('nt-severe');
  }
  box.classList.add('nt-show');
}

function ntReset() {
  /* SNAQ */
  var radios = document.querySelectorAll('input[name="snaq1"], input[name="snaq2"], input[name="snaq3"]');
  for (var i = 0; i < radios.length; i++) radios[i].checked = false;
  var sr = document.getElementById('snaq-result');
  if (sr) { sr.classList.remove('nt-show','nt-normal','nt-moderate','nt-severe'); }

  /* MIS */
  var mis = ['mis1','mis2','mis3','mis4','mis5','mis6','mis7','mis8','mis9','mis10'];
  for (var j = 0; j < mis.length; j++) {
    var el = document.getElementById(mis[j]);
    if (el) el.value = '';
  }
  var mr = document.getElementById('mis-result');
  if (mr) { mr.classList.remove('nt-show','nt-normal','nt-moderate','nt-severe'); }

  /* SGA */
  var sgaSels = ['sga-a1','sga-a2','sga-b','sga-c','sga-d'];
  for (var k = 0; k < sgaSels.length; k++) {
    var s = document.getElementById(sgaSels[k]);
    if (s) s.value = '';
  }
  var sgaRad = document.querySelectorAll('input[name="sga-e1"], input[name="sga-e2"], input[name="sga-e3"]');
  for (var m = 0; m < sgaRad.length; m++) sgaRad[m].checked = false;
  var pills = document.querySelectorAll('#sga-global-btns .nt-sga-pill');
  for (var n = 0; n < pills.length; n++) pills[n].classList.remove('nt-selected');
  NT_SGA_GLOBAL_SELECTED = null;
  var sgaR = document.getElementById('sga-result');
  if (sgaR) { sgaR.classList.remove('nt-show','nt-normal','nt-moderate','nt-severe'); }

  /* Demographics */
  var fields = ['nt-name','nt-age','nt-date'];
  for (var f = 0; f < fields.length; f++) {
    var fi = document.getElementById(fields[f]);
    if (fi) { fi.value = ''; fi.disabled = false; }
  }
  var sex = document.getElementById('nt-sex');
  if (sex) sex.value = '';
  var tod = document.getElementById('nt-today');
  if (tod) tod.checked = false;
}

function ntPrint(tool) {
  var name = (document.getElementById('nt-name') || {value:''}).value || '—';
  var age  = (document.getElementById('nt-age')  || {value:''}).value || '—';
  var sex  = (document.getElementById('nt-sex')  || {value:''}).value || '—';
  var date = (document.getElementById('nt-date') || {value:''}).value || '—';

  var title = tool === 'snaq' ? 'SNAQ Score' : tool === 'mis' ? 'Malnutrition-Inflammation Score (MIS)' : 'Subjective Global Assessment (SGA)';
  var resultEl = document.getElementById(tool + '-result');
  var scoreEl  = document.getElementById(tool + '-score');
  var labelEl  = document.getElementById(tool + '-label');
  var descEl   = document.getElementById(tool + '-desc');

  var scoreText = scoreEl  ? scoreEl.textContent  : '—';
  var labelText = labelEl  ? labelEl.textContent  : '—';
  var descText  = descEl   ? descEl.textContent   : '';
  var hasResult = resultEl && resultEl.classList.contains('nt-show');

  var html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>' + title + '</title>'
    + '<style>body{font-family:Arial,sans-serif;max-width:700px;margin:40px auto;color:#1e2a38;font-size:14px;}'
    + 'h1{font-size:22px;color:#1a6b72;margin-bottom:4px;}h2{font-size:16px;margin-top:24px;border-bottom:1px solid #ddd;padding-bottom:4px;}'
    + 'table{border-collapse:collapse;width:100%;}td,th{border:1px solid #ddd;padding:7px 10px;font-size:13px;}'
    + 'th{background:#f4f6f9;font-weight:600;}.result{background:#e6f4ea;border:1px solid #b2dfdb;border-radius:8px;padding:14px 18px;margin-top:16px;}'
    + '.score{font-size:1.6rem;font-weight:800;color:#1a6b72;}.footer{font-size:11px;color:#888;margin-top:30px;border-top:1px solid #ddd;padding-top:8px;}'
    + '</style></head><body>'
    + '<h1>' + title + '</h1>'
    + '<p style="color:#6b7a8d;font-size:13px;">Dr. W. G. M. Rivero, MD, FPCP, DPSN &mdash; williamriveromd.com</p>'
    + '<h2>Patient Information</h2>'
    + '<table><tr><th>Name</th><td>' + name + '</td><th>Age</th><td>' + age + '</td></tr>'
    + '<tr><th>Sex</th><td>' + sex + '</td><th>Date</th><td>' + date + '</td></tr></table>';

  if (hasResult) {
    html += '<div class="result"><div class="score">' + scoreText + '</div>'
      + '<div style="font-weight:700;margin:4px 0;">' + labelText + '</div>'
      + '<div style="font-size:13px;color:#444;">' + descText + '</div></div>';
  } else {
    html += '<p style="color:#c00;">Complete the assessment to see results before printing.</p>';
  }

  html += '<p class="footer">Generated by williamriveromd.com Nutrition Screening Tools &mdash; For clinical use only. Not a substitute for full nutritional assessment by a registered dietitian.</p></body></html>';

  var win = window.open('', '_blank');
  if (!win) { alert('Please allow pop-ups for this site to print.'); return; }
  win.document.write(html);
  win.document.close();
  setTimeout(function(){ win.print(); }, 400);
}
</script>
"""

# ─── Helper: read file ───────────────────────────────────────────────────────
def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def patch(path, old, new, label):
    content = read(path)
    if old not in content:
        print(f'  SKIP [{label}] — anchor not found in {path}')
        return False
    if new in content:
        print(f'  ALREADY [{label}] — already applied in {path}')
        return False
    write(path, content.replace(old, new, 1))
    print(f'  OK [{label}] in {path}')
    return True

# ─── 1. nutrition-kidney-patients.html ──────────────────────────────────────
p1 = '/home/user/williamriveromd.github.io/guides/nutrition-kidney-patients.html'
print('Patching:', p1)

# CSS already inserted (from prior run) — skip if already present
c1 = read(p1)
if '.nt-section{' not in c1:
    patch(p1,
        '.faq-item.faq-open .faq-a{display:block;}\n</style>',  # won't match; use per-guide end
        '.faq-item.faq-open .faq-a{display:block;}\n' + NT_CSS + '</style>',
        'CSS')
else:
    print('  CSS already present in nutrition-kidney-patients.html')

# HTML section — before </main>
patch(p1,
    '\n</main>',
    '\n' + NT_HTML + '\n</main>',
    'HTML section')

# JS — before first non-JSON <script>
patch(p1,
    '\n<script>\n  const DARK_KEY=',
    '\n' + NT_JS + '\n<script>\n  const DARK_KEY=',
    'JS block')

# ─── 2. eating-on-dialysis.html ─────────────────────────────────────────────
p2 = '/home/user/williamriveromd.github.io/guides/eating-on-dialysis.html'
print('Patching:', p2)

# CSS — before second </style> (per-guide style end at line ~1193)
patch(p2,
    '.faq-item.faq-open .faq-a{display:block;}\n</style>\n\n<script type="application/ld+json">',
    '.faq-item.faq-open .faq-a{display:block;}\n' + NT_CSS + '</style>\n\n<script type="application/ld+json">',
    'CSS')

# Nav pill after #prom-tools
patch(p2,
    '<a class="nav-pill" href="#prom-tools"><span data-lang="en">QoL Tools</span><span class="lang-hidden" data-lang="tl">Mga Kasangkapan sa QoL</span><span class="lang-hidden" data-lang="ceb">Mga Himan sa QoL</span><span class="lang-hidden" data-lang="kap">Deng Kasangkapan sa QoL</span></a>',
    '<a class="nav-pill" href="#prom-tools"><span data-lang="en">QoL Tools</span><span class="lang-hidden" data-lang="tl">Mga Kasangkapan sa QoL</span><span class="lang-hidden" data-lang="ceb">Mga Himan sa QoL</span><span class="lang-hidden" data-lang="kap">Deng Kasangkapan sa QoL</span></a>\n    <a class="nav-pill" href="#nut-tools"><span data-lang="en">Nutrition Screening</span><span data-lang="tl" class="lang-hidden">Nutrition Screening</span><span data-lang="ceb" class="lang-hidden">Nutrition Screening</span><span data-lang="kap" class="lang-hidden">Nutrition Screening</span></a>',
    'nav pill')

# HTML section — before </div><!-- end .mode-patient -->
patch(p2,
    '</div><!-- end .mode-patient -->',
    NT_HTML + '\n</div><!-- end .mode-patient -->',
    'HTML section')

# JS — before first non-JSON <script>
c2 = read(p2)
# Find the first <script> that is NOT application/ld+json
import re as _re
m = _re.search(r'\n(<script>)', c2)
if m:
    first_script = m.group(1)
    if NT_JS.strip() not in c2:
        idx = c2.index('\n' + first_script)
        c2 = c2[:idx] + '\n' + NT_JS + '\n' + first_script + c2[idx + len('\n' + first_script):]
        write(p2, c2)
        print('  OK [JS block] in eating-on-dialysis.html')
    else:
        print('  ALREADY [JS block] in eating-on-dialysis.html')
else:
    print('  SKIP [JS block] — <script> not found in eating-on-dialysis.html')

# ─── 3. kain-pa-rin.html ─────────────────────────────────────────────────────
p3 = '/home/user/williamriveromd.github.io/guides/kain-pa-rin.html'
print('Patching:', p3)

# CSS — before second </style>
patch(p3,
    'html[data-theme="dark"] .qr-table tr:nth-child(even) td { background: #1a2535; }\n</style>',
    'html[data-theme="dark"] .qr-table tr:nth-child(even) td { background: #1a2535; }\n' + NT_CSS + '</style>',
    'CSS')

# Nav pills
patch(p3,
    '<a class="nav-pill mode-patient-pill" href="#pt-faq">FAQ</a>',
    '<a class="nav-pill mode-patient-pill" href="#pt-faq">FAQ</a>\n  <a class="nav-pill mode-patient-pill" href="#nut-tools">Nutrition Screening</a>',
    'patient nav pill')

patch(p3,
    '<a class="nav-pill mode-physician-pill" href="#md-quickref">Quick Ref</a>',
    '<a class="nav-pill mode-physician-pill" href="#md-quickref">Quick Ref</a>\n  <a class="nav-pill mode-physician-pill" href="#nut-tools">SGA / MIS / SNAQ</a>',
    'physician nav pill')

# HTML section — before </main>
patch(p3,
    '\n</main>',
    '\n' + NT_HTML + '\n</main>',
    'HTML section')

# JS — before first non-JSON <script>
c3 = read(p3)
m3 = _re.search(r'\n(<script>)', c3)
if m3:
    first_script = m3.group(1)
    if NT_JS.strip() not in c3:
        idx = c3.index('\n' + first_script)
        c3 = c3[:idx] + '\n' + NT_JS + '\n' + first_script + c3[idx + len('\n' + first_script):]
        write(p3, c3)
        print('  OK [JS block] in kain-pa-rin.html')
    else:
        print('  ALREADY [JS block] in kain-pa-rin.html')
else:
    print('  SKIP [JS block] — <script> not found in kain-pa-rin.html')

# ─── 4. ckd-dri-calculator.html ──────────────────────────────────────────────
p4 = '/home/user/williamriveromd.github.io/guides/ckd-dri-calculator.html'
print('Patching:', p4)

# CSS — before second </style>
c4 = read(p4)
if '.nt-section{' not in c4:
    patch(p4,
        'body.dark .related-card-title {\n  color: #e8edf2;\n}\n</style>',
        'body.dark .related-card-title {\n  color: #e8edf2;\n}\n' + NT_CSS + '</style>',
        'CSS')
else:
    print('  CSS already present in ckd-dri-calculator.html')

# Nav pill
patch(p4,
    '<a class="nav-pill" href="#tips"><span data-lang="en">Practical Tips</span><span class="lang-hidden" data-lang="tl">Mga Praktikal na Tip</span><span class="lang-hidden" data-lang="ceb">Mga Praktikal nga Tip</span><span class="lang-hidden" data-lang="kap">Deng Praktikal a Tip</span></a>',
    '<a class="nav-pill" href="#tips"><span data-lang="en">Practical Tips</span><span class="lang-hidden" data-lang="tl">Mga Praktikal na Tip</span><span class="lang-hidden" data-lang="ceb">Mga Praktikal nga Tip</span><span class="lang-hidden" data-lang="kap">Deng Praktikal a Tip</span></a>\n<a class="nav-pill" href="#nut-tools"><span data-lang="en">Nutrition Screening</span><span class="lang-hidden" data-lang="tl">Nutrition Screening</span><span class="lang-hidden" data-lang="ceb">Nutrition Screening</span><span class="lang-hidden" data-lang="kap">Nutrition Screening</span></a>',
    'nav pill')

# HTML section — before </main>
patch(p4,
    '\n</main>',
    '\n' + NT_HTML + '\n</main>',
    'HTML section')

# JS
c4r = read(p4)
m4 = _re.search(r'\n(<script>)', c4r)
if m4:
    first_script = m4.group(1)
    if NT_JS.strip() not in c4r:
        idx = c4r.index('\n' + first_script)
        c4r = c4r[:idx] + '\n' + NT_JS + '\n' + first_script + c4r[idx + len('\n' + first_script):]
        write(p4, c4r)
        print('  OK [JS block] in ckd-dri-calculator.html')
    else:
        print('  ALREADY [JS block] in ckd-dri-calculator.html')
else:
    print('  SKIP [JS block] — <script> not found in ckd-dri-calculator.html')

print('Done.')
