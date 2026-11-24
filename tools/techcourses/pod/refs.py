# -*- coding: utf-8 -*-
"""References for the Physician on Duty track (APA 7). Merged into SHARED.REFS by generate_tech_courses.py
(see integrate_pod.py). Keys are cited in module text as [[key]]. Each entry was checked against PubMed or the
publisher on November 23, 2026."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "foley2011": ("Foley, R. N., Gilbertson, D. T., Murray, T., &amp; Collins, A. J. (2011). Long interdialytic interval and mortality among "
                  "patients receiving hemodialysis. <em>New England Journal of Medicine, 365</em>(12), 1099&ndash;1107. " + _doi("10.1056/NEJMoa1103313")),
    "flythe2011": ("Flythe, J. E., Kimmel, S. E., &amp; Brunelli, S. M. (2011). Rapid fluid removal during dialysis is associated with "
                   "cardiovascular morbidity and mortality. <em>Kidney International, 79</em>(2), 250&ndash;257. " + _doi("10.1038/ki.2010.383")),
    "kalantar2009": ("Kalantar-Zadeh, K., Regidor, D. L., Kovesdy, C. P., Van Wyck, D., Bunnapradist, S., Horwich, T. B., &amp; Fonarow, G. C. (2009). "
                     "Fluid retention is associated with cardiovascular mortality in patients undergoing long-term hemodialysis. "
                     "<em>Circulation, 119</em>(5), 671&ndash;679. " + _doi("10.1161/CIRCULATIONAHA.108.807362")),
    "obi2016": ("Obi, Y., Rhee, C. M., Mathew, A. T., Shah, G., Streja, E., Brunelli, S. M., Kovesdy, C. P., Mehrotra, R., &amp; Kalantar-Zadeh, K. (2016). "
                "Residual kidney function decline and mortality in incident hemodialysis patients. "
                "<em>Journal of the American Society of Nephrology, 27</em>(12), 3758&ndash;3768. " + _doi("10.1681/ASN.2015101142")),
    "palmer2016": ("Palmer, B. F., &amp; Clegg, D. J. (2016). Physiology and pathophysiology of potassium homeostasis. "
                   "<em>Advances in Physiology Education, 40</em>(4), 480&ndash;490. " + _doi("10.1152/advan.00121.2016")),
    "kdigo_bpvol2020": ("Flythe, J. E., Chang, T. I., Gallagher, M. P., Lindley, E., Madero, M., Sarafidis, P. A., Unruh, M. L., Wang, A. Y.-M., "
                        "Weiner, D. E., Cheung, M., Jadoul, M., Winkelmayer, W. C., &amp; Polkinghorne, K. R. (2020). Blood pressure and volume management "
                        "in dialysis: Conclusions from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference. "
                        "<em>Kidney International, 97</em>(5), 861&ndash;876. " + _doi("10.1016/j.kint.2020.01.046")),
    "muller2018": ("M&uuml;ller, M., J&uuml;rgens, J., Reda&egrave;lli, M., Klingberg, K., Hautz, W. E., &amp; Stock, S. (2018). Impact of the communication "
                   "and patient hand-off tool SBAR on patient safety: A systematic review. <em>BMJ Open, 8</em>(8), e022202. " + _doi("10.1136/bmjopen-2018-022202")),
    "meyer2007": ("Meyer, T. W., &amp; Hostetter, T. H. (2007). Uremia. <em>New England Journal of Medicine, 357</em>(13), 1316&ndash;1325. "
                  + _doi("10.1056/NEJMra071313")),
    "kraut2016": ("Kraut, J. A., &amp; Madias, N. E. (2016). Metabolic acidosis of CKD: An update. "
                  "<em>American Journal of Kidney Diseases, 67</em>(2), 307&ndash;317. " + _doi("10.1053/j.ajkd.2015.08.028")),
    "montague2008": ("Montague, B. T., Ouellette, J. R., &amp; Buller, G. K. (2008). Retrospective review of the frequency of ECG changes in hyperkalemia. "
                     "<em>Clinical Journal of the American Society of Nephrology, 3</em>(2), 324&ndash;330. " + _doi("10.2215/CJN.04611007")),
    "daugirdas2015": ("Daugirdas, J. T., Blake, P. G., &amp; Ing, T. S. (Eds.). (2015). <em>Handbook of dialysis</em> (5th ed.). Wolters Kluwer."),
    "hall2021": ("Hall, J. E., &amp; Hall, M. E. (2021). <em>Guyton and Hall textbook of medical physiology</em> (14th ed.). Elsevier."),
    "ra10173": ("Republic of the Philippines. (2012). <em>Republic Act No. 10173: Data Privacy Act of 2012</em>. "
                '<a href="https://privacy.gov.ph/data-privacy-act/">https://privacy.gov.ph/data-privacy-act/</a>'),
}

# >>> module 05
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_05", _Pa(__file__).resolve().parent / "parts" / "refs_05.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 05

# >>> module 09
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_09", _Pa(__file__).resolve().parent / "parts" / "refs_09.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 09

# >>> module 10
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_10", _Pa(__file__).resolve().parent / "parts" / "refs_10.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 10

# >>> module 11
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_11", _Pa(__file__).resolve().parent / "parts" / "refs_11.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 11

# >>> module 13
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_13", _Pa(__file__).resolve().parent / "parts" / "refs_13.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 13

# >>> module 16
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_16", _Pa(__file__).resolve().parent / "parts" / "refs_16.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 16

# >>> module 15
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_15", _Pa(__file__).resolve().parent / "parts" / "refs_15.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 15

# >>> module 03
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_03", _Pa(__file__).resolve().parent / "parts" / "refs_03.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 03

# >>> module 04
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_04", _Pa(__file__).resolve().parent / "parts" / "refs_04.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 04

# >>> module 06
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_06", _Pa(__file__).resolve().parent / "parts" / "refs_06.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 06

# >>> module 07
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_07", _Pa(__file__).resolve().parent / "parts" / "refs_07.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 07

# >>> module 08
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_08", _Pa(__file__).resolve().parent / "parts" / "refs_08.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 08

# >>> module 12
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_12", _Pa(__file__).resolve().parent / "parts" / "refs_12.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 12

# >>> module 14
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_14", _Pa(__file__).resolve().parent / "parts" / "refs_14.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 14

# >>> module 17
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_17", _Pa(__file__).resolve().parent / "parts" / "refs_17.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 17

# >>> module 18
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_18", _Pa(__file__).resolve().parent / "parts" / "refs_18.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 18

# >>> module 19
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_19", _Pa(__file__).resolve().parent / "parts" / "refs_19.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 19

# >>> module 20
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_20", _Pa(__file__).resolve().parent / "parts" / "refs_20.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 20

# >>> module 21
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_21", _Pa(__file__).resolve().parent / "parts" / "refs_21.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 21

# >>> module 22
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_22", _Pa(__file__).resolve().parent / "parts" / "refs_22.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 22

# >>> module 23
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_23", _Pa(__file__).resolve().parent / "parts" / "refs_23.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 23

# >>> module 24
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_24", _Pa(__file__).resolve().parent / "parts" / "refs_24.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 24

# >>> module 25
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_25", _Pa(__file__).resolve().parent / "parts" / "refs_25.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 25

# >>> module 26
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_26", _Pa(__file__).resolve().parent / "parts" / "refs_26.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 26

# >>> module 27
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_27", _Pa(__file__).resolve().parent / "parts" / "refs_27.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 27

# >>> module 28
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_28", _Pa(__file__).resolve().parent / "parts" / "refs_28.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 28

# >>> module 29
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_29", _Pa(__file__).resolve().parent / "parts" / "refs_29.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 29

# >>> module 30
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_30", _Pa(__file__).resolve().parent / "parts" / "refs_30.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 30

# >>> module 31
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_31", _Pa(__file__).resolve().parent / "parts" / "refs_31.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 31

# >>> module 32
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_refs_32", _Pa(__file__).resolve().parent / "parts" / "refs_32.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.REFS.items():
    REFS.setdefault(_k, _v)
# <<< module 32
