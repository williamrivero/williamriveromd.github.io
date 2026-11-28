# -*- coding: utf-8 -*-
"""Self-assessment banks for the Dialysis Team Resuscitation Lab: 10 items per module (130). Every item is
(stem, [4 options], correct index, why). The correct option is written first and quizutil.balance() spreads the keys evenly
across A to D at build time."""
import importlib.util as _u
from pathlib import Path as _P


def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m


QUIZ = {}
for _f in sorted(_P(__file__).resolve().parent.glob("quiz_[0-9][0-9].py")):
    QUIZ.update(_ld(_f.stem).QUIZ)
