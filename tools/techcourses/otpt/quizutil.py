# -*- coding: utf-8 -*-
"""Quiz helper for the Renal Transplant Coordinator track.

balance(quiz) moves each keyed answer so the correct options are spread evenly across A to D.
It is deterministic (the same input always gives the same output), so page builds are stable.
Same signature as the MRO helper: list of (stem, [4 options], correct_index, why)."""


def balance(quiz):
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        if len(opts) != 4 or not 0 <= ans < 4:
            raise ValueError(f"Question {i + 1} needs four options and a key from 0 to 3: {stem[:60]}")
        target = (i * 3 + 1) % 4  # 1, 0, 3, 2, 1, 0 ... a fixed, even spread
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out
