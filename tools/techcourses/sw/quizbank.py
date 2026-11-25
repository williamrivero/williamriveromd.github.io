# -*- coding: utf-8 -*-
"""Self-assessment banks for the Renal Social Worker track: 10 items per module (200).
Items 1-4 per module adapt the handoff package's keyed items (question-bank.json v1.0.0); items 5-10 are new application
items written for blueprint v2. Every item is (stem, [4 options], correct index, why). The correct option is written first
and quizutil.balance() spreads the keys evenly across A to D at build time."""
import importlib.util as _u
from pathlib import Path as _P


def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m


QUIZ = {}
QUIZ.update(_ld("quiz_a").QUIZ)
QUIZ.update(_ld("quiz_b").QUIZ)
