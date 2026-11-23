# -*- coding: utf-8 -*-
"""Spreads the keyed answers of a question bank evenly across positions A to D, so that no letter is favored.
Deterministic: the same bank always gives the same order."""


def balance(quiz):
    out = []
    for i, (stem, options, answer, why) in enumerate(quiz):
        target = (i * 3 + 1) % 4          # 1, 0, 3, 2, 1, 0, ...
        opts = list(options)
        opts[answer], opts[target] = opts[target], opts[answer]
        out.append((stem, opts, target, why))
    return out
