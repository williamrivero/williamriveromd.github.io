# -*- coding: utf-8 -*-
"""Helpers for the image plan data files (image_plan_hd.py, image_plan_water.py, image_plan_biomed.py)."""


def F(letter, title, slug, kind, section, job, truth, labels, negatives, alt, core=True, canvas=None):
    """One teaching figure. kind: aid | flow | card | circuit. labels: verbatim, separated by ' | '."""
    return {"letter": letter, "title": title, "slug": slug, "kind": kind, "section": section, "job": job, "truth": truth,
            "labels": [x.strip() for x in labels.split("|")], "negatives": [x.strip() for x in negatives.split(";")],
            "alt": alt, "core": core, "canvas": canvas or ("portrait" if kind == "flow" and False else "landscape")}


def M(mid, title, slug, origin, teach, case, skills, hero_scene, figs):
    """One module of an expanded track: curriculum brief + hero scene + figures."""
    return {"id": mid, "title": title, "slug": slug, "origin": origin, "teach": teach, "case": case, "skills": skills,
            "hero": hero_scene, "figs": figs}
