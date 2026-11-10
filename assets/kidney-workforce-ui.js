/* kidney-workforce-ui.js — renalcarematters.com
 * Small browser helpers shared by the three workforce planner pages
 * (calc-kidney-care-fte-gap, calc-dialysis-shift-coverage, calc-referral-backlog-planner).
 * No storage, no network, no analytics: inputs stay in page memory. Exports are
 * generated locally and saved only when the user clicks a download button.
 */
(function (root) {
  'use strict';
  var UI = {};

  UI.$ = function (id) { return document.getElementById(id); };
  UI.esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  };
  UI.fmt = function (n, dp) {
    if (n === null || n === undefined || typeof n !== 'number' || !isFinite(n)) return '—';
    dp = dp === undefined ? 0 : dp;
    return n.toLocaleString('en-US', { minimumFractionDigits: dp, maximumFractionDigits: dp });
  };
  UI.stamp = function () {
    var d = new Date();
    function p(x) { return (x < 10 ? '0' : '') + x; }
    return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()) + ' ' + p(d.getHours()) + ':' + p(d.getMinutes());
  };
  UI.download = function (filename, text, mime) {
    var blob = new Blob([text], { type: mime || 'text/plain;charset=utf-8' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 400);
  };
  UI.announce = function (id, msg) { var el = UI.$(id); if (el) el.textContent = msg; };

  // Show inline errors next to fields (by data-field attribute) and in a summary list.
  UI.showErrors = function (container, errors) {
    document.querySelectorAll('[data-field]').forEach(function (el) {
      el.removeAttribute('aria-invalid');
      var d = el.getAttribute('aria-describedby');
      if (d && d.indexOf('err-') === 0) el.removeAttribute('aria-describedby');
    });
    document.querySelectorAll('.kwp-err').forEach(function (e) { e.remove(); });
    var box = UI.$(container);
    if (!box) return;
    if (!errors || !errors.length) { box.innerHTML = ''; box.hidden = true; return; }
    box.hidden = false;
    box.innerHTML = '<strong>Please check these inputs:</strong><ul>' + errors.map(function (e) {
      return '<li>' + UI.esc(e.message) + '</li>';
    }).join('') + '</ul>';
    errors.forEach(function (e, i) {
      var el = document.querySelector('[data-field="' + e.field + '"]');
      if (!el) return;
      el.setAttribute('aria-invalid', 'true');
      var msg = document.createElement('div');
      msg.className = 'kwp-err';
      msg.id = 'err-' + i;
      msg.textContent = e.message;
      el.setAttribute('aria-describedby', msg.id);
      el.insertAdjacentElement('afterend', msg);
    });
  };

  // Horizontal bar chart (SVG) for labelled values; returns markup string.
  UI.bars = function (items, unit) {
    if (!items.length) return '';
    var max = Math.max.apply(null, items.map(function (i) { return i.value; })) || 1;
    var rowH = 30, w = 640, labelW = 210, h = items.length * rowH + 10;
    var out = '<svg class="kwp-chart" viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="Bar chart; the same values are in the table below.">';
    items.forEach(function (it, i) {
      var y = 6 + i * rowH;
      var bw = Math.max(2, (w - labelW - 90) * it.value / max);
      out += '<text x="0" y="' + (y + 17) + '" class="kwp-ct">' + UI.esc(it.label.length > 30 ? it.label.slice(0, 29) + '…' : it.label) + '</text>';
      out += '<rect x="' + labelW + '" y="' + (y + 4) + '" width="' + bw + '" height="18" rx="4" class="' + (it.cls || 'kwp-bar') + '"></rect>';
      out += '<text x="' + (labelW + bw + 6) + '" y="' + (y + 17) + '" class="kwp-ct">' + UI.fmt(it.value, it.dp || 0) + (unit ? ' ' + unit : '') + '</text>';
    });
    return out + '</svg>';
  };

  // Line chart for one or two weekly series; returns markup string.
  UI.lines = function (seriesList) {
    var w = 640, h = 240, pl = 48, pr = 12, pt = 12, pb = 30;
    var n = 0, max = 1;
    seriesList.forEach(function (s) { n = Math.max(n, s.values.length - 1); s.values.forEach(function (v) { if (v > max) max = v; }); });
    if (n < 1) return '';
    function X(i) { return pl + (w - pl - pr) * i / n; }
    function Y(v) { return pt + (h - pt - pb) * (1 - v / max); }
    var out = '<svg class="kwp-chart" viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="Backlog by week; values are in the table below.">';
    for (var g = 0; g <= 4; g++) {
      var gv = max * g / 4, gy = Y(gv);
      out += '<line x1="' + pl + '" x2="' + (w - pr) + '" y1="' + gy + '" y2="' + gy + '" class="kwp-grid"/>';
      out += '<text x="' + (pl - 6) + '" y="' + (gy + 4) + '" text-anchor="end" class="kwp-ct">' + UI.fmt(gv) + '</text>';
    }
    [0, Math.round(n / 4), Math.round(n / 2), Math.round(3 * n / 4), n].forEach(function (t, k) {
      var anchor = k === 0 ? 'start' : (k === 4 ? 'end' : 'middle');
      out += '<text x="' + X(t) + '" y="' + (h - 8) + '" text-anchor="' + anchor + '" class="kwp-ct">wk ' + t + '</text>';
    });
    seriesList.forEach(function (s) {
      var d = s.values.map(function (v, i) { return (i ? 'L' : 'M') + X(i).toFixed(1) + ' ' + Y(v).toFixed(1); }).join(' ');
      out += '<path d="' + d + '" class="' + s.cls + '" fill="none"/>';
    });
    return out + '</svg>';
  };

  root.KWPUI = UI;
})(typeof self !== 'undefined' ? self : this);
