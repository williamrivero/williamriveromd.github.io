# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 03: The Rules. v0.1 RT03."""

MODULE = {
    "image_alt": "A reprocessing technician at a desk comparing a printed Philippine regulation, a payer circular and a germicide instruction sheet, with a labeled dialyzer beside them.",
    "objectives": [
        "Tell apart a licensing order, a payer condition, professional guidance, device and germicide instructions, and a local procedure.",
        "State the Philippine requirements that shape reuse: DOH duties and water monitoring, PSN eligibility guidance, PhilHealth use limits and volume floor.",
        "Count uses correctly: five uses is the first treatment plus up to four reuses.",
        "Compare Philippine rules with United States and Malaysian rules without exporting one country&rsquo;s rule to another.",
        "Apply the strictest rule that applies to a dialyzer, and hold when rules conflict.",
    ],
    "big": """
{{plain:Driving a jeepney means obeying several rulebooks at once: the traffic law, the franchise conditions, the vehicle maker&rsquo;s manual, and the operator&rsquo;s own house rules. When the maker says the brakes need checking every month and the operator says every week, you check every week.}}
<p>The picture has a limit. Traffic rules are mostly about the driver. Reuse rules are about a patient who cannot see the reuse room and has to trust that every rulebook was followed. So the reprocessing technician cannot pick the convenient rule. The working principle is the strictest rule that applies to this dialyzer, and a hold when two rules conflict and nobody has decided.</p>
{{cards:Key terms for this module|Administrative Order (AO)::A regulation issued by the Department of Health. Licensing depends on meeting it.|Circular::A PhilHealth policy issuance. It sets payment conditions, not clinical permission.|Professional guidance::Standards from a medical society such as the Philippine Society of Nephrology (PSN).|Instructions for use (IFU)::The manufacturer&rsquo;s written directions for a dialyzer, a germicide or a reprocessor.|Standard operating procedure (SOP)::The unit&rsquo;s own written procedure, approved by the medical director.|Use count::The number of treatments a dialyzer has been used for, including the first.}}
<p>You do not need to memorize every rule. You need to know which rulebook answers which question, where to find the current version, and what to do when they disagree.</p>
""",
    "case": {"title": "The transfer patient", "html": """
<p>Mr. Danilo Reyes, 47, transfers from a unit in Cavite to your unit in Quezon City. He arrives with his own reprocessed dialyzer in a sealed bag, labeled &ldquo;Reuse 4&rdquo; in his old unit&rsquo;s handwriting. His transfer papers list his hepatitis B surface antigen (HBsAg) as negative, tested seven months ago; his hepatitis C antibody result is not in the folder.</p>
<p>The technician on duty, Ms. Arlene Bautista, has to decide what to do with the dialyzer before the 1 p.m. shift. The charge nurse says, &ldquo;Use it; it only has one use left.&rdquo;</p>
""", "questions": ["What does &ldquo;Reuse 4&rdquo; mean, and how many uses has the dialyzer had?",
                  "Which rules decide whether this dialyzer may be used in your unit?",
                  "What should Ms. Bautista do before 1 p.m.?"]},
    "sections": [
        ("rulebooks", "Rulebooks", "Which rulebook answers which question", """
{{fig:rt03_hierarchy}}
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Kind</th><th>Question it answers</th><th>Example for reuse</th></tr></thead>
<tbody>
<tr><td>DOH AO 2012-0001</td><td>Licensing regulation</td><td>What must a licensed dialysis facility have and do?</td><td>Technician duties include daily reprocessor calibration, reprocessing, acceptance testing, labeling, records and storage[[doh2012]]</td></tr>
<tr><td>DOH AO 2013-0003</td><td>Licensing regulation</td><td>How must dialysis water be monitored?</td><td>Microbiology at least monthly; chemical analysis at least every six months; weekly product-water total dissolved solids (TDS)[[doh_water]]</td></tr>
<tr><td>PSN Hemodialysis Guidelines, 2024</td><td>Professional guidance</td><td>What do nephrologists consider sound practice?</td><td>Reuse in hepatitis B or C only with separate areas and machines; no dialyzer reuse in HIV[[psn2024]]</td></tr>
<tr><td>PhilHealth Circular 2024-0023</td><td>Payer condition</td><td>What will the hemodialysis package pay for?</td><td>Up to five uses per dialyzer, up to 32 dialyzers a year within the package[[rt_phic0023]]</td></tr>
<tr><td>PhilHealth Circular 2024-0029</td><td>Payer quality condition</td><td>What must a facility show to qualify?</td><td>An established reuse protocol and TCV of at least 80%[[rt_phic0029]]</td></tr>
<tr><td>Dialyzer, germicide and reprocessor IFUs</td><td>Manufacturer instructions</td><td>How may this product be used?</td><td>Whether the dialyzer may be reprocessed at all; germicide concentration and contact time</td></tr>
<tr><td>Unit SOP</td><td>Local procedure</td><td>How does this unit do it?</td><td>The exact steps, tests and records, and often a lower use limit</td></tr>
</tbody></table></div>
<p>A payer rule is about money, not safety. PhilHealth paying for up to five uses does not mean a dialyzer may be used five times. It means the package will not pay for more. A lower limit in the IFU or the SOP comes first.</p>
{{key:Each rulebook answers its own question. The strictest one that applies to this dialyzer decides.}}
"""),
        ("counting", "Counting uses", "Five uses is not five reuses", """
{{fig:rt03_uses}}
<p>The PhilHealth package counts uses: the first treatment plus up to four more after reprocessing.[[rt_phic0023]] Some units count reuses instead, starting from zero after the first treatment. The same dialyzer can be &ldquo;use 5&rdquo; in one system and &ldquo;reuse 4&rdquo; in another. Confusing the two gives a patient a sixth use.</p>
<div class="table-wrap"><table>
<thead><tr><th>Treatment</th><th>Use number</th><th>Reprocessing cycles completed before it</th><th>Eligible under a five-use ceiling?</th></tr></thead>
<tbody>
<tr><td>First treatment, new dialyzer</td><td>1</td><td>0</td><td>Yes</td></tr>
<tr><td>Second</td><td>2</td><td>1</td><td>Yes, if every gate passes</td></tr>
<tr><td>Fifth</td><td>5</td><td>4</td><td>Yes, if every gate passes</td></tr>
<tr><td>Sixth</td><td>6</td><td>5</td><td><strong>No</strong>, even with a passing volume test</td></tr>
</tbody></table></div>
<p>A processing cycle is not a use. A dialyzer that is reprocessed twice because the first cycle failed has had one more processing cycle, not one more use. Your unit&rsquo;s record must keep both counts, labeled.</p>
{{key:Count completed treatments. The sixth use is never eligible, whatever the tests say. When the counting system is unclear, hold.}}
"""),
        ("eligibility", "Eligibility by country", "Infection status and reuse: three countries, three answers", """
<p>Countries handle blood-borne infection and reuse differently. Each rule must keep its country label.</p>
<div class="table-wrap"><table>
<thead><tr><th>Topic</th><th>Philippines (PSN 2024)</th><th>United States (federal rule)</th><th>Malaysia (2026 standards)</th></tr></thead>
<tbody>
<tr><td>Same patient only</td><td>Patient-specific labeling and matching</td><td>Required[[rt_cfr494]]</td><td>Individually labeled storage[[rt_my2026]]</td></tr>
<tr><td>Hepatitis B positive</td><td>Only with a separate area and machine; otherwise single use[[psn2024]]</td><td>Reuse not permitted[[rt_cfr494]]</td><td>Single use mandatory[[rt_my2026]]</td></tr>
<tr><td>Hepatitis C positive</td><td>Only with a separate area and machine; otherwise single use[[psn2024]]</td><td>Federal rule does not exclude it; follow the facility program</td><td>Single use mandatory[[rt_my2026]]</td></tr>
<tr><td>HIV positive</td><td>No dialyzer reuse[[psn2024]]</td><td>Not addressed by the same exclusion; do not export the PSN rule</td><td>Confirm the full local policy</td></tr>
</tbody></table></div>
<p>This track teaches a conservative academy default for Philippine units: single use for hepatitis B and HIV; hepatitis C on hold unless the medical director approves a documented pathway with dedicated facilities; unknown or conflicting status always on hold. It is a teaching default, not a national rule. Your unit&rsquo;s program decides.</p>
{{stop:If a patient&rsquo;s infection status is unknown, out of date under your program, or conflicting, hold the dialyzer and ask. Do not reprocess on an assumption.}}
"""),
        ("currency", "Is the rule current?", "Is the rule current?", """
<p>Rules change. A photocopy in a drawer may be two versions old. Before you rely on a rule, check four things: who issued it, its number and date, whether it has been amended or replaced, and whether it applies to your type of facility.</p>
<p>The Malaysian standards show why. Their 2026 edition replaced the 2018 edition; a statement in the older edition about reusing dialyzers many times should not be quoted as current, and it was never a Philippine rule.[[rt_my2026]] PhilHealth circulars are amended often; the medical director or compliance officer confirms which apply.</p>
{{cards:Where to find the current version|DOH::The Health Facilities and Services Regulatory Bureau (HFSRB) and your regional licensing office.|PhilHealth::The circulars archive on the PhilHealth website and your regional office.|PSN::The current hemodialysis guidelines on the PSN website.|Manufacturers::The IFU shipped with the product lot you are using.}}
{{key:A rule without a date is a rumor. Use the current edition, and ask when in doubt.}}
"""),
    ],
    "debrief": ["""
<p><strong>What does &ldquo;Reuse 4&rdquo; mean?</strong> If his old unit counted reuses, the dialyzer has had five uses already: the first treatment plus four reuses. Its next use would be the sixth, which no five-use ceiling allows. If the old unit counted uses, it has had four. Ms. Bautista cannot tell from a handwritten label alone, so the count is unproven.</p>
<p><strong>Which rules decide?</strong> Your unit&rsquo;s program, which follows the strictest applicable rule. The dialyzer arrives without your unit&rsquo;s processing record, with no proof of how it was cleaned, tested or stored, and with an incomplete infection workup. Under most programs, a dialyzer from another facility is not accepted for reuse.</p>
<p><strong>What should she do?</strong> Hold the dialyzer, label it as quarantined, and tell the charge nurse that Mr. Reyes needs a new dialyzer today. She reports the missing hepatitis C result so the nurse can raise it with the nephrologist, who decides his eligibility. &ldquo;Only one use left&rdquo; is an assumption, and assumptions are not evidence.</p>
"""],
    "skills": {"title": "Rule-finding and use-count drill",
               "intro": "Use printed copies of your unit&rsquo;s SOP, the relevant issuances, and five synthetic dialyzer records with mixed counting systems.",
               "items": [
                   ("Names the source that answers each of five questions (licensing, water, eligibility, payment, product use).", False),
                   ("Converts each record to a use number and identifies the one that would reach a sixth use.", True),
                   ("Distinguishes a processing cycle from a use.", True),
                   ("Applies the stricter of an IFU limit and the payer ceiling.", True),
                   ("Holds a dialyzer whose infection eligibility is unknown or conflicting.", True),
                   ("Checks the issue date and current status of one rule.", False),
               ],
               "placement": "Find the current edition of each document your unit&rsquo;s reuse program cites. Note any that are out of date and show the list to the head nurse."},
    "quiz": [
        ("A dialyzer has been used for four treatments. Under a five-use ceiling, how many more treatments may it be used for if every gate passes?",
         ["One", "Two", "Four", "Five"], 0,
         "Five uses total. Four done, one left."),
        ("&ldquo;Five uses&rdquo; under the PhilHealth package means:",
         ["The first treatment plus up to five reuses", "The first treatment plus up to four reuses", "Five processing cycles", "Five months of storage"], 1,
         "The count includes the first treatment."),
        ("A dialyzer failed its first processing cycle and was processed again before passing. What changed?",
         ["Its use number went up by one", "It had one more processing cycle; the use number is unchanged", "Its baseline was reset", "It must be discarded"], 1,
         "A processing cycle is not a treatment."),
        ("The IFU allows three uses; PhilHealth pays for up to five. How many uses are allowed?",
         ["Five", "Four", "Three", "Eight"], 2,
         "The strictest rule that applies wins."),
        ("What is PhilHealth Circular 2024-0029&rsquo;s volume criterion?",
         ["TCV of at least 50%", "TCV of at least 80%", "TCV of at least 95%", "No volume criterion"], 1,
         "At least 80% of baseline, as one of several criteria."),
        ("Under PSN 2024 guidance, dialyzer reuse for a patient with HIV is:",
         ["Allowed with a separate machine", "Not allowed", "Allowed up to five uses", "Allowed if the patient consents"], 1,
         "The PSN guidance does not allow dialyzer reuse in HIV."),
        ("Which statement about the United States federal reuse rule is correct?",
         ["It applies to Philippine units", "It excludes patients positive for hepatitis B from reuse", "It requires single use for everyone", "It sets a ceiling of five uses"], 1,
         "The US rule excludes hepatitis B positive patients. It does not apply to Philippine units."),
        ("A patient&rsquo;s hepatitis C result is missing from the transfer folder. What do you do with his dialyzer?",
         ["Reprocess it; most patients are negative", "Hold it and report the missing result", "Reprocess it in the general area", "Ask the patient"], 1,
         "Unknown status holds. Eligibility is decided by the clinical team."),
        ("What does a PhilHealth circular decide?",
         ["Whether a dialyzer is safe", "Payment conditions", "The germicide concentration", "Who may cannulate"], 1,
         "A payer rule decides what is paid for, not whether something is safe."),
        ("You find a 2018 regional standard in a drawer that mentions very high reuse numbers. What should you do?",
         ["Follow it", "Check whether it has been replaced; the 2026 edition supersedes it, and it was never a Philippine rule", "Post it on the wall", "Use it to set your unit&rsquo;s limit"], 1,
         "Always check edition, issuer and applicability."),
        ("Where does the exact germicide contact time come from?",
         ["The payer circular", "The germicide IFU and the validated SOP", "The technician&rsquo;s experience", "The patient&rsquo;s chart"], 1,
         "Chemistry comes from the product instructions and the validated procedure."),
        ("A dialyzer arrives from another facility with a handwritten label and no processing record. Under most programs it is:",
         ["Accepted if the label looks recent", "Not accepted for reuse; the patient receives a new dialyzer", "Accepted after one extra rinse", "Accepted if the charge nurse agrees"], 1,
         "Without your unit&rsquo;s record, nothing about its history is proven."),
    ],
    "terms": [("Administrative Order", "A DOH regulation; licensing depends on meeting it."),
              ("Circular", "A PhilHealth policy issuance setting payment conditions."),
              ("Professional guidance", "Standards issued by a medical society."),
              ("Instructions for use", "The manufacturer&rsquo;s written directions for a product."),
              ("Use count", "The number of treatments a dialyzer has been used for, including the first."),
              ("Processing cycle", "One complete run of reprocessing; not the same as a use."),
              ("Supersede", "To replace an older version of a rule.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "Background on reuse rules and practice.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c2"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
