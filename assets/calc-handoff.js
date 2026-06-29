/* ──────────────────────────────────────────────────────────────────
   Combined-calculator input handoff — williamriveromd.com
   ──────────────────────────────────────────────────────────────────
   Carries the common patient inputs across the whole calculator
   library so entering them once feeds every related calculator:
     • age, sex, eGFR, height (cm), weight (kg), serum creatinine (mg/dL)

   How it works
   - Fields are found by the library's id-suffix convention:
       <prefix>-age, -sex, -egfr, -height|-ht, -weight, -scr|-creat
   - Values are stored canonically in localStorage ('wgmr-rx-patient').
   - On load, ONLY EMPTY fields are prefilled — a user's own entry is
     never overwritten — and the calculator is recomputed by firing
     input/change events.
   - Weight & creatinine are UNIT-GUARDED: they are read and written
     only when the page is in its default unit (no active
     <prefix>-wbtn-lb / <prefix>-cbtn-si toggle), so a kg value is never
     pushed into a lb field, or mg/dL into µmol/L.
   - Self-activating and harmless: a page with none of these inputs
     simply does nothing. Vanilla JS, no dependencies.
   ────────────────────────────────────────────────────────────────── */
(function () {
  var KEY = 'wgmr-rx-patient';

  function read() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function write(o) { try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function one(sel) { return document.querySelector(sel); }
  function all(sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); }
  function val(e) { return e ? String(e.value).trim() : ''; }
  function active(id) { var b = document.getElementById(id); return !!(b && b.classList.contains('active')); }
  function prefixOf(id, suffix) { return id.slice(0, id.length - suffix.length); }

  // Default unit = no toggle present, or the non-default toggle is not active.
  function weightIsKg(prefix) { return !document.getElementById(prefix + '-wbtn-lb') || !active(prefix + '-wbtn-lb'); }
  function scrIsMgdl(prefix) { return !document.getElementById(prefix + '-cbtn-si') || !active(prefix + '-cbtn-si'); }

  function scrSuffix(id) { return id.slice(-6) === '-creat' ? '-creat' : '-scr'; }

  function fill(e, v) {
    if (e && !val(e) && v != null && v !== '') {
      e.value = v;
      e.dispatchEvent(new Event('input', { bubbles: true }));
      e.dispatchEvent(new Event('change', { bubbles: true }));
      return true;
    }
    return false;
  }

  // ── Prefill empty fields from the stored patient (before binding save) ──────
  var s = read();
  var filled = 0;
  all('input[id$="-age"]').forEach(function (e) { if (fill(e, s.age)) filled++; });
  all('[id$="-sex"]').forEach(function (e) { if (fill(e, s.sex)) filled++; });
  all('input[id$="-egfr"]').forEach(function (e) { if (fill(e, s.egfr)) filled++; });
  all('input[id$="-height"], input[id$="-ht"]').forEach(function (e) { if (fill(e, s.heightCm)) filled++; });
  all('input[id$="-weight"]').forEach(function (e) {
    if (weightIsKg(prefixOf(e.id, '-weight')) && fill(e, s.weightKg)) filled++;
  });
  all('input[id$="-scr"], input[id$="-creat"]').forEach(function (e) {
    if (scrIsMgdl(prefixOf(e.id, scrSuffix(e.id))) && fill(e, s.scrMgdl)) filled++;
  });

  // ── Save canonical values back whenever a shared field changes ──────────────
  function save() {
    var st = read();
    var a = one('input[id$="-age"]'); if (a && val(a)) st.age = val(a);
    var x = one('[id$="-sex"]'); if (x && val(x)) st.sex = val(x);
    var g = one('input[id$="-egfr"]'); if (g && val(g)) st.egfr = val(g);
    var h = one('input[id$="-height"], input[id$="-ht"]'); if (h && val(h)) st.heightCm = val(h);
    var w = one('input[id$="-weight"]');
    if (w && val(w) && weightIsKg(prefixOf(w.id, '-weight'))) st.weightKg = val(w);
    var c = one('input[id$="-scr"], input[id$="-creat"]');
    if (c && val(c) && scrIsMgdl(prefixOf(c.id, scrSuffix(c.id)))) st.scrMgdl = val(c);
    write(st);
  }
  ['-age', '-sex', '-egfr', '-height', '-ht', '-weight', '-scr', '-creat'].forEach(function (suf) {
    all('[id$="' + suf + '"]').forEach(function (e) {
      e.addEventListener('input', save);
      e.addEventListener('change', save);
    });
  });

  // ── Carry-over banner (only when something was actually prefilled) ──────────
  if (filled) {
    var wrap = one('.calc-wrap') || one('.calculator') || one('main') || document.body;
    if (wrap && !document.getElementById('rx-carry-note')) {
      var d = document.createElement('div');
      d.id = 'rx-carry-note';
      d.style.cssText = 'display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:600;' +
        'color:var(--teal,#1a6b72);background:var(--teal-light,#e1f5f0);' +
        'border:1px solid rgba(26,107,114,.25);border-radius:8px;padding:8px 12px;margin-bottom:16px;';
      d.textContent = '↺ Patient details carried over from a previous calculator — edit any field to update.';
      wrap.insertBefore(d, wrap.firstChild);
    }
  }
})();
