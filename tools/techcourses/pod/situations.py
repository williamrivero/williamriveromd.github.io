# -*- coding: utf-8 -*-
"""Real situations and field notes for the Physician on Duty modules. Each scenario: (title, what you see,
what is likely going on, what to do, why it matters). All are fictional and were written for this series."""

SITUATIONS = {
"01": {"scenarios": [
    ("Two calls at once", "A nurse reports chest pain at station 4 while you are examining a breathless patient at station 9.",
     "Two patients may both be unstable, and you can be in only one place.",
     "Ask the charge nurse to send a nurse with the emergency cart to station 4, get an electrocardiogram and vital signs there, and have someone telephone the attending nephrologist. Finish the first minute of care where you are, then move to the sicker patient.",
     "You lead by assigning tasks. A physician who tries to do everything alone delays both patients."),
    ("The order that does not fit", "The prescription says dialysis fluid potassium 2 mmol/L. This morning&rsquo;s result shows the patient&rsquo;s potassium is at the low end of normal, and he has had diarrhea for three days.",
     "The standing prescription was written for his usual state, not for today.",
     "Hold the start, examine him, and call the attending nephrologist with the result and the history. Do not change the dialysis fluid yourself.",
     "The prescription belongs to the nephrologist, but noticing that it no longer fits today&rsquo;s patient belongs to you."),
    ("The family at the nurses&rsquo; station", "A patient&rsquo;s daughter asks loudly, in front of other patients, whether her father&rsquo;s hepatitis test came back.",
     "She is worried, and she has not thought about who can hear.",
     "Take her to a private space before answering. Confirm that the patient agrees to share his results with her, then explain, or arrange for the attending nephrologist to do so.",
     "Health information is sensitive, and other patients on an open floor hear everything."),
    ("&ldquo;Doctor, just sign here&rdquo;", "At the end of a busy shift you are handed a stack of forms and certificates to sign for patients you did not examine.",
     "The paperwork has fallen behind and you are the available physician.",
     "Sign only what you can personally confirm. For the rest, review the record or see the patient first, or leave it for the physician who did.",
     "Your signature certifies that something is true. It is a legal statement."),
    ("The nephrologist does not answer", "A patient&rsquo;s blood pressure has not recovered after the first steps of the protocol. You have called the attending nephrologist twice with no answer.",
     "The nephrologist may be in a procedure or out of signal.",
     "Continue care, and go to the next name on the unit&rsquo;s escalation list now: the covering nephrologist, then the clinical head. Record each call and its time.",
     "An escalation list exists for exactly this. Waiting for one person is not a plan."),
], "tips": [
    "Walk the floor at the start of the last hour of every shift. That is when blood pressure falls and cramps begin.",
    "Save every attending nephrologist&rsquo;s number in your telephone on the first day.",
    "When a nurse calls you to a chair, go. You can decide it was nothing after you have looked.",
    "Write the time on every note and every order.",
    "If you are unsure whether to call, call."]},
"02": {"scenarios": [
    ("The drip that came with the patient", "A patient who makes no urine is sent from a ward for dialysis with a liter of saline running at a &ldquo;maintenance&rdquo; rate. It has been running since the night before.",
     "The ward team ordered what they order for every admitted patient.",
     "Stop the drip and cap the cannula. Find out how much has gone in, examine the patient for overload, and tell the attending nephrologist, because today&rsquo;s fluid removal target may need to change. Call the ward team and explain why.",
     "Every milliliter is still inside the patient. Teaching the ward prevents the same order tomorrow."),
    ("Fasting since midnight", "A diabetic dialysis patient has fasted for 14 hours for a procedure that was delayed. She feels weak. Her blood sugar is normal.",
     "Long fasting lowers insulin, and potassium moves out of cells. Weakness may be a sign of a high potassium.",
     "Get an electrocardiogram and an urgent potassium, follow your unit&rsquo;s hyperkalemia protocol if it is high, and call the attending nephrologist. Remember that a normal electrocardiogram does not rule it out.",
     "Hyperkalemia can develop without the patient eating any potassium."),
    ("Normal ankles, wet lungs", "A thin, elderly patient is 3 kilograms above dry weight. Her ankles are not swollen, but she slept sitting up and has crackles at both lung bases.",
     "She is overloaded. Leg edema appears late, and less in patients who have been sitting or lying.",
     "Treat her as overloaded: sit her up, check oxygen saturation, and report the findings. Do not be reassured by the ankles.",
     "Breathlessness on lying flat and weight gain are earlier and more reliable signs than ankle swelling."),
    ("The Friday result on a Monday", "A potassium of 3.6 mmol/L is on the chart, and a relative asks whether the patient should eat more bananas. The sample was taken right after last Friday&rsquo;s session.",
     "A sample taken right after dialysis is the lowest value of the week, and it rebounds within hours.",
     "Explain that the result does not show a low potassium. Advise no change in diet, and check when the next pre-dialysis sample is due.",
     "Acting on the timing-distorted result could cause dangerous hyperkalemia over the long gap."),
    ("Weight below target, pressure low", "A patient arrives 0.8 kilograms below his dry weight after three days of poor appetite and loose stools. His blood pressure is 92/58.",
     "He may be truly short of volume, and his real body weight may also be falling.",
     "Examine him and look for infection. Call the attending nephrologist before starting: the session may need little or no fluid removal, and the dry weight may need review.",
     "Removing fluid from a patient who is already dry causes low blood pressure and can injure the heart and gut."),
], "tips": [
    "The first question for any dialysis patient is how much urine they still pass.",
    "Look at the trend of pre-dialysis weights over several weeks, not just today&rsquo;s.",
    "Ask what the patient ate over the gap. Dried fish, instant noodles, and sauces explain most large weight gains.",
    "When another department telephones about a dialysis patient&rsquo;s fluids, take the call. It is the cheapest prevention you will do all day.",
    "Always note when a blood sample was taken in relation to dialysis."]},
}

# >>> module 05
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_05", _Pa(__file__).resolve().parent / "parts" / "situations_05.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 05

# >>> module 09
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_09", _Pa(__file__).resolve().parent / "parts" / "situations_09.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 09

# >>> module 10
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_10", _Pa(__file__).resolve().parent / "parts" / "situations_10.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 10

# >>> module 11
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_11", _Pa(__file__).resolve().parent / "parts" / "situations_11.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 11

# >>> module 13
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_13", _Pa(__file__).resolve().parent / "parts" / "situations_13.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 13

# >>> module 16
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_16", _Pa(__file__).resolve().parent / "parts" / "situations_16.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 16

# >>> module 15
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_15", _Pa(__file__).resolve().parent / "parts" / "situations_15.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 15

# >>> module 03
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_03", _Pa(__file__).resolve().parent / "parts" / "situations_03.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 03

# >>> module 04
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_04", _Pa(__file__).resolve().parent / "parts" / "situations_04.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 04

# >>> module 06
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_06", _Pa(__file__).resolve().parent / "parts" / "situations_06.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 06

# >>> module 07
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_07", _Pa(__file__).resolve().parent / "parts" / "situations_07.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 07

# >>> module 08
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_08", _Pa(__file__).resolve().parent / "parts" / "situations_08.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 08

# >>> module 12
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_12", _Pa(__file__).resolve().parent / "parts" / "situations_12.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 12

# >>> module 14
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_14", _Pa(__file__).resolve().parent / "parts" / "situations_14.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 14

# >>> module 17
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_17", _Pa(__file__).resolve().parent / "parts" / "situations_17.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 17

# >>> module 18
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_18", _Pa(__file__).resolve().parent / "parts" / "situations_18.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 18

# >>> module 19
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_19", _Pa(__file__).resolve().parent / "parts" / "situations_19.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 19

# >>> module 20
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_20", _Pa(__file__).resolve().parent / "parts" / "situations_20.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 20

# >>> module 21
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_21", _Pa(__file__).resolve().parent / "parts" / "situations_21.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 21

# >>> module 22
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_22", _Pa(__file__).resolve().parent / "parts" / "situations_22.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 22

# >>> module 23
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_23", _Pa(__file__).resolve().parent / "parts" / "situations_23.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 23

# >>> module 24
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_24", _Pa(__file__).resolve().parent / "parts" / "situations_24.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 24

# >>> module 25
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_25", _Pa(__file__).resolve().parent / "parts" / "situations_25.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 25

# >>> module 26
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_26", _Pa(__file__).resolve().parent / "parts" / "situations_26.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 26

# >>> module 27
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_27", _Pa(__file__).resolve().parent / "parts" / "situations_27.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 27

# >>> module 28
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_28", _Pa(__file__).resolve().parent / "parts" / "situations_28.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 28

# >>> module 29
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_29", _Pa(__file__).resolve().parent / "parts" / "situations_29.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 29

# >>> module 30
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_30", _Pa(__file__).resolve().parent / "parts" / "situations_30.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 30

# >>> module 31
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_31", _Pa(__file__).resolve().parent / "parts" / "situations_31.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 31

# >>> module 32
import importlib.util as _iu
from pathlib import Path as _Pa
_sp = _iu.spec_from_file_location("pod_situations_32", _Pa(__file__).resolve().parent / "parts" / "situations_32.py")
_mo = _iu.module_from_spec(_sp); _sp.loader.exec_module(_mo)
for _k, _v in _mo.SITUATIONS.items():
    SITUATIONS.setdefault(_k, _v)
# <<< module 32
