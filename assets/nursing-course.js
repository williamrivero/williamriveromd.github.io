/* Nephrology Nursing & Hemodialysis course — self-assessment and optional
   on-device progress. Vanilla JS, no network requests: answers never leave
   the browser. Loaded with `defer` on the course hub and module pages. */
(function () {
  'use strict';
  var KEY = 'rcm-nursing-progress';

  function readStore() {
    try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; }
  }
  function writeStore(obj) {
    try { localStorage.setItem(KEY, JSON.stringify(obj)); return true; } catch (e) { return false; }
  }
  function clearStore() {
    try { localStorage.removeItem(KEY); } catch (e) {}
  }

  /* ── In-text citation links: open the References accordion on phones ── */
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[data-ref]');
    if (!a) return;
    if (document.querySelector('.rcm-rail')) return; // desktop rail handles #ref-N
    var acc = document.querySelector('details.ref-acc');
    if (!acc) return;
    var li = acc.querySelectorAll('ol > li')[parseInt(a.getAttribute('data-ref'), 10) - 1];
    if (!li) return;
    ev.preventDefault();
    acc.open = true;
    li.setAttribute('tabindex', '-1');
    li.scrollIntoView({ block: 'center' });
    li.focus({ preventScroll: true });
  });

  /* ── Self-assessment ─────────────────────────────────────────────────── */
  var form = document.getElementById('nc-quiz');
  if (form) initQuiz(form);

  function initQuiz(form) {
    var result = document.getElementById('nc-result');
    var retry = form.querySelector('[data-nc-retry]');
    var submit = form.querySelector('button[type="submit"]');
    var remember = document.getElementById('nc-remember');
    var newset = form.querySelector('[data-nc-newset]');
    /* The whole bank is in the page. Each load shows a random draw of
       data-draw questions, in random order, with the options shuffled. */
    var bank = Array.prototype.slice.call(form.querySelectorAll('fieldset.nc-q'));
    var drawN = Math.min(parseInt(form.getAttribute('data-draw'), 10) || bank.length, bank.length);
    var questions = [];
    function rand(n) {
      if (window.crypto && window.crypto.getRandomValues) {
        var a = new Uint32Array(1); window.crypto.getRandomValues(a); return a[0] % n;
      }
      return Math.floor(Math.random() * n);
    }
    function shuffle(arr) {
      for (var i = arr.length - 1; i > 0; i--) { var j = rand(i + 1); var t = arr[i]; arr[i] = arr[j]; arr[j] = t; }
      return arr;
    }
    function drawSet() {
      var previous = questions.slice();
      var pick = shuffle(bank.slice()).slice(0, drawN);
      if (form.hasAttribute('data-stratify')) {
        /* one question per data-group, groups in random order */
        var groups = {}, keys = [];
        bank.forEach(function (q) { var g = q.getAttribute('data-group') || ''; if (!groups[g]) { groups[g] = []; keys.push(g); } groups[g].push(q); });
        pick = shuffle(keys.map(function (g) { return groups[g][rand(groups[g].length)]; })).slice(0, drawN);
      }
      // a new set should not repeat the previous set exactly
      if (previous.length && bank.length > drawN &&
          pick.every(function (q) { return previous.indexOf(q) !== -1; })) {
        pick = shuffle(bank.slice()).slice(0, drawN);
      }
      var anchor = form.querySelector('.nc-remember');
      bank.forEach(function (q) {
        q.hidden = true;
        Array.prototype.forEach.call(q.querySelectorAll('input'), function (i) { i.disabled = true; i.checked = false; });
      });
      pick.forEach(function (q, idx) {
        q.hidden = false;
        q.classList.remove('nc-checked', 'nc-missing');
        shuffle(Array.prototype.slice.call(q.querySelectorAll('.nc-opt'))).forEach(function (opt) {
          opt.classList.remove('nc-opt-correct', 'nc-opt-chosen-wrong');
          var rat = opt.querySelector('.nc-rat'); if (rat) rat.hidden = true;
          var verdict = opt.querySelector('.nc-verdict'); if (verdict) verdict.textContent = '';
          q.appendChild(opt);
        });
        Array.prototype.forEach.call(q.querySelectorAll('input'), function (i) { i.disabled = false; });
        var qn = q.querySelector('.nc-qn');
        if (qn) qn.textContent = 'Question ' + (idx + 1) + ' of ' + pick.length;
        q.setAttribute('data-shown', String(idx + 1));
        if (anchor) form.insertBefore(q, anchor);
      });
      questions = pick;
    }
    drawSet();
    var store = readStore();
    if (remember && store && store.optin) remember.checked = true;

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var unanswered = questions.filter(function (q) { return !q.querySelector('input:checked'); });
      questions.forEach(function (q) { q.classList.remove('nc-missing'); });
      if (unanswered.length) {
        unanswered.forEach(function (q) { q.classList.add('nc-missing'); });
        var nums = unanswered.map(function (q) { return q.getAttribute('data-shown'); }).join(', ');
        result.className = 'nc-result nc-result-warn';
        result.textContent = 'Please answer every question before checking. Not yet answered: question ' + nums + '.';
        var first = unanswered[0].querySelector('input');
        if (first) first.focus();
        return;
      }
      var score = 0, critMissed = 0;
      questions.forEach(function (q) {
        var chosen = q.querySelector('input:checked');
        var right = chosen.getAttribute('data-correct') === '1';
        if (right) score++;
        else if (q.getAttribute('data-critical') === '1') critMissed++;
        q.classList.add('nc-checked');
        Array.prototype.forEach.call(q.querySelectorAll('.nc-opt'), function (opt) {
          var inp = opt.querySelector('input');
          var isCorrect = inp.getAttribute('data-correct') === '1';
          var verdict = opt.querySelector('.nc-verdict');
          opt.classList.toggle('nc-opt-correct', isCorrect);
          opt.classList.toggle('nc-opt-chosen-wrong', inp.checked && !isCorrect);
          if (verdict) {
            verdict.textContent = isCorrect
              ? (inp.checked ? 'Correct. You chose the best answer.' : 'This is the best answer.')
              : (inp.checked ? 'Your answer. Not the best answer.' : '');
          }
          var rat = opt.querySelector('.nc-rat');
          if (rat) rat.hidden = false;
          inp.disabled = true;
        });
      });
      var total = questions.length;
      result.className = 'nc-result nc-result-done';
      result.innerHTML = '';
      var strong = document.createElement('strong');
      strong.textContent = 'Self-assessment complete: ' + score + ' of ' + total + ' best answers.';
      var p = document.createElement('span');
      p.textContent = ' Read the rationale under every option, including the ones you did not choose. ' +
        'This score records self-study only; practice competencies are observed and signed off by a preceptor.';
      result.appendChild(strong); result.appendChild(p);
      var passMark = parseInt(form.getAttribute('data-pass'), 10);
      if (passMark) {
        var line = document.createElement('span');
        line.className = 'nc-verdict-line';
        var passed = score >= passMark;
        if (form.hasAttribute('data-critical-pass') && critMissed > 0) {
          passed = false;
          line.textContent = 'Not yet passed (' + score + ' of ' + total + '), because ' + critMissed + (critMissed === 1 ? ' safety-critical question was' : ' safety-critical questions were') +
            ' missed. A safety-critical answer must be right even when the total is high. Review that module, then try a new set.';
        } else
        line.textContent = passed
          ? 'Passed (' + score + ' of ' + total + '; pass mark ' + passMark + '). Your self-study is complete. Simulation and workplace competency are assessed separately.'
          : 'Not yet passed (' + score + ' of ' + total + '; pass mark ' + passMark + '). Review the modules for the questions you missed, then try a new set.';
        result.classList.add(passed ? 'nc-result-pass' : 'nc-result-fail');
        result.appendChild(line);
      }
      submit.hidden = true; retry.hidden = false;
      result.focus();
      if (remember && remember.checked) {
        var s = readStore() || { optin: true, modules: {} };
        s.optin = true; s.modules = s.modules || {};
        s.modules[form.getAttribute('data-module')] = { score: score, total: total, date: new Date().toISOString().slice(0, 10) };
        if (!writeStore(s)) {
          p.textContent += ' (Progress could not be saved in this browser.)';
        }
      }
    });

    retry.addEventListener('click', function () {
      form.reset();
      questions.forEach(function (q) {
        q.classList.remove('nc-checked', 'nc-missing');
        Array.prototype.forEach.call(q.querySelectorAll('.nc-opt'), function (opt) {
          opt.classList.remove('nc-opt-correct', 'nc-opt-chosen-wrong');
          var inp = opt.querySelector('input'); inp.disabled = false;
          var rat = opt.querySelector('.nc-rat'); if (rat) rat.hidden = true;
          var verdict = opt.querySelector('.nc-verdict'); if (verdict) verdict.textContent = '';
        });
      });
      var st = readStore();
      if (remember && st && st.optin) remember.checked = true;
      result.className = 'nc-result'; result.textContent = '';
      submit.hidden = false; retry.hidden = true;
      var first = questions[0] && questions[0].querySelector('input[type="radio"]');
      if (first) first.focus();
    });

    if (newset) {
      newset.addEventListener('click', function () {
        form.reset();
        drawSet();
        var st = readStore();
        if (remember && st && st.optin) remember.checked = true;
        result.className = 'nc-result';
        result.textContent = 'A new set of ' + questions.length + ' questions has been drawn from the bank.';
        submit.hidden = false; retry.hidden = true;
        var first = questions[0] && questions[0].querySelector('input[type="radio"]');
        if (first) first.focus();
      });
    }

    if (remember) {
      remember.addEventListener('change', function () {
        if (!remember.checked) { clearStore(); }
        else { var s = readStore() || { modules: {} }; s.optin = true; writeStore(s); }
      });
    }
  }

  /* ── Hub: show saved progress (only if the reader opted in) ─────────── */
  var hub = document.getElementById('nc-modules');
  if (hub) {
    var st = readStore();
    var bar = document.getElementById('nc-progress');
    var done = 0;
    if (st && st.optin && st.modules) {
      Array.prototype.forEach.call(hub.querySelectorAll('[data-module]'), function (card) {
        var m = st.modules[card.getAttribute('data-module')];
        var slot = card.querySelector('.nc-mod-status');
        if (m && slot) {
          done++;
          slot.textContent = 'Self-assessment done: ' + m.score + '/' + m.total + ' (' + m.date + ')';
          slot.classList.add('nc-mod-done');
        }
      });
    }
    if (bar) {
      if (st && st.optin) {
        bar.hidden = false;
        bar.querySelector('.nc-progress-text').textContent =
          done + ' of ' + hub.querySelectorAll('[data-module]').length + ' self-assessments recorded on this device.';
        var btn = bar.querySelector('button');
        btn.addEventListener('click', function () {
          clearStore();
          bar.querySelector('.nc-progress-text').textContent = 'Saved progress cleared from this device.';
          btn.hidden = true;
          Array.prototype.forEach.call(hub.querySelectorAll('.nc-mod-status'), function (s) {
            s.textContent = ''; s.classList.remove('nc-mod-done');
          });
        });
      }
    }
    /* Path selector */
    var buttons = document.querySelectorAll('[data-nc-path]');
    Array.prototype.forEach.call(buttons, function (b) {
      b.addEventListener('click', function () {
        var path = b.getAttribute('data-nc-path');
        Array.prototype.forEach.call(buttons, function (x) {
          x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
        });
        hub.setAttribute('data-path', path);
        var cards = Array.prototype.slice.call(hub.querySelectorAll('[data-module]'));
        cards.sort(function (a, c) {
          return parseInt(a.getAttribute('data-order-' + path), 10) - parseInt(c.getAttribute('data-order-' + path), 10);
        });
        cards.forEach(function (c, i) {
          hub.appendChild(c);
          var step = c.querySelector('.nc-mod-step');
          if (step) step.textContent = 'Step ' + (i + 1);
        });
        var note = document.getElementById('nc-path-note');
        if (note) note.textContent = b.getAttribute('data-note');
      });
    });
  }
})();
