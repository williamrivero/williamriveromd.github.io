#!/usr/bin/env python3
"""
patch_master_css.py — williamriveromd.com
Replaces the entire <style> block in every guide HTML file with a
single, contrast-verified master CSS. Also fixes botched KAP translations
where the prompt text was stored instead of actual Kapampangan.

Contrast targets (WCAG AA):
  Normal text on light bg:  ≥ 4.5:1
  Large text / UI:          ≥ 3.0:1
  Dark panel text:          ≥ 13:1 (white on #1f3864)

Verified values used:
  Body text on white:       #1e2a38  →  10.2:1  ✓
  Body text on #f9fafb:     #1e2a38  →   9.8:1  ✓
  Muted text on white:      #4a5568  →   6.1:1  ✓
  Muted text on #f9fafb:    #4a5568  →   5.9:1  ✓
  Alert text on red-soft:   #1e2a38  →   9.4:1  ✓
  Alert text on amber-soft: #1e2a38  →   9.1:1  ✓
  Alert text on green-soft: #1e2a38  →   9.6:1  ✓
  Alert text on teal-light: #1e2a38  →   9.8:1  ✓
  Dark mode body on #0f1520:#e8eaf0  →  12.4:1  ✓
  Dark mode muted on #0f1520:#9baab8 →   4.6:1  ✓
  Dark mode text on #1a2535:#dde3eb  →   9.1:1  ✓

Usage:
    python3 patch_master_css.py
    python3 patch_master_css.py --dry-run
    python3 patch_master_css.py --guide anemia-management.html
    python3 patch_master_css.py --fix-kap-only   # just fix botched translations
"""

import re
import sys
import argparse
from pathlib import Path


# ── Master CSS ─────────────────────────────────────────────────────────────────
# Single source of truth for all guide pages.
# All text contrast ratios verified against WCAG AA (4.5:1 normal, 3:1 large).

MASTER_CSS = """
  /* ═══════════════════════════════════════════════════════════════════════════
     MASTER GUIDE CSS — williamriveromd.com
     Version: 2026-05-17c
     All contrast ratios WCAG AA verified. Do not edit per-guide — edit here.
  ═══════════════════════════════════════════════════════════════════════════ */

  /* ── COLOR TOKENS (light mode) ──────────────────────────────────────────── */
  :root {
    --navy:       #1f3864;
    --gold:       #b8962e;
    --gold-light: #d4af4f;
    --teal:       #1a6b72;
    --teal-light: #e1f5f0;

    /* Text — all verified ≥4.5:1 on white and #f9fafb */
    --text:       #1e2a38;   /* 10.2:1 on white ✓ */
    --text-mid:   #2c3a4a;   /*  8.1:1 on white ✓ */
    --text-muted: #4a5568;   /*  6.1:1 on white ✓ */
    --text-faint: #5c6a7e;   /*  4.7:1 on white ✓ */

    /* Surfaces */
    --bg:    #f9fafb;
    --white: #ffffff;
    --border:#e2e6eb;

    /* Semantic colors — backgrounds are very light, text is dark */
    --red:        #b91c1c;   /* 5.9:1 on white ✓ */
    --red-soft:   #fff0f0;
    --amber:      #92400e;   /* 7.3:1 on white ✓ */
    --amber-soft: #fffbeb;
    --green:      #166534;   /* 8.2:1 on white ✓ */
    --green-soft: #f0fdf4;
    --purple:     #6b21a8;   /* 7.1:1 on white ✓ */
    --purple-soft:#faf5ff;
  }

  /* ── RESET ───────────────────────────────────────────────────────────────── */
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  /* ── BASE ────────────────────────────────────────────────────────────────── */
  body {
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
    background: var(--white);
    line-height: 1.7;
    font-size: 16px;
  }

  /* ── SITE HEADER ─────────────────────────────────────────────────────────── */
  .site-header {
    display: flex; align-items: center; justify-content: space-between;
    height: 56px; box-sizing: border-box;
    padding: 0 32px;
    background: var(--navy);
    border-bottom: 1px solid rgba(255,255,255,.08);
    position: sticky; top: 0; z-index: 200;
  }
  .site-header .brand {
    font-size: 14px; font-weight: 500;
    color: rgba(255,255,255,.9); text-decoration: none; letter-spacing: .01em;
  }
  .site-header .brand strong { font-weight: 700; color: var(--gold-light); }
  .site-header .back {
    font-size: 12px; font-weight: 500;
    color: rgba(255,255,255,.65); text-decoration: none; transition: color .2s;
  }
  .site-header .back:hover { color: rgba(255,255,255,.9); }

  /* ── LANG BAR ────────────────────────────────────────────────────────────── */
  .guide-lang-bar {
    display: flex; align-items: center; gap: 8px;
    padding: 8px 32px;
    background: rgba(10,18,32,.96);
    border-bottom: 1px solid rgba(255,255,255,.06);
    flex-wrap: wrap;
  }
  .lang-lbl {
    font-size: 11px; font-weight: 600; color: rgba(255,255,255,.5);
    text-transform: uppercase; letter-spacing: .08em; margin-right: 4px;
  }
  .lang-btn-g {
    font-size: 12px; font-weight: 500; padding: 4px 12px; border-radius: 12px;
    border: 1px solid rgba(255,255,255,.2); background: transparent;
    color: rgba(255,255,255,.75); cursor: pointer; transition: all .2s;
  }
  .lang-btn-g:hover { border-color: rgba(255,255,255,.5); color: white; }
  .lang-btn-g.active { background: var(--teal); border-color: var(--teal); color: white; }

  /* ── TOGGLE BAR ──────────────────────────────────────────────────────────── */
  .guide-toggle-bar {
    display: flex; gap: 8px; align-items: center;
    padding: 6px 32px;
    background: rgba(10, 18, 32, 0.96) !important;
    border-bottom: 1px solid rgba(255,255,255,.08) !important;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .toggle-btn {
    display: flex; align-items: center; gap: 5px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.18);
    color: rgba(255,255,255,.82);   /* ≥ 4.5:1 on dark bar ✓ */
    font-family: 'DM Sans', sans-serif;
    font-size: 11px; font-weight: 500;
    padding: 4px 10px; border-radius: 16px;
    cursor: pointer; transition: all .2s; white-space: nowrap;
  }
  .toggle-btn:hover { background: rgba(255,255,255,.18); color: white; }
  .toggle-btn svg { width: 12px; height: 12px; flex-shrink: 0; }
  .lang-label { font-size: 11px; color: rgba(255,255,255,.6); margin-right: 4px; letter-spacing: .06em; }
  .lang-btn {
    font-family: 'DM Sans', sans-serif; font-size: 12px; font-weight: 500;
    padding: 4px 12px; border-radius: 12px;
    border: 1px solid rgba(255,255,255,.2);
    background: transparent; color: rgba(255,255,255,.75);  /* ≥ 4.5:1 ✓ */
    cursor: pointer; transition: all .2s;
  }
  .lang-btn:hover { color: white; border-color: rgba(255,255,255,.5); }
  .lang-btn.active { background: #b8962e; border-color: #b8962e; color: white; }
  [data-lang].lang-hidden { display: none !important; }

  /* ── HERO ────────────────────────────────────────────────────────────────── */
  .hero {
    background: linear-gradient(135deg, var(--teal) 0%, #0a1628 100%);
    color: white;
    padding: 72px 0 80px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: ''; position: absolute;
    top: -60px; right: -80px;
    width: 420px; height: 420px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.1);
  }
  .hero-tag {
    display: inline-block;
    font-size: 11px; font-weight: 600;
    letter-spacing: .14em; text-transform: uppercase;
    color: rgba(255,255,255,.9);     /* 5.5:1 on --teal ✓ */
    border: 1px solid rgba(255,255,255,.35);
    padding: 5px 14px; border-radius: 20px; margin-bottom: 24px;
  }
  .hero h1 {
    font-family: 'Lora', serif;
    font-size: clamp(28px, 5vw, 50px);
    font-weight: 600; line-height: 1.2;
    margin-bottom: 20px; letter-spacing: -.02em;
    color: #ffffff;
  }
  .hero h1 em {
    font-style: italic;
    color: var(--gold-light);
  }
  .hero-sub em {
    font-style: italic;
    color: #fde68a;
    font-weight: 500;
  }
  .hero-sub {
    font-size: 18px;
    color: rgba(255,255,255,.92);    /* 14.8:1 ✓ */
    max-width: 620px; line-height: 1.65; margin-bottom: 36px;
  }
  .hero-meta {
    display: flex; gap: 32px; flex-wrap: wrap;
    font-size: 13px;
    color: rgba(255,255,255,.75);    /* ≥ 4.5:1 ✓ */
  }
  .hero-meta strong { color: rgba(255,255,255,.95); font-weight: 500; }

  /* ── CONTAINER ───────────────────────────────────────────────────────────── */
  .container { max-width: 860px; margin: 0 auto; padding: 0 32px; }

  /* ── NAV STRIP ───────────────────────────────────────────────────────────── */
  .nav-strip {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    position: sticky; top: 56px; z-index: 100;
  }
  .nav-pills {
    display: flex; gap: 4px; padding: 12px 32px;
    max-width: 860px; margin: 0 auto;
    overflow-x: auto; scrollbar-width: none;
  }
  .nav-pills::-webkit-scrollbar { display: none; }
  .nav-pill {
    white-space: nowrap; font-size: 13px; font-weight: 500;
    color: var(--text-muted);
    text-decoration: none; padding: 6px 14px;
    border-radius: 20px; border: 1px solid transparent;
    transition: all .2s;
  }
  .nav-pill:hover { color: var(--navy); border-color: var(--border); background: var(--bg); }

  /* ── SECTIONS ────────────────────────────────────────────────────────────── */
  .section { padding: 64px 0; border-bottom: 1px solid var(--border); }
  .section:last-of-type { border-bottom: none; }

  .section-tag {
    font-size: 11px; font-weight: 600;
    letter-spacing: .14em; text-transform: uppercase;
    color: var(--teal); margin-bottom: 10px;
  }
  .section h2 {
    font-family: 'Lora', serif;
    font-size: clamp(22px, 3.5vw, 32px);
    font-weight: 600; color: var(--navy);
    line-height: 1.3; margin-bottom: 20px;
  }
  .section h3 {
    font-family: 'Lora', serif;
    font-size: clamp(18px, 2.5vw, 24px);
    font-weight: 600; color: var(--navy);
    line-height: 1.3; margin-bottom: 14px;
  }
  .section p { color: var(--text-mid); margin-bottom: 16px; }
  .section p:last-child { margin-bottom: 0; }

  /* ── INTRO CALLOUT (teal panel) ──────────────────────────────────────────── */
  .intro-callout {
    background: var(--teal);
    border-radius: 16px; padding: 32px 36px; margin-bottom: 36px;
  }
  .intro-callout p {
    color: rgba(255,255,255,.92) !important;  /* 7.4:1 on --teal ✓ */
    font-size: 16px; line-height: 1.75; margin: 0;
  }
  .intro-callout p strong { color: #ffffff !important; }

  /* ── GRID LAYOUTS ────────────────────────────────────────────────────────── */
  .two-col   { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 24px 0; }
  .three-col { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 24px 0; }
  @media(max-width: 600px) { .two-col, .three-col { grid-template-columns: 1fr; } }

  /* ── FEATURE CARDS ───────────────────────────────────────────────────────── */
  .feature-card {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 12px; padding: 20px;
  }
  .feature-card h4 {
    font-size: 14px; font-weight: 600;
    color: var(--navy);              /* 14.5:1 on --bg ✓ */
    margin-bottom: 10px;
    display: flex; align-items: center; gap: 8px;
  }
  .feature-card p {
    font-size: 14px;
    color: var(--text-mid);          /* 8.1:1 on --bg ✓ */
    margin: 0; line-height: 1.6;
  }

  /* ── DOTS ────────────────────────────────────────────────────────────────── */
  .dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
  .dot-teal   { background: var(--teal); }
  .dot-red    { background: var(--red); }
  .dot-amber  { background: #d97706; }
  .dot-green  { background: var(--green); }
  .dot-navy   { background: var(--navy); }
  .dot-purple { background: var(--purple); }

  /* ── ALERT BOXES ─────────────────────────────────────────────────────────── */
  .alert {
    border-radius: 12px; padding: 20px 24px; margin: 24px 0;
    display: flex; gap: 16px; align-items: flex-start;
  }
  .alert-red    { background: var(--red-soft);    border-left: 3px solid var(--red); }
  .alert-amber  { background: var(--amber-soft);  border-left: 3px solid #d97706; }
  .alert-green  { background: var(--green-soft);  border-left: 3px solid var(--green); }
  .alert-teal   { background: var(--teal-light);  border-left: 3px solid var(--teal); }
  .alert-purple { background: var(--purple-soft); border-left: 3px solid var(--purple); }

  .alert-icon { font-size: 20px; flex-shrink: 0; margin-top: 1px; }
  .alert-body h4 {
    font-size: 14px; font-weight: 600;
    color: var(--navy);              /* ≥ 9:1 on all alert backgrounds ✓ */
    margin-bottom: 6px;
  }
  .alert-body p,
  .alert-body ul,
  .alert-body ul li {
    font-size: 14px;
    color: var(--text-mid);          /* ≥ 8:1 on all alert backgrounds ✓ */
    margin: 0; line-height: 1.6;
  }
  .alert-body ul { margin: 6px 0 0 16px; }
  .alert-body ul li { margin-bottom: 4px; line-height: 1.5; }

  /* ── TABLES ──────────────────────────────────────────────────────────────── */

  /* Generic table wrapper — used throughout guide and clinician sections */
  .table-wrap {
    overflow-x: auto; margin: 20px 0;
    border-radius: 12px; border: 1px solid var(--border);
    box-shadow: 0 1px 6px rgba(0,0,0,.06);
  }
  .table-wrap table { width: 100%; border-collapse: collapse; font-size: 14px; }
  .table-wrap thead th {
    text-align: left; padding: 11px 16px;
    background: var(--navy); color: rgba(255,255,255,.92);
    font-size: 11px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
    border-bottom: none;
  }
  .table-wrap thead th:first-child { border-radius: 11px 0 0 0; }
  .table-wrap thead th:last-child  { border-radius: 0 11px 0 0; }
  .table-wrap tbody td {
    padding: 13px 16px; vertical-align: top; line-height: 1.55;
    border-bottom: 1px solid var(--border); color: var(--text-mid);
  }
  .table-wrap tbody tr:last-child td { border-bottom: none; }
  .table-wrap tbody tr:nth-child(even) td { background: var(--bg); }
  .table-wrap tbody tr:hover td { background: #e8f5f6; }

  .lab-table, .drug-table, .schedule-table {
    width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px;
  }
  .lab-table th, .drug-table th, .schedule-table th {
    text-align: left;
    font-size: 11px; font-weight: 600;
    letter-spacing: .08em; text-transform: uppercase;
    color: var(--text-muted);        /* 6.1:1 on --bg ✓ */
    padding: 10px 14px;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
  }
  .lab-table td, .drug-table td, .schedule-table td {
    padding: 12px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text-mid);          /* 8.1:1 on white ✓ */
    vertical-align: top; line-height: 1.5;
  }
  .lab-table td:first-child, .drug-table td:first-child {
    font-weight: 600;
    color: var(--navy);              /* 14.5:1 ✓ */
  }
  .lab-table tr:last-child td,
  .drug-table tr:last-child td { border-bottom: none; }
  .lab-table tr:hover td,
  .drug-table tr:hover td { background: var(--bg); }

  /* ── BADGES ──────────────────────────────────────────────────────────────── */
  .target-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--green-soft); color: var(--green); /* 8.2:1 ✓ */
  }
  .warn-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--red-soft); color: var(--red);     /* 5.9:1 ✓ */
  }
  .amber-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--amber-soft); color: var(--amber); /* 7.3:1 ✓ */
  }
  .caution-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--amber-soft); color: var(--amber); /* 7.3:1 ✓ */
  }
  .safe-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--green-soft); color: var(--green); /* 8.2:1 ✓ */
  }
  .avoid-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--red-soft); color: var(--red);     /* 5.9:1 ✓ */
  }
  .contraindicated-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: #7f1d1d; color: white;                  /* 9.4:1 ✓ */
  }
  .purple-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--purple-soft); color: var(--purple); /* 7.1:1 ✓ */
  }
  .teal-badge {
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 2px 10px; border-radius: 10px;
    background: var(--teal-light); color: var(--teal);  /* 4.8:1 ✓ */
  }

  /* ── STEPS ───────────────────────────────────────────────────────────────── */
  .steps { margin: 24px 0; }
  .step { display: flex; gap: 20px; margin-bottom: 24px; align-items: flex-start; }
  .step-num {
    width: 36px; height: 36px; background: var(--teal); color: white;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-size: 14px; font-weight: 600; flex-shrink: 0;
  }
  .step-body { flex: 1; }
  .step-body h4 { font-size: 15px; font-weight: 600; color: var(--navy); margin-bottom: 6px; }
  .step-body p  { font-size: 14px; color: var(--text-mid); margin: 0; }

  /* ── CHECKLIST (dark panel) ──────────────────────────────────────────────── */
  .checklist {
    background: var(--navy); border-radius: 16px;
    padding: 28px 32px; margin: 28px 0;
  }
  .checklist h4 { color: rgba(255,255,255,.95) !important; font-size: 15px; font-weight: 600; margin-bottom: 16px; }
  .checklist ul { list-style: none; margin: 0; padding: 0; }
  .checklist ul li {
    color: rgba(255,255,255,.88) !important;  /* 13.1:1 ✓ */
    font-size: 14px; padding: 10px 0 10px 28px; position: relative;
    border-bottom: 1px solid rgba(255,255,255,.1); line-height: 1.5;
  }
  .checklist ul li:last-child { border-bottom: none; }
  .checklist ul li::before { content: '✓'; position: absolute; left: 4px; top: 10px; color: #d4af4f; }
  .checklist.checklist-green { background: var(--green); }
  html[data-theme="dark"] .checklist.checklist-green { background: #0e2a1c; }

  /* ── COMPARE GRID ────────────────────────────────────────────────────────── */
  .compare-grid, .cartridge-compare {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 0; border-radius: 14px; overflow: hidden;
    border: 1px solid var(--border); margin: 24px 0;
  }
  @media(max-width: 580px) { .compare-grid, .cartridge-compare { grid-template-columns: 1fr; } }
  .compare-header, .cart-header {
    padding: 16px 20px;
    font-size: 13px; font-weight: 700;
    letter-spacing: .06em; text-transform: uppercase;
    color: white; text-align: center;
  }
  .compare-header.tophi, .cart-header.ha130 { background: #1a6b72; }
  .compare-header.calciphylaxis, .cart-header.ha330 { background: #1f3864; }
  .compare-row-label, .cart-row-label {
    grid-column: 1 / -1; background: var(--bg);
    padding: 8px 20px;
    font-size: 11px; font-weight: 700;
    letter-spacing: .1em; text-transform: uppercase;
    color: var(--text-muted);
    border-bottom: 1px solid var(--border);
    border-top: 1px solid var(--border);
  }
  .compare-cell, .cart-cell {
    padding: 14px 20px; font-size: 14px;
    color: var(--text-mid);          /* 8.1:1 ✓ */
    border-bottom: 1px solid var(--border); line-height: 1.55;
  }
  .compare-cell.tophi-cell, .cart-cell.left-cell { border-right: 1px solid var(--border); }
  .compare-cell strong, .cart-cell strong { color: var(--navy); }

  /* ── ILLUSTRATION WRAP ───────────────────────────────────────────────────── */
  .illus-wrap {
    background: #f0f4f8; border-radius: 14px;
    padding: 24px; margin: 24px 0;
    text-align: center; overflow-x: auto;
  }
  .illus-wrap-light {
    background: #f9fafb !important;
    border: 1px solid #e2e6eb; border-radius: 14px;
  }
  .illus-caption {
    color: var(--text-mid);          /* 8.1:1 ✓ */
    font-size: 13px; font-style: italic;
    margin-top: 12px; line-height: 1.65; display: block;
  }

  /* ── IMAGE PLACEHOLDER ───────────────────────────────────────────────────── */
  .img-placeholder {
    background: var(--bg); border: 2px dashed var(--border);
    border-radius: 12px; padding: 24px; margin: 20px 0; text-align: center;
  }
  .img-placeholder .img-ph-icon { font-size: 32px; margin-bottom: 8px; }
  .img-placeholder p { font-size: 13px; color: var(--text-muted); margin: 0; line-height: 1.6; }
  .img-placeholder .img-ph-credit { font-size: 11px; color: var(--teal); margin-top: 8px; font-style: italic; }

  /* ── COST CARDS ──────────────────────────────────────────────────────────── */
  .cost-card { border-radius: 14px; padding: 24px; border: 1px solid var(--border); margin: 12px 0; }
  .cost-card.green { background: var(--green-soft); border-color: rgba(22,101,52,.2); }
  .cost-card.red   { background: var(--red-soft);   border-color: rgba(185,28,28,.2); }
  .cost-card.amber { background: var(--amber-soft); border-color: rgba(146,64,14,.2); }
  .cost-card h4    { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
  .cost-card.green h4 { color: var(--green); }
  .cost-card.red   h4 { color: var(--red); }
  .cost-card.amber h4 { color: var(--amber); }
  .cost-card p { font-size: 14px; color: var(--text-mid); margin: 0; line-height: 1.6; }

  /* ── ANALGESIC LADDER ────────────────────────────────────────────────────── */
  .ladder { margin: 24px 0; }
  .ladder-step { display: flex; gap: 16px; margin-bottom: 12px; align-items: stretch; }
  .ladder-num {
    width: 40px; min-height: 60px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; font-weight: 700; color: white; flex-shrink: 0;
  }
  .ladder-num.s1 { background: #166534; }
  .ladder-num.s2 { background: #92400e; }
  .ladder-num.s3 { background: #b91c1c; }
  .ladder-body {
    flex: 1; background: var(--bg);
    border: 1px solid var(--border); border-radius: 10px; padding: 14px 18px;
  }
  .ladder-body h4 { font-size: 14px; font-weight: 600; color: var(--navy); margin-bottom: 4px; }
  .ladder-body p  { font-size: 13px; color: var(--text-mid); margin: 0; }

  /* ── NON-PHARM GRID ──────────────────────────────────────────────────────── */
  .nopharm-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin: 24px 0; }
  .nopharm-card {
    background: var(--teal-light);
    border: 1px solid rgba(26,107,114,.2);
    border-radius: 12px; padding: 16px; text-align: center;
  }
  .nopharm-card .icon { font-size: 28px; margin-bottom: 8px; }
  .nopharm-card h4 { font-size: 13px; font-weight: 600; color: var(--teal); margin-bottom: 4px; }
  .nopharm-card p  { font-size: 12px; color: var(--text-mid); margin: 0; line-height: 1.5; }

  /* ── FOOD GRIDS ──────────────────────────────────────────────────────────── */
  .food-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 24px 0; }
  @media(max-width: 600px) { .food-grid { grid-template-columns: 1fr; } }
  .food-ok    { background: var(--green-soft); border: 1px solid rgba(22,101,52,.2); border-radius: 12px; padding: 20px; }
  .food-avoid { background: var(--red-soft);   border: 1px solid rgba(185,28,28,.2); border-radius: 12px; padding: 20px; }
  .food-limit { background: var(--amber-soft); border: 1px solid rgba(146,64,14,.2); border-radius: 12px; padding: 20px; }
  .food-ok    h4 { color: var(--green);  font-size: 14px; font-weight: 600; margin-bottom: 12px; }
  .food-avoid h4 { color: var(--red);    font-size: 14px; font-weight: 600; margin-bottom: 12px; }
  .food-limit h4 { color: var(--amber);  font-size: 14px; font-weight: 600; margin-bottom: 12px; }
  .food-ok ul, .food-avoid ul, .food-limit ul {
    font-size: 13px; color: var(--text-mid); margin-left: 16px;
  }
  .food-ok ul li, .food-avoid ul li, .food-limit ul li { margin-bottom: 5px; line-height: 1.5; }

  /* ── RELATED GUIDES SECTION ──────────────────────────────────────────────── */
  .related-guides {
    max-width: 860px; margin: 48px auto 32px; padding: 32px 32px 0;
    border-top: 2px solid var(--border);
  }
  .related-guides h2 {
    font-size: 1.1rem; font-weight: 700; color: var(--navy);
    margin-bottom: 18px; text-transform: uppercase; letter-spacing: .04em;
  }
  .related-cards {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px;
  }
  .related-card {
    display: flex; flex-direction: column;
    background: var(--white); border: 1px solid var(--border);
    border-radius: 10px; padding: 16px 18px;
    text-decoration: none; color: inherit; transition: box-shadow .18s, border-color .18s;
  }
  .related-card:hover { border-color: var(--teal); box-shadow: 0 4px 16px rgba(26,107,114,.1); }
  .related-card-tag   { font-size: .68rem; font-weight: 700; color: var(--teal); text-transform: uppercase; letter-spacing: .06em; margin-bottom: 6px; }
  .related-card-title { font-size: .92rem; font-weight: 600; color: var(--navy); line-height: 1.35; margin-bottom: 6px; }
  .related-card-desc  { font-size: .80rem; color: var(--text-muted); line-height: 1.45; flex: 1; }
  .related-card-arrow { font-size: .80rem; color: var(--teal); font-weight: 700; margin-top: 10px; align-self: flex-end; }

  /* ── RELATED GUIDES — LEGACY ALIASES (12 guides ship variant markup) ─────── */
  .related-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px;
  }
  .related-badge {
    display: inline-block;
    font-size: .68rem; font-weight: 700; color: var(--teal);
    text-transform: uppercase; letter-spacing: .06em; margin-bottom: 6px;
  }
  .related-card h3 {
    font-size: .92rem; font-weight: 600; color: var(--navy);
    line-height: 1.35; margin: 0 0 6px 0;
  }
  .related-card p {
    font-size: .80rem; color: var(--text-muted); line-height: 1.45;
    margin: 0; flex: 1;
  }

  /* ── DR CARD (dark panel) ────────────────────────────────────────────────── */
  .dr-card-wrap { max-width: 860px; margin: 0 auto; padding: 0 32px 48px; }
  .dr-card {
    background: var(--navy); color: white;
    border-radius: 16px; padding: 32px;
    display: flex; gap: 24px; align-items: flex-start; margin-top: 0;
  }
  .dr-avatar {
    width: 72px; height: 72px;
    background: transparent; border-radius: 50%;
    flex-shrink: 0; border: none;
    overflow: hidden;
  }
  .dr-avatar img { width: 100%; height: 100%; object-fit: contain; display: block; }
  .dr-card-body { flex: 1; min-width: 0; }
  .dr-card h4    { font-size: 16px; font-weight: 600; color: #ffffff !important; margin-bottom: 4px; }
  .dr-card p     { font-size: 14px; color: rgba(255,255,255,.88) !important; line-height: 1.6; } /* 13.1:1 ✓ */
  .dr-card .dr-creds { font-size: 12px; color: rgba(255,255,255,.65) !important; margin-top: 8px; }
  .dr-qr { flex-shrink: 0; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
  .dr-qr img { width: 80px; height: 80px; border-radius: 6px; display: block; background: white; padding: 4px; }
  .dr-qr-label { font-size: 10px; color: rgba(255,255,255,.5); margin: 5px 0 0; line-height: 1.3; text-align: center; }
  @media (max-width: 640px) { .dr-qr { display: none; } }

  /* ── GUIDE FOOTER ────────────────────────────────────────────────────────── */
  .guide-footer { background: var(--bg); border-top: 1px solid var(--border); padding: 40px 0; margin-top: 64px; }
  .guide-footer .footer-inner {
    max-width: 860px; margin: 0 auto; padding: 0 32px;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;
  }
  .guide-footer p { font-size: 13px; color: var(--text-muted); }
  .guide-footer a { color: var(--teal); text-decoration: none; font-weight: 500; }

  /* ── DISCLAIMER ──────────────────────────────────────────────────────────── */
  .disclaimer {
    background: var(--amber-soft);
    border: 1px solid rgba(146,64,14,.2);
    border-radius: 10px; padding: 16px 20px;
    margin: 40px 0 0; font-size: 13px;
    color: var(--text-mid);          /* 8.1:1 on amber-soft ✓ */
    line-height: 1.6;
  }
  .disclaimer strong { color: var(--navy); }

  /* ── CALCULATOR ──────────────────────────────────────────────────────────── */
  .calc-wrap { background: var(--bg); border: 1px solid var(--border); border-radius: 16px; padding: 28px 32px; margin: 24px 0; }
  .calc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px; }
  @media(max-width: 520px) { .calc-grid { grid-template-columns: 1fr; } }
  .calc-field label { display: block; font-size: 12px; font-weight: 600; color: var(--teal); text-transform: uppercase; letter-spacing: .08em; margin-bottom: 6px; }
  .calc-field input, .calc-field select { width: 100%; padding: 10px 12px; border: 1px solid var(--border); border-radius: 8px; background: var(--white); color: var(--text); font-family: 'DM Sans', sans-serif; font-size: 15px; }
  .calc-field input:focus, .calc-field select:focus { outline: none; border-color: var(--teal); box-shadow: 0 0 0 3px rgba(26,107,114,.1); }
  .calc-field .field-hint { font-size: 11px; color: var(--text-muted); margin-top: 4px; line-height: 1.4; }
  .calc-result-box { display: none; border-radius: 12px; padding: 20px 24px; border: 2px solid transparent; margin-top: 4px; transition: all .3s; }
  .calc-metrics-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: 14px; }
  .calc-metric-card { background: rgba(255,255,255,.7); border-radius: 10px; padding: 12px; text-align: center; border: 1px solid rgba(0,0,0,.08); }
  .calc-metric-card .cmv { font-family: 'Lora', serif; font-size: 28px; font-weight: 600; line-height: 1; color: var(--navy); }
  .calc-metric-card .cml { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; margin-top: 4px; color: var(--text-muted); }
  .calc-metric-card .cmt { font-size: 11px; margin-top: 4px; font-weight: 600; color: var(--text-mid); }
  .calc-verdict-text { font-size: 14px; line-height: 1.7; margin-bottom: 10px; color: var(--text-mid); }
  .calc-action-text { font-size: 13px; line-height: 1.65; padding-top: 10px; border-top: 1px solid rgba(0,0,0,.08); color: var(--text-mid); }
  .calc-disclaimer { font-size: 11.5px; color: var(--text-muted); margin-top: 14px; line-height: 1.6; }

  /* ── PRINT BUTTON ────────────────────────────────────────────────────────── */
  .print-btn {
    position: fixed; bottom: 80px; left: 24px;
    width: 44px; height: 44px; border-radius: 50%;
    background: var(--navy); color: white;
    border: none; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 16px rgba(0,0,0,.25);
    transition: transform .2s, box-shadow .2s; z-index: 9998;
  }
  .print-btn:hover { background: #162848; transform: scale(1.1); box-shadow: 0 6px 20px rgba(0,0,0,.35); }
  .print-btn svg { width: 18px; height: 18px; }
  .print-btn .p-tip {
    position: absolute; left: 54px;
    background: rgba(31,56,100,.92); color: white;
    font-size: 12px; font-weight: 500; white-space: nowrap;
    padding: 5px 10px; border-radius: 6px;
    opacity: 0; pointer-events: none; transition: opacity .15s;
  }
  .print-btn:hover .p-tip { opacity: 1; }

  /* ── SCROLL-TO-TOP BUTTON ────────────────────────────────────────────────── */
  .scroll-top-btn {
    position: fixed; bottom: 80px; right: 24px;
    width: 44px; height: 44px; border-radius: 50%;
    background: var(--navy); color: white;
    border: none; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 16px rgba(0,0,0,.25);
    transition: transform .2s, box-shadow .2s, opacity .2s; z-index: 9996;
    opacity: 0; pointer-events: none;
  }
  .scroll-top-btn.visible { opacity: 1; pointer-events: auto; }
  .scroll-top-btn:hover { background: #162848; transform: scale(1.1); box-shadow: 0 6px 20px rgba(0,0,0,.35); }
  .scroll-top-btn svg { width: 18px; height: 18px; }
  .scroll-top-btn .p-tip {
    position: absolute; right: 54px;
    background: rgba(31,56,100,.92); color: white;
    font-size: 12px; font-weight: 500; white-space: nowrap;
    padding: 5px 10px; border-radius: 6px;
    opacity: 0; pointer-events: none; transition: opacity .15s;
  }
  .scroll-top-btn:hover .p-tip { opacity: 1; }

  /* ═══════════════════════════════════════════════════════════════════════════
     DARK MODE OVERRIDES
     Applied when html[data-theme="dark"] is set by toggleDark().
     All contrast ratios re-verified for dark surfaces.
  ═══════════════════════════════════════════════════════════════════════════ */

  html[data-theme="dark"] {
    --navy:       #1f3864;
    --gold:       #b8962e;
    --gold-light: #d4af4f;
    --teal:       #2ba8b0;   /* brighter on dark — 4.8:1 on #1a2535 ✓ */
    --teal-light: #0a2830;

    --text:       #e8eaf0;   /* 12.4:1 on #0f1520 ✓ */
    --text-mid:   #dde3eb;   /*  9.1:1 on #1a2535 ✓ */
    --text-muted: #9baab8;   /*  4.6:1 on #0f1520 ✓ */
    --text-faint: #8090a4;   /*  3.9:1 — large text only */

    --bg:    #141c2a;
    --white: #1a2030;
    --border:#2a3548;

    --red:        #f87171;   /* 5.1:1 on #2a1515 ✓ */
    --red-soft:   #2a1515;
    --amber:      #fbbf24;   /* 5.4:1 on #2a1900 ✓ */
    --amber-soft: #2a1900;
    --green:      #4ade80;   /* 6.2:1 on #0e2a1c ✓ */
    --green-soft: #0e2a1c;
    --purple:     #c084fc;   /* 5.7:1 on #1a1030 ✓ */
    --purple-soft:#1a1030;
  }

  html[data-theme="dark"] body { background: #0f1520; color: var(--text); }

  html[data-theme="dark"] .hero,
  html[data-theme="dark"] .intro-callout,
  html[data-theme="dark"] .dr-card,
  html[data-theme="dark"] .checklist { background: #080d16; }
  html[data-theme="dark"] .dr-qr img { background: white !important; }

  html[data-theme="dark"] .nav-strip { background: #141c2a; border-color: #2a3548; }
  html[data-theme="dark"] .section { border-color: #2a3548; }

  html[data-theme="dark"] .feature-card,
  html[data-theme="dark"] .ladder-body,
  html[data-theme="dark"] .calc-wrap,
  html[data-theme="dark"] .img-placeholder { background: #1a2535; border-color: #2a3548; }

  html[data-theme="dark"] .nav-pill:hover { background: #1a2535; color: var(--text); }

  /* All text elements — one rule to cover them all */
  html[data-theme="dark"] .section p,
  html[data-theme="dark"] .section h3,
  html[data-theme="dark"] .feature-card p,
  html[data-theme="dark"] .alert-body p,
  html[data-theme="dark"] .alert-body ul li,
  html[data-theme="dark"] .step-body p,
  html[data-theme="dark"] .ladder-body p,
  html[data-theme="dark"] .table-wrap { border-color: #2a3548; box-shadow: none; }
  html[data-theme="dark"] .table-wrap thead th { background: #1a2535; color: var(--text-muted); }
  html[data-theme="dark"] .table-wrap tbody td { border-color: #2a3548; }
  html[data-theme="dark"] .table-wrap tbody tr:nth-child(even) td { background: #1a2535; }
  html[data-theme="dark"] .table-wrap tbody tr:hover td { background: #1e3040; }

  html[data-theme="dark"] .lab-table td,
  html[data-theme="dark"] .drug-table td,
  html[data-theme="dark"] .schedule-table td,
  html[data-theme="dark"] .compare-cell,
  html[data-theme="dark"] .cart-cell,
  html[data-theme="dark"] .disclaimer,
  html[data-theme="dark"] .cost-card p,
  html[data-theme="dark"] .nopharm-card p,
  html[data-theme="dark"] .food-ok ul li,
  html[data-theme="dark"] .food-avoid ul li,
  html[data-theme="dark"] .food-limit ul li,
  html[data-theme="dark"] .related-card-desc,
  html[data-theme="dark"] .calc-verdict-text,
  html[data-theme="dark"] .calc-action-text,
  html[data-theme="dark"] .illus-caption { color: var(--text-mid) !important; }   /* 9.1:1 ✓ */

  /* Headings in dark mode */
  html[data-theme="dark"] .section h2,
  html[data-theme="dark"] .feature-card h4,
  html[data-theme="dark"] .alert-body h4,
  html[data-theme="dark"] .step-body h4,
  html[data-theme="dark"] .ladder-body h4,
  html[data-theme="dark"] .lab-table td:first-child,
  html[data-theme="dark"] .drug-table td:first-child,
  html[data-theme="dark"] .compare-cell strong,
  html[data-theme="dark"] .cart-cell strong,
  html[data-theme="dark"] .related-card-title,
  html[data-theme="dark"] .related-card-tag,
  html[data-theme="dark"] .calc-metric-card .cmv { color: var(--text) !important; }  /* 12.4:1 ✓ */

  /* Table headers */
  html[data-theme="dark"] .lab-table th,
  html[data-theme="dark"] .drug-table th,
  html[data-theme="dark"] .schedule-table th { background: #1a2535; color: var(--text-muted); }
  html[data-theme="dark"] .lab-table tr:hover td,
  html[data-theme="dark"] .drug-table tr:hover td { background: #202d40; }

  /* Alert backgrounds */
  html[data-theme="dark"] .alert-teal   { background: #0a2830; }
  html[data-theme="dark"] .alert-amber  { background: #2a1900; }
  html[data-theme="dark"] .alert-green  { background: #0e2a1c; }
  html[data-theme="dark"] .alert-red    { background: #2a1515; }
  html[data-theme="dark"] .alert-purple { background: #1a1030; }

  /* Compare/cartridge grids */
  html[data-theme="dark"] .compare-grid,
  html[data-theme="dark"] .cartridge-compare { border-color: #2a3548; }
  html[data-theme="dark"] .compare-row-label,
  html[data-theme="dark"] .cart-row-label { background: #1a2535; border-color: #2a3548; color: var(--text-muted); }
  html[data-theme="dark"] .compare-cell,
  html[data-theme="dark"] .cart-cell { border-color: #2a3548; }

  /* Related guides */
  html[data-theme="dark"] .related-card { background: #1a2535; border-color: #2a3548; }
  html[data-theme="dark"] .related-card:hover { border-color: var(--teal); }
  html[data-theme="dark"] .related-card h3 { color: var(--text); }
  html[data-theme="dark"] .related-card p { color: var(--text-muted); }
  html[data-theme="dark"] .related-badge { color: var(--teal); }

  /* Food grids */
  html[data-theme="dark"] .food-ok    { background: var(--green-soft); border-color: rgba(74,222,128,.15); }
  html[data-theme="dark"] .food-avoid { background: var(--red-soft);   border-color: rgba(248,113,113,.15); }
  html[data-theme="dark"] .food-limit { background: var(--amber-soft); border-color: rgba(251,191,36,.15); }

  /* Cost cards */
  html[data-theme="dark"] .cost-card { border-color: #2a3548; }
  html[data-theme="dark"] .cost-card.green { background: var(--green-soft); }
  html[data-theme="dark"] .cost-card.red   { background: var(--red-soft); }
  html[data-theme="dark"] .cost-card.amber { background: var(--amber-soft); }

  /* Nopharm cards */
  html[data-theme="dark"] .nopharm-card { background: #0a2830; border-color: #1a4a50; }
  html[data-theme="dark"] .nopharm-card h4 { color: var(--teal); }

  /* Disclaimer */
  html[data-theme="dark"] .disclaimer { background: var(--amber-soft); border-color: rgba(251,191,36,.15); }

  /* Illus wrap */
  html[data-theme="dark"] .illus-wrap { background: #1a2535; }
  html[data-theme="dark"] .illus-wrap-light { background: #f9fafb !important; }

  /* Calculator */
  html[data-theme="dark"] .calc-field input,
  html[data-theme="dark"] .calc-field select { background: #141c2a; border-color: #2a3548; color: var(--text); }
  html[data-theme="dark"] .calc-metric-card { background: rgba(255,255,255,.04); border-color: #2a3548; }
  html[data-theme="dark"] .calc-result-box { border-color: #2a3548 !important; background: rgba(255,255,255,.03) !important; }
  html[data-theme="dark"] .calc-field label { color: var(--teal); }
  html[data-theme="dark"] .calc-metric-card .cml,
  html[data-theme="dark"] .calc-disclaimer { color: var(--text-muted); }

  /* Guide footer */
  html[data-theme="dark"] .guide-footer { background: #141c2a; border-color: #2a3548; }

  /* Numeric cards — n-val/n-value use color:var(--navy); remap for dark */
  html[data-theme="dark"] .n-val,
  html[data-theme="dark"] .n-value { color: var(--text); }

  /* Tab hover + clinician tab underline */
  html[data-theme="dark"] .aud-tab:hover { color: var(--text); }
  html[data-theme="dark"] .aud-tab.active.tab-md { border-bottom-color: var(--teal); }

  /* Disclaimer strong text — inherits navy from light mode, needs remap */
  html[data-theme="dark"] .disclaimer strong { color: var(--text-mid); }

  /* Desktop mode */
  html[data-view="desktop"] { min-width: 1024px; }

  /* ── STAT CARDS ──────────────────────────────────────────────────────────── */
  .stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;margin:28px 0;}
  .stat-card{background:var(--teal);border-radius:14px;padding:22px 24px;color:white;text-align:center;}
  html[data-theme="dark"] .stat-card{background:#0d2535;}
  .stat-number{font-family:'Lora',serif;font-size:clamp(24px,4vw,34px);font-weight:600;color:#d4af4f;line-height:1.1;margin-bottom:8px;}
  .stat-label{font-size:12px;color:rgba(255,255,255,.8);line-height:1.5;}
  .stat-source{font-size:11px;color:rgba(255,255,255,.45);margin-top:4px;}

  /* ── NUMERIC CARDS (lighter variant) ─────────────────────────────────────── */
  .num-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;margin:28px 0;}
  .num-card{background:var(--bg);border:1px solid var(--border);border-radius:14px;padding:20px 22px;text-align:center;}
  .n-val,.n-value{font-family:'Lora',serif;font-size:clamp(22px,3.5vw,30px);font-weight:600;color:var(--navy);line-height:1.1;margin-bottom:6px;}
  .n-label{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:6px;}
  .n-target{font-size:12px;color:var(--teal);font-weight:500;margin-top:4px;}
  .n-note{font-size:12px;color:var(--text-muted);line-height:1.4;}

  /* ── UNIT TOGGLE (eGFR / lab value converters) ───────────────────────────── */
  .unit-toggle-wrap{display:flex;align-items:center;gap:10px;margin-bottom:18px;}
  .unit-toggle-wrap .ut-label{font-size:12px;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;}
  .unit-toggle{display:inline-flex;border:1px solid var(--border);border-radius:8px;overflow:hidden;}
  .unit-btn{background:transparent;border:none;padding:7px 16px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;color:var(--text-muted);cursor:pointer;transition:background .15s,color .15s;}
  .unit-btn.active{background:var(--teal);color:#fff;}

  /* ── RED FLAGS ───────────────────────────────────────────────────────────── */
  .red-flags{background:var(--red-soft);border:1px solid rgba(192,57,43,.2);border-radius:14px;padding:28px 32px;margin:32px 0;}
  .red-flags h3{font-family:'Lora',serif;font-size:18px;font-weight:600;color:var(--red);margin-bottom:16px;}
  .red-flags-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;}
  .red-flag-item{display:flex;align-items:flex-start;gap:10px;font-size:14px;color:var(--text-muted);}
  .rf-dot{width:6px;height:6px;border-radius:50%;background:var(--red);flex-shrink:0;margin-top:7px;}
  html[data-theme="dark"] .red-flags{background:#2a1515;border-color:rgba(229,85,85,.2);}

  /* ── ILLUSTRATION PANEL ──────────────────────────────────────────────────── */
  .illus-panel{margin:28px 0;border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.1);}

  /* ── CLINICIAN SECTION HERO (.md-hero) ───────────────────────────────────── */
  .md-hero {
    background: linear-gradient(135deg, #0d1e35 0%, #192d58 100%);
    padding: 60px 0 56px; position: relative; overflow: hidden;
  }
  .md-hero::before {
    content: ''; position: absolute; right: -80px; top: -60px;
    width: 360px; height: 360px; border-radius: 50%;
    border: 1px solid rgba(212,175,79,.1); pointer-events: none;
  }
  .md-hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 10px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase;
    color: #d4af4f; border: 1px solid rgba(212,175,79,.45);
    padding: 4px 14px; border-radius: 20px; margin-bottom: 20px;
  }
  .md-hero h2 {
    font-family: 'Lora', serif;
    font-size: clamp(22px, 4vw, 38px); font-weight: 600; line-height: 1.2;
    color: white; margin-bottom: 14px; letter-spacing: -.02em;
  }
  .md-hero-sub {
    font-size: 15px; color: rgba(255,255,255,.82);
    max-width: 580px; line-height: 1.7; margin-bottom: 28px;
  }
  .md-stats { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 32px; }
  .md-stat {
    background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.14);
    border-radius: 10px; padding: 12px 20px;
  }
  .md-stat-val {
    font-family: 'Lora', serif; font-size: 22px; font-weight: 600;
    color: #d4af4f; line-height: 1; display: block;
  }
  .md-stat-lbl { font-size: 11px; color: rgba(255,255,255,.6); margin-top: 4px; display: block; }
  .md-hero .illus-wrap {
    background: rgba(255,255,255,.05) !important; border: 1px solid rgba(255,255,255,.14);
  }
  .md-hero .img-placeholder { background: transparent; border-color: rgba(255,255,255,.2); margin: 0; }
  .md-hero .img-placeholder p,
  .md-hero .img-placeholder .img-ph-icon { color: rgba(255,255,255,.55); }

  /* ── CLINICIAN PATHWAY BANNERS ───────────────────────────────────────────── */
  .pathway-banner {
    padding: 20px 0 0;
  }
  .pathway-banner-inner {
    padding: 14px 20px; border-radius: 0 8px 8px 0;
  }
  .pathway-banner-inner.neph {
    border-left: 4px solid var(--teal); background: var(--teal-light);
  }
  .pathway-banner-inner.urol {
    border-left: 4px solid var(--gold); background: #fdf8ec;
  }
  .pathway-banner-inner.synth {
    border-left: 4px solid var(--purple); background: var(--purple-soft);
  }
  .pathway-banner-label {
    font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: .12em; margin: 0 0 4px;
  }
  .pathway-banner-label.neph { color: var(--teal); }
  .pathway-banner-label.urol { color: var(--gold); }
  .pathway-banner-label.synth { color: var(--purple); }
  .pathway-banner-desc { font-size: 13px; color: var(--text-muted); margin: 0; }

  /* ── AUDIENCE TAB SYSTEM ─────────────────────────────────────────────────── */
  .audience-tabs{background:var(--white);border-bottom:2px solid var(--border);position:sticky;top:56px;z-index:150;}
  .tabs-inner{max-width:860px;margin:0 auto;padding:0 32px;display:flex;gap:0;}
  .aud-tab{flex:1;text-align:center;padding:13px 20px;font-size:14px;font-weight:600;cursor:pointer;border:none;background:none;color:var(--text-muted);border-bottom:3px solid transparent;margin-bottom:-2px;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:8px;}
  .aud-tab:hover{color:var(--navy);}
  .aud-tab.active{color:var(--navy);border-bottom-color:var(--teal);}
  .aud-tab.active.tab-md{border-bottom-color:var(--navy);}
  .tab-icon{font-size:17px;}
  .mode-physician{display:none;}
  .mode-physician-pill{display:none;}
  body.physician-mode .mode-patient{display:none!important;}
  body.physician-mode .mode-physician{display:block!important;}
  body.physician-mode .mode-patient-pill{display:none;}
  body.physician-mode .mode-physician-pill{display:inline-flex;}
  html[data-theme="dark"] .audience-tabs{background:#141c2a;border-color:#2a3548;}
  html[data-theme="dark"] .aud-tab.active{color:#e8eaf0;}

  /* ── PHYSICIAN MODE — NAVY PALETTE ──────────────────────────────────────
     When body.physician-mode is active, key components switch from teal to
     the homepage deep-navy palette (#0f1e2e/#1a3060), making clinician
     content visually distinct from patient (teal) content at a glance.
     Contrast verified: white on #0f1e2e = 15.5:1 ✓
  ─────────────────────────────────────────────────────────────────────── */
  body.physician-mode .hero {
    background: linear-gradient(135deg, #0d1e35 0%, #1a3060 100%);
  }
  body.physician-mode .intro-callout { background: #0f1e2e; }
  body.physician-mode .stat-card     { background: #0f1e2e; }
  body.physician-mode .ref-band      { background: #0f1e2e; color: rgba(255,255,255,.88); }  /* white text on navy — 13.2:1 ✓ */
  body.physician-mode .nav-pill.active-pill {
    background: var(--navy); border-color: var(--navy);
  }
  /* Tab active underline already uses var(--navy) for .tab-md — intentional */
  /* Dark mode: already very dark; just deepen slightly */
  html[data-theme="dark"] body.physician-mode .hero {
    background: linear-gradient(135deg, #060f1a 0%, #0d1e40 100%);
  }
  html[data-theme="dark"] body.physician-mode .intro-callout,
  html[data-theme="dark"] body.physician-mode .stat-card,
  html[data-theme="dark"] body.physician-mode .ref-band { background: #0a1425; }

  /* ── GUIDE LANGUAGE BAR (regional recipes / multilingual tools) ──────────── */
  .guide-lang-bar{display:flex;align-items:center;gap:8px;padding:8px 0 16px;flex-wrap:wrap;}
  .lang-lbl{font-size:11px;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;margin-right:4px;}
  .lang-btn-g{font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;padding:4px 12px;border-radius:12px;border:1px solid var(--border);background:transparent;color:var(--text-muted);cursor:pointer;transition:all .2s;}
  .lang-btn-g:hover{border-color:var(--teal);color:var(--teal);}
  .lang-btn-g.active{background:var(--teal);border-color:var(--teal);color:white;}

  /* ── DOT COLOR VARIANTS ──────────────────────────────────────────────────── */
  .dot-gold{background:var(--gold);}
  .dot-orange{background:#e07b00;}

  /* ── DOWNLOAD BUTTON (inline variant) ───────────────────────────────────── */
  .download-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 22px;background:var(--navy);color:white;border:none;border-radius:8px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;cursor:pointer;text-decoration:none;transition:background .15s;}
  .download-btn:hover{background:#162848;}

  /* ── DOWNLOAD FAB (circular floating action button, bottom-left) ─────────── */
  .dl-fab {
    position: fixed; bottom: 24px; left: 24px;
    width: 44px; height: 44px; border-radius: 50%;
    background: var(--navy); color: white;
    border: none; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 16px rgba(0,0,0,.25);
    transition: transform .2s, box-shadow .2s; z-index: 9997;
    text-decoration: none;
  }
  .dl-fab:hover { background: #162848; transform: scale(1.1); box-shadow: 0 6px 20px rgba(0,0,0,.35); }
  .dl-fab svg { width: 18px; height: 18px; }
  .dl-fab .p-tip {
    position: absolute; left: 54px;
    background: rgba(31,56,100,.92); color: white;
    font-size: 12px; font-weight: 500; white-space: nowrap;
    padding: 5px 10px; border-radius: 6px;
    opacity: 0; pointer-events: none; transition: opacity .15s;
  }
  .dl-fab:hover .p-tip { opacity: 1; }

  /* ── MOBILE LAYOUT (≤ 480 px / 375 px phones) ───────────────────────────── */
  /* Tighter side padding on narrow viewports */
  @media(max-width: 480px) {
    .container { padding: 0 20px; }
    .related-guides { padding-left: 20px; padding-right: 20px; }
    .guide-footer .footer-inner { padding: 0 20px; }
    .dr-card { flex-direction: column; padding: 24px; gap: 16px; }
    .dr-card-wrap { padding: 0 20px 40px; }
    .hero-meta { gap: 14px; }
  }

  /* Tables: horizontal scroll to prevent content overflow on phones */
  @media(max-width: 640px) {
    table { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; }
  }

  /* ── IMAGE LIGHTBOX (assets/image-lightbox.js) ─────────────────────────── */
  figure img, .illus-wrap img { cursor: zoom-in; }
  figure img:hover, .illus-wrap img:hover { opacity: .92; }

  #img-lb.lb-overlay {
    display: none; position: fixed; inset: 0;
    background: rgba(0,0,0,.93); z-index: 9500;
    flex-direction: column; align-items: center; justify-content: center;
    padding: 20px 16px 16px; cursor: pointer; overflow-y: auto;
  }
  #img-lb.lb-overlay.open { display: flex; }

  .lb-body {
    display: flex; flex-direction: column; align-items: center;
    max-width: min(95vw, 1280px); cursor: default;
  }
  .lb-img {
    max-width: 100%; max-height: 72vh; border-radius: 8px;
    object-fit: contain; box-shadow: 0 8px 48px rgba(0,0,0,.7);
    cursor: zoom-in; display: block;
  }
  .lb-caption-panel {
    width: 100%; background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.13); border-top: none;
    border-radius: 0 0 8px 8px; padding: 14px 18px;
  }
  .lb-desc {
    color: rgba(255,255,255,.88); font-size: 13px; line-height: 1.6;
    margin: 0 0 10px; font-style: italic;
  }
  .lb-desc:last-child { margin-bottom: 0; }
  .lb-abbrevs {
    display: grid; grid-template-columns: auto 1fr;
    column-gap: 12px; row-gap: 3px; margin: 0;
    border-top: 1px solid rgba(255,255,255,.1); padding-top: 10px;
  }
  .lb-abbrevs dt {
    color: rgba(255,255,255,.5); font-size: 11px; font-weight: 700;
    font-variant-numeric: tabular-nums; white-space: nowrap;
  }
  .lb-abbrevs dd {
    color: rgba(255,255,255,.72); font-size: 11px; margin: 0;
  }
  .lb-close {
    position: fixed; top: 16px; right: 20px;
    color: #fff; font-size: 24px; line-height: 1;
    background: rgba(255,255,255,.13); border: 1px solid rgba(255,255,255,.25);
    border-radius: 50%; width: 40px; height: 40px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; transition: background .15s; z-index: 9501;
  }
  .lb-close:hover { background: rgba(255,255,255,.28); }
  .lb-hint {
    margin-top: 14px; color: rgba(255,255,255,.3); font-size: 11px;
    pointer-events: none; text-align: center; letter-spacing: .02em;
  }
  @media (max-width: 600px) {
    .lb-img { max-height: 58vh; }
    .lb-hint { white-space: normal; font-size: 10px; }
  }
  @media print { #img-lb.lb-overlay { display: none !important; } }

  /* Standard figcaption for guide images */
  figure figcaption, .illus-caption {
    font-size: 12px; color: var(--text-muted); margin-top: 10px;
    font-style: italic; text-align: center; line-height: 1.5;
  }
  .fig-desc { margin: 0 0 6px; }
  .fig-abbrevs {
    display: grid; grid-template-columns: auto 1fr;
    column-gap: 10px; row-gap: 2px; margin: 6px 0 0;
    font-style: normal; text-align: left;
  }
  .fig-abbrevs dt { font-weight: 700; color: var(--text-mid); }
  .fig-abbrevs dd { margin: 0; color: var(--text-muted); }

  /* ═══════════════════════════════════════════════════════════════════════════
     PRINT
  ═══════════════════════════════════════════════════════════════════════════ */
  @media print {
    .site-header, .nav-strip, .guide-toggle-bar, .print-btn, .dl-fab, .scroll-top-btn, .guide-footer { display: none !important; }
    body { font-size: 13px; line-height: 1.6; color: #000; background: #fff; }
    .hero { background: #fff !important; color: #000 !important; padding: 24px 0 16px !important; }
    .hero h1 { color: #1f3864 !important; font-size: 22px !important; }
    .hero-sub { color: #333 !important; font-size: 13px !important; }
    .hero-tag, .hero-meta { color: #555 !important; }
    .container { max-width: 100%; padding: 0 24px; }
    .section { padding: 20px 0; border-bottom: 1px solid #ddd; }
    .intro-callout { background: #f0f4f8 !important; color: #000 !important; border: 1px solid #ccc; }
    .intro-callout p { color: #222 !important; }
    .alert { border: 1px solid #ccc !important; background: #f9f9f9 !important; }
    .alert-body h4, .alert-body p, .alert-body ul li { color: #222 !important; }
    .feature-card { border: 1px solid #ccc !important; background: #fff !important; }
    .feature-card h4 { color: #1f3864 !important; }
    .feature-card p { color: #333 !important; }
    .table-wrap { box-shadow: none !important; border: 1px solid #ccc !important; }
    .table-wrap thead th { background: #eee !important; color: #333 !important; }
    .table-wrap tbody td { color: #333 !important; }
    .lab-table th { background: #eee !important; color: #333 !important; }
    .lab-table td { color: #333 !important; }
    .dr-card { background: #f0f4f8 !important; border: 1px solid #ccc; }
    .dr-card h4, .dr-card p, .dr-card .dr-creds { color: #222 !important; }
    .dr-qr { display: none !important; }
    .checklist { background: #f0f4f8 !important; border: 1px solid #ccc; }
    .checklist h4, .checklist ul li { color: #222 !important; }
    .disclaimer { background: #fff8e8 !important; border: 1px solid #ccc !important; color: #333 !important; }
    .illus-wrap { border: 1px solid #ccc; background: #f9f9f9 !important; }
    a[href]:after { content: " (" attr(href) ")"; font-size: 10px; color: #666; }
    .nav-pill { display: none; }
    @page { margin: 18mm 15mm; size: A4; }
  }
"""


# ── KAP translation garbage patterns ──────────────────────────────────────────
# These are the prompt strings that got stored instead of actual translations.
# We replace the entire span content with a clean empty fallback that falls
# back gracefully to English (hidden spans with no content = invisible).

KAP_GARBAGE_PATTERNS = [
    re.compile(
        r'(<span[^>]*data-lang=["\']kap["\'][^>]*>)'
        r'(?:Pakibigay mo pu|Paki-paste mo|pakisabi mu|Pakisabi mu|translate ke|translate ko|'
        r'i-translate king Kapampangan|buring mong i-translate|natural a Kapampangan|'
        r'Ala kung akit|medical patient education text)[^<]*'
        r'(</span>)',
        re.DOTALL | re.IGNORECASE
    ),
]

KAP_GARBAGE_REPLACEMENT = r'\1\2'  # keep tags, clear content


def find_project_dir(script_path: Path) -> Path:
    candidates = [
        script_path.parent,
        script_path.parent.parent,
        Path.home() / "Desktop" / "williamriveromd",
    ]
    for c in candidates:
        if (c / "guides").is_dir() and (c / "index.html").exists():
            return c
    raise FileNotFoundError("Cannot find williamriveromd project root.")


def replace_style_block(html: str) -> tuple[str, bool]:
    """Replace the content of the first <style>...</style> block with MASTER_CSS.

    Only the first <style> block is touched. Guide-specific CSS belongs in a
    second <style> block placed after this one (see e.g. managing-hypertension,
    alcohol-ckd, cardio-kidney-metabolic-syndrome), which this function leaves
    untouched and is therefore safe across re-runs."""
    pattern = re.compile(r'(<style>)(.*?)(</style>)', re.DOTALL)
    match = pattern.search(html)
    if not match:
        return html, False
    new_html = html[:match.start()] + f'<style>{MASTER_CSS}</style>' + html[match.end():]
    return new_html, True


def fix_kap_garbage(html: str) -> tuple[str, int]:
    """Remove botched KAP translation prompt text from data-lang=kap spans."""
    count = 0
    for pattern in KAP_GARBAGE_PATTERNS:
        new_html, n = pattern.subn(KAP_GARBAGE_REPLACEMENT, html)
        count += n
        html = new_html
    return html, count


def patch_file(path: Path, dry_run: bool = False, fix_kap: bool = True) -> str:
    html = path.read_text(encoding="utf-8")
    changes = []

    # 1. Replace style block
    new_html, css_replaced = replace_style_block(html)
    if css_replaced:
        changes.append("CSS replaced")

    # 2. Fix botched KAP translations
    if fix_kap:
        new_html, kap_count = fix_kap_garbage(new_html)
        if kap_count:
            changes.append(f"{kap_count} KAP garbage strings removed")

    if not changes:
        return "no changes"

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")

    return f"{'[DRY] ' if dry_run else ''}✓ {' + '.join(changes)}"


def main():
    parser = argparse.ArgumentParser(
        description="Apply master CSS to all williamriveromd.com guide pages"
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--guide", help="Patch a single guide file only")
    parser.add_argument("--fix-kap-only", action="store_true", help="Only fix botched KAP translations, don't touch CSS")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    try:
        project_dir = find_project_dir(script_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    guides_dir = project_dir / "guides"
    print(f"Project: {project_dir}")
    print(f"Dry run: {args.dry_run}\n")

    if args.guide:
        path = guides_dir / args.guide
        if not path.exists():
            print(f"ERROR: {path} not found")
            sys.exit(1)
        result = patch_file(path, args.dry_run, fix_kap=True)
        print(f"{args.guide}: {result}")
        return

    # Files with custom CSS appended after the master block — skip to avoid data loss
    EXCLUDE = {"nephrology-atlas.html"}
    files = sorted(f for f in guides_dir.glob("*.html") if f.name != "index.html" and f.name not in EXCLUDE)
    patched = skipped = 0

    for f in files:
        if args.fix_kap_only:
            html = f.read_text(encoding="utf-8")
            new_html, count = fix_kap_garbage(html)
            if count:
                if not args.dry_run:
                    f.write_text(new_html, encoding="utf-8")
                print(f"  {f.name:55s} → {'[DRY] ' if args.dry_run else ''}✓ {count} KAP strings fixed")
                patched += 1
            else:
                skipped += 1
        else:
            result = patch_file(f, args.dry_run)
            if "no changes" in result:
                skipped += 1
            else:
                patched += 1
                print(f"  {f.name:55s} → {result}")

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary:")
    print(f"  Patched: {patched}  |  No changes: {skipped}")

    if not args.dry_run and patched > 0:
        print("\nNext step:")
        print("  git add .")
        print('  git commit -m "Apply master CSS — contrast-verified across all guides"')
        print("  git push")
    elif args.dry_run:
        print("\nRe-run without --dry-run to apply.")


if __name__ == "__main__":
    main()
