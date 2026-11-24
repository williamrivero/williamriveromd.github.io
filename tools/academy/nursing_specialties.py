"""Specialty subtrack cards shown on the Nephrology Nursing hub (academy/nephrology-nursing.html, #specialty).

generate_transplant_nurse.entry_blocks() renders these cards ahead of the Transplant Nurse card, so the
specialty section lists every Nephrology Nursing subtrack whichever generator last rewrote it.
Order follows the parent module each subtrack continues (Module 10 before Module 11)."""

CARDS = [
    {
        "href": "peritoneal-dialysis-nurse.html",
        "meta": "12 modules &middot; about 60 hours",
        "title": "Peritoneal Dialysis Nurse",
        "desc": ("Peritoneal dialysis program nursing, from physiology and home readiness to the catheter and exit site, CAPD and APD, "
                 "goal-directed monitoring, peritonitis, urgent problems, teaching, transitions and quality, with five skills stations. "
                 "Entry lesson: Module 10."),
    },
    {
        "href": "special-dialysis-nurse-roles.html",
        "meta": "By Role &middot; 14 modules &middot; about 111 hours",
        "title": "Special Dialysis Nurse Roles",
        "desc": ("For the nurse handed a portfolio: vascular access, infection prevention, educator and preceptor, patient education, "
                 "quality, safety and emergencies, care coordination, anemia, transplant liaison, records and PhilHealth, water and "
                 "equipment, and adequacy, with worked scenarios and a capstone."),
    },
]


def cards_html():
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from tile_img import tile
    return "".join(
        tile(f"""    <a class="nc-mod" href="{c['href']}">""", f"""      <span class="nc-mod-top"><span class="nc-mod-step">Specialty</span><span>{c['meta']}</span></span>
      <span class="nc-mod-title">{c['title']}</span>
      <span class="nc-mod-desc">{c['desc']}</span>""", c['href'].split('#')[0][:-5]) + "\n" for c in CARDS)
