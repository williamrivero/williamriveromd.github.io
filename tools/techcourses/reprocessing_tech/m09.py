# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 09: Performance Testing and Acceptance. v0.1 RT09."""

MODULE = {
    "image_alt": "A reprocessor screen showing a total cell volume result and a pressure-hold test curve, with a technician pointing at the result and a dialyzer mounted beside it.",
    "objectives": [
        "Calculate retained total cell volume (TCV) against the dialyzer&rsquo;s own baseline, and hold when the baseline is missing or implausible.",
        "Explain what the integrity (pressure-hold) test detects, and why a passing volume cannot compensate for a failed integrity test.",
        "Inspect a processed dialyzer and name the findings that reject it.",
        "Apply every acceptance gate independently: identity, eligibility, uses left, inspection, volume, integrity, processing record.",
        "Repeat a test only as the validated procedure allows, keep every result, and escalate inconsistent results.",
    ],
    "big": """
{{plain:Buying a used car, you check that the engine runs, that the brakes work, and that the papers are in order. A strong engine does not make up for brakes that fail. Every check must pass on its own.}}
<p>The picture has a limit. A buyer can choose to accept a small fault. A technician cannot trade one result against another, because each test looks at a different danger. The volume test asks whether enough fibers are open to deliver the dose. The integrity test asks whether any fiber is broken, which would let blood and dialysis fluid mix. A dialyzer with perfect volume and a broken fiber is a dangerous dialyzer.</p>
{{cards:Key terms for this module|Total cell volume (TCV)::The volume of the blood compartment, measured to estimate how many fibers are open.|Baseline::The TCV measured on this dialyzer before its first use, under the program&rsquo;s method.|Retained TCV::Measured TCV as a percentage of baseline.|Integrity test::A pressure-hold test of the membrane: the blood side is pressurized and any leak shows as a fall in pressure.|Acceptance gate::A condition that must pass on its own before release.|Disposition::The recorded decision for a dialyzer: release, reprocess, or discard.}}
<p>Your job is to measure honestly, apply every gate independently, and let one failure stop the dialyzer.</p>
""",
    "case": {"title": "Seventy-nine and eighty", "html": """
<p>It is 4:40 on a Friday afternoon at a unit in Davao. Ms. Grace Alcantara is finishing the day&rsquo;s run. The unit floor for retained TCV is 80%, from the PhilHealth quality circular and the program.[[rt_phic0029]]</p>
<p>Dialyzer RU-0731 has a baseline of 100 mL and a measured volume of 79 mL. Dialyzer RU-0732 has a baseline of 100 mL and a measured volume of 86 mL, but its pressure-hold test failed. Dialyzer RU-0733 shows a measured volume of 104 mL against a baseline of 98 mL. A colleague suggests running RU-0731 again &ldquo;until it passes,&rdquo; and says RU-0732 is &ldquo;fine, the volume is great.&rdquo;</p>
""", "questions": ["What is the retained TCV of each dialyzer, and what does each result mean?",
                  "Can the good volume of RU-0732 make up for its failed pressure test?",
                  "When is a repeat test legitimate?"]},
    "sections": [
        ("tcv", "Total cell volume", "Measuring against a defensible baseline", """
{{fig:rt09_tcv}}
<p>TCV is measured by displacing the fluid in the blood compartment and measuring its volume. Each dialyzer&rsquo;s first measurement, before first use, is its baseline. Every later result is compared with that baseline, never with a catalog value, because individual dialyzers of the same model differ.</p>
{{formula:Retained TCV (%) = measured TCV &divide; baseline TCV &times; 100 &nbsp;&middot;&nbsp; Example for training only: 82 mL &divide; 100 mL &times; 100 = 82%.}}
<p>The PhilHealth quality circular and the AAMI standard use a floor of at least 80% retained.[[rt_phic0029]][[aami_reuse]] A dialyzer at 80% has lost a fifth of its blood compartment. It meets the floor, and it may still clean less than it did when new (Module 2).</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>What it means</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Baseline missing</td><td>No denominator; the result means nothing</td><td>Hold; never substitute a catalog value</td></tr>
<tr><td>Baseline implausible for the model</td><td>Possible measurement or recording error</td><td>Hold and investigate</td></tr>
<tr><td>Measured above baseline</td><td>Possible measurement error, air, or record mismatch</td><td>Flag for review; do not cap or accept automatically</td></tr>
<tr><td>Measured below the floor</td><td>Too many fibers closed</td><td>Fails this gate; follow the procedure for discard</td></tr>
</tbody></table></div>
{{key:Compare every result with this dialyzer&rsquo;s own baseline. A missing baseline is a hold, not a guess.}}
"""),
        ("integrity", "Integrity test", "The integrity test", """
<p>In a pressure-hold test, the reprocessor pressurizes the blood compartment, usually with air, and watches the pressure. An intact membrane holds it. A broken fiber lets gas escape to the other side, and the pressure falls faster than the allowed rate. The pass criterion comes from the reprocessor and the dialyzer model, as validated in your procedure.</p>
<p>A broken fiber is dangerous in both directions. Dialysis fluid and anything in it can enter the blood, and blood can leak into the dialysis fluid. Volume and integrity measure different things, so one can be perfect while the other fails. In a CDC study of three centers whose reprocessed dialyzers were all integrity-tested before use, the rate of pyrogenic reactions was 0.7 per 1,000 treatments despite high bacterial counts in the dialysis fluid.[[rt_gordon1992]] The study did not test the integrity check itself, but it shows the setting in which membrane integrity protects patients.</p>
{{stop:A failed integrity test stops the dialyzer, whatever its volume. Never override it, never repeat it until it passes without the procedure allowing it.}}
"""),
        ("inspection", "Inspection", "Inspecting the processed dialyzer", """
<div class="table-wrap"><table>
<thead><tr><th>Look for</th><th>Why it rejects the dialyzer</th></tr></thead>
<tbody>
<tr><td>Cracks or leaks in the housing or ports</td><td>Loss of containment; contamination</td></tr>
<tr><td>Visible clot, dark streaks or discolored fibers more than the procedure allows</td><td>Blocked surface; trapped residue</td></tr>
<tr><td>Blood or protein in the headers after cleaning</td><td>Cleaning incomplete</td></tr>
<tr><td>Missing or damaged caps; damaged O-rings</td><td>Germicide can leak out and contaminants can enter</td></tr>
<tr><td>Label damaged or unreadable</td><td>Identity lost (Module 7)</td></tr>
</tbody></table></div>
<p>Inspect in good light, at a set point in the procedure, and record what you saw. &ldquo;Looked fine&rdquo; written at the end of the day is not an inspection.</p>
"""),
        ("gates", "Every gate", "Every gate must pass", """
{{fig:rt09_gates}}
<p>Before a processed dialyzer can be stored for release, every acceptance gate must pass. Each is independent. A favorable result on one cannot compensate for a failure on another.</p>
<div class="table-wrap"><table>
<thead><tr><th>Gate</th><th>Question</th><th>If it fails or is missing</th></tr></thead>
<tbody>
<tr><td>Identity</td><td>Is this the labeled patient&rsquo;s dialyzer, with a matching record?</td><td>Quarantine</td></tr>
<tr><td>Eligibility</td><td>Is the patient currently eligible?</td><td>Hold</td></tr>
<tr><td>Uses left</td><td>Is the next use within the limit?</td><td>Discard at the limit</td></tr>
<tr><td>Inspection</td><td>Any rejecting finding?</td><td>Discard or reprocess per procedure</td></tr>
<tr><td>Volume</td><td>Retained TCV at or above the floor, against a valid baseline?</td><td>Discard below the floor; hold if baseline invalid</td></tr>
<tr><td>Integrity</td><td>Pressure held within the criterion?</td><td>Discard or follow procedure; never override</td></tr>
<tr><td>Processing record</td><td>Every step and test recorded, with the run linked to its water, germicide and reprocessor checks?</td><td>Hold until resolved, or discard</td></tr>
</tbody></table></div>
<p>After this, the germicide, contact time, storage and residual-test gates follow (Module 10).</p>
{{key:Ten gates, ten separate proofs. A passing gate cannot vote for a failing one.}}
"""),
        ("repeats", "Repeats without gaming", "Repeating a test without gaming it", """
<p>Measurements can go wrong for innocent reasons: air in the line, a loose connection, a sensor fault. Your procedure may allow one repeat for a defined reason. What it never allows is repeating a test until a passing number appears and keeping only that one.</p>
{{cards:Legitimate repeats|Defined reason::A recorded cause, such as a loose connection, that the procedure names.|Every result kept::The first result stays in the record beside the repeat.|Limited number::No more repeats than the procedure allows.|Pattern escalated::Several inconsistent results on different dialyzers suggest an equipment problem; report it to the biomedical technician (Module 11).}}
<p>A failed dialyzer stays unavailable until its disposition follows the program. A later finding that the reprocessor was faulty does not erase the dialyzer&rsquo;s recorded failure; it adds a question about every dialyzer processed on that reprocessor (Module 11).</p>
{{key:Every result belongs in the record. A test repeated until it passes proves only that the test can be beaten.}}
"""),
    ],
    "debrief": ["""
<p><strong>The three results.</strong> RU-0731: 79 &divide; 100 &times; 100 = 79%, below the 80% floor. It fails the volume gate. RU-0732: 86%, which meets the floor, but its integrity test failed. RU-0733: 104 &divide; 98 &times; 100 = 106%, above baseline. That is not a super-dialyzer; it suggests a measurement or record error and must be flagged for review, not accepted.</p>
<p><strong>Can RU-0732&rsquo;s volume make up for the failed pressure test?</strong> No. The two tests look at different dangers. A broken fiber can mix blood and dialysis fluid regardless of how many fibers are open. RU-0732 follows the procedure for an integrity failure.</p>
<p><strong>When is a repeat legitimate?</strong> Only for a defined, recorded reason the procedure allows, with the first result kept. Running RU-0731 &ldquo;until it passes&rdquo; is gaming. If several dialyzers that day gave odd readings, Ms. Alcantara reports a possible equipment fault before more dialyzers are processed.</p>
"""],
    "skills": {"title": "Acceptance decisions on ten records",
               "intro": "Use ten synthetic processing records and the Reprocessing Technician Toolkit, then observe acceptance testing on the unit&rsquo;s reprocessor.",
               "items": [
                   ("Calculates retained TCV correctly for every record.", True),
                   ("Holds a record with a missing or implausible baseline.", True),
                   ("Flags a measured volume above baseline for review.", True),
                   ("Rejects a dialyzer with a failed integrity test regardless of volume.", True),
                   ("Identifies the record that would reach a sixth use.", True),
                   ("Inspects a processed training dialyzer and records findings.", False),
                   ("States when a repeat test is legitimate and keeps every result.", True),
                   ("Writes a disposition (release to storage, reprocess, discard, hold) for each record.", False),
               ],
               "placement": "During supervised practice, handle at least one failed volume and one failed integrity result from start to disposition, observed by your assessor."},
    "quiz": [
        ("Baseline 100 mL, measured 85 mL. What is the retained TCV?",
         ["15%", "85%", "100%", "117%"], 1,
         "85 &divide; 100 &times; 100 = 85%."),
        ("Baseline 100 mL, measured 79 mL, floor 80%. What is the decision on volume?",
         ["Pass", "Fail", "Round up to pass", "Repeat until it passes"], 1,
         "79% is below the floor."),
        ("A dialyzer has 90% retained volume but failed its integrity test. What happens?",
         ["Release, since volume is excellent", "It fails; volume cannot compensate for a failed integrity test", "Release if the nurse agrees", "Average the two results"], 1,
         "Each gate is independent."),
        ("A record has no baseline TCV. What do you do?",
         ["Use the catalog value", "Hold the dialyzer until the record is resolved", "Use the average of other dialyzers", "Assume 100 mL"], 1,
         "Without a valid baseline the result means nothing."),
        ("Measured volume is above the baseline. What is the correct response?",
         ["Accept it as excellent", "Cap it at 100%", "Flag it for review as a possible error", "Reset the baseline to the new value"], 2,
         "A value above baseline suggests an error."),
        ("What does a pressure-hold test detect?",
         ["Clotted fibers", "A broken fiber or leak in the membrane", "Germicide strength", "Water quality"], 1,
         "A leak lets pressure fall faster than allowed."),
        ("What did the PhilHealth quality circular set for retained TCV?",
         ["At least 50%", "At least 80%", "At least 95%", "No requirement"], 1,
         "At least 80%, as one criterion among several."),
        ("Your colleague repeats a failed volume test four times and records only the passing result. What is wrong?",
         ["Nothing", "It is gaming: every result must be kept, and repeats need a defined reason", "Only that it took too long", "He should have repeated it five times"], 1,
         "Selective recording destroys the evidence."),
        ("Several dialyzers today gave inconsistent volume readings. What should you suspect and do?",
         ["Bad luck; keep going", "A possible equipment fault; stop and report to the biomedical technician", "Patients clotting more", "Germicide too strong"], 1,
         "A pattern across dialyzers points to the machine."),
        ("Why is a catalog volume not used as the baseline?",
         ["It is too high", "Individual dialyzers of the same model differ, so only this dialyzer&rsquo;s first measurement is valid", "It is secret", "It changes every year"], 1,
         "Each dialyzer is its own reference."),
        ("A dialyzer passes volume, integrity and inspection, but its processing record has a blank where the reprocessor run number should be. Is it ready?",
         ["Yes, all tests passed", "No; the processing record gate is not proven", "Yes, if it is the patient&rsquo;s last use", "Yes, if the run number is added from memory"], 1,
         "An unlinked record cannot prove the run&rsquo;s water, germicide and machine checks."),
        ("A dialyzer at exactly 80% retained TCV means:",
         ["It is as good as new", "It meets the volume floor only; all other gates still apply", "It must be discarded", "It may be used ten more times"], 1,
         "Meeting one floor is not release."),
    ],
    "terms": [("Total cell volume", "The volume of a dialyzer&rsquo;s blood compartment."),
              ("Baseline", "This dialyzer&rsquo;s TCV measured before first use."),
              ("Retained TCV", "Measured TCV as a percentage of baseline."),
              ("Integrity test", "A pressure-hold test that detects a broken fiber or leak."),
              ("Acceptance gate", "A condition that must pass on its own before release."),
              ("Disposition", "The recorded decision: release, reprocess or discard."),
              ("Gaming", "Repeating or selecting results to obtain a pass.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "Performance tests in reprocessing.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c1", "calc-reprocessing-technician-toolkit.html#c2"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
