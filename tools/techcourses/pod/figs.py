# -*- coding: utf-8 -*-
"""Figures made for the Physician on Duty track. key: (file in images/, alt text, default caption).
Until a file exists the page prints an HTML comment in its place, so pages build before the art is produced.
Existing site figures (kidneys, nephron, two_compartment, hd_week, code_readiness, ...) come from tools/techcourses/figs.py."""

FIGS = {
    "pod01_team": ("physician-on-duty-01-care-team.webp",
                   "A dialysis patient in a chair surrounded by the care team: nephrologist, physician on duty, nurse, technician, dietitian, and social worker.",
                   "The team around one patient. Each member sees a different part of the picture."),
    "pod01_floor": ("physician-on-duty-01-unit-floor-map.webp",
                    "Floor plan of a hemodialysis unit showing treatment stations, the isolation room, the nurses' station, the emergency cart, and the water room.",
                    "A typical unit layout. Learn where the emergency cart, oxygen, and isolation station are before your first patient arrives."),
    "pod01_ladder": ("physician-on-duty-01-escalation-ladder.webp",
                     "A four-step ladder: nurse, physician on duty, attending nephrologist, emergency room.",
                     "The escalation ladder. Problems move up one step at a time, quickly, with the same facts at every step."),
    "pod02_drain": ("physician-on-duty-02-closed-drain.webp",
                    "Two houses with the same tap running: one with an open drain, one with the drain closed and water rising.",
                    "With the drain closed, everything that comes in stays until the next dialysis session."),
    "pod02_potassium": ("physician-on-duty-02-potassium-cell.webp",
                        "A cell packed with potassium and a thin layer of potassium in the blood outside it, with arrows for insulin and adrenaline pushing potassium in and acid pushing it out.",
                        "Almost all potassium sits inside cells. Small shifts across the cell wall cause large changes in the blood."),
    "pod02_sawtooth": ("physician-on-duty-02-weekly-sawtooth.webp",
                       "A weekly graph with weight, potassium, and urea rising between sessions and falling during each session, highest after the longest gap.",
                       "One week on dialysis. The peaks are highest after the longest gap."),
    "pod02_salt": ("physician-on-duty-02-salt-in-filipino-food.webp",
                   "Common Filipino foods high in salt: patis, toyo, bagoong, instant noodles, tuyo, and canned goods.",
                   "Salt drives thirst. Most of it comes from sauces, dried fish, and processed food."),
}

# >>> module 05
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_05", _Pa(__file__).resolve().parent / "parts" / "figs_05.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 05

# >>> module 09
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_09", _Pa(__file__).resolve().parent / "parts" / "figs_09.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 09

# >>> module 10
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_10", _Pa(__file__).resolve().parent / "parts" / "figs_10.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 10

# >>> module 11
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_11", _Pa(__file__).resolve().parent / "parts" / "figs_11.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 11

# >>> module 13
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_13", _Pa(__file__).resolve().parent / "parts" / "figs_13.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 13

# >>> module 16
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_16", _Pa(__file__).resolve().parent / "parts" / "figs_16.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 16

# >>> module 15
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_figs_15", _Pa(__file__).resolve().parent / "parts" / "figs_15.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.FIGS.items():
    FIGS.setdefault(_k, _v)
# <<< module 15
