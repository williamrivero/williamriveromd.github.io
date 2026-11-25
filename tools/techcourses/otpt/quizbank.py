# -*- coding: utf-8 -*-
"""Self-assessment banks for the Occupational and Physical Therapist track: 10 items per module.
Items 1-5: the keyed handoff items (src/question-bank.json, v1: three formative and two final-designated per module),
with the handoff rationale as the explanation. Items 6-10: new application items written for blueprint v2 (quiz_new.py).
The end-of-course examination draws one item per module from these banks (generate_tech_courses.py, exam_stratify)."""
import html as _html
import importlib.util as _u
import json as _json
from pathlib import Path as _P

_HERE = _P(__file__).resolve().parent


def _e(s):
    return _html.escape(s, quote=False).replace("'", "&rsquo;")


def _load_new():
    s = _u.spec_from_file_location("otpt_quiz_new", _HERE / "quiz_new.py")
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return m.QUIZ_NEW


_BANK = _json.loads((_HERE / "src" / "question-bank.json").read_text(encoding="utf-8"))
_NEW = _load_new()

QUIZ = {}
for _q in _BANK:
    _mid = _q["module_id"][1:]
    QUIZ.setdefault(_mid, []).append((_e(_q["stem"]), [_e(o) for o in _q["options"]], _q["answer_index"],
                                      "Best answer: " + _e(_q["rationale"])))
for _mid, _items in _NEW.items():
    QUIZ.setdefault(_mid, []).extend(_items)
