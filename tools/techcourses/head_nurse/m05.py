# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 05: Making Infection Prevention Visible. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse observing hand hygiene at a dialysis station from a short distance, clipboard in hand.",
    "objectives": [
        "Explain why dialysis patients are prone to infection, using the host, the portal, the environment, and the fluid.",
        "Explain why hepatitis B needs a dedicated room, machine, and staff, and hepatitis C does not.",
        "List the core interventions for preventing bloodstream infection, and state how strong the evidence is.",
        "Observe hand hygiene and catheter care, and report the result with its uncertainty.",
        "Calculate a bloodstream infection rate with the right denominator.",
        "Start the review of a possible cluster without delaying care for the patients.",
    ],
    "big": """
{{plain:Picture every station as an island with an invisible shoreline. During treatment, everything inside the shoreline is contaminated with that patient&rsquo;s blood until it is cleaned: the chair, the machine surface, the clamps, the blanket. Infection spreads when something crosses a shoreline without being cleaned.}}
<p>The picture has a limit. Real contamination is invisible and uneven. That is exactly why the shoreline has to be treated as real even when nothing looks dirty.</p>
{{fig:hn05_shore}}
{{cards:Key terms for this module|Bloodstream infection (BSI)::Organisms growing in the blood, shown by a positive blood culture.|Access-related BSI::A bloodstream infection whose source is the access, usually a catheter.|Pyrogenic reaction::Fever and chills from fragments of bacteria in the fluid, not from live bacteria in the blood.|Hand-hygiene opportunity::A moment when hand hygiene is required, such as before touching a patient or after touching the station.|Patient-month::One patient followed for one month. The denominator for most dialysis infection rates.|Catheter-day::One patient with a catheter for one day.|Cluster::Two or more linked infections close together in time or place.}}
""",
    "case": {"title": "Chills on the same shift", "html": """
<p>On the Wednesday morning shift, Mr. Ricardo Gomez, 55, and Mrs. Nenita Pascual, 69, both dialyzing through tunneled catheters at stations 3 and 4, start to shiver. Mr. Gomez&rsquo;s chills began about twenty minutes after connection. Mrs. Pascual&rsquo;s began at two hours. The patient at station 5 is well.</p>
<p>The supply officer mentions that a new lot of bicarbonate concentrate and a new brand of catheter-locking solution arrived on Monday.</p>
""", "questions": ["What do you do first, and for whom?",
                  "What three groups of causes are you considering, and how does the timing help?",
                  "What do you record and preserve, and who decides what happens next?"]},
    "sections": [
        ("why", "Why dialysis", "Why dialysis patients and units are prone to infection", """
<p><strong>The host.</strong> Kidney failure weakens white cell function. Diabetes, poor nutrition, and iron therapy add to it. Vaccines work less well, which is why hepatitis B vaccination uses higher doses and antibody levels are rechecked.</p>
<p><strong>The portal.</strong> A patient with a fistula has the skin broken by a needle about 300 times a year. A patient with a catheter has a plastic tube open to the bloodstream all the time.</p>
<p><strong>The environment.</strong> Hepatitis B virus survives on surfaces for days at high concentrations and spreads through invisible blood on shared equipment. That durability, not the severity of the disease, is why hepatitis B alone needs a dedicated room, machine, supplies, and staff. Hepatitis C is less hardy. Guidelines do not recommend isolating it and rely on strict standard precautions, because outbreaks have been traced to lapses such as shared medicine vials and poor station cleaning.</p>
<p><strong>The fluid.</strong> Gram-negative water organisms grow in stagnant water, bicarbonate concentrate, and reused containers. Module 6 covers the water system.</p>
{{fig:hn05_hub}}
"""),
        ("core", "Core interventions", "The core interventions and what they achieved", """
<p>The United States Centers for Disease Control and Prevention (CDC) groups its recommendations for dialysis units into a set of core interventions.[[hn_cdc_core]]</p>
{{fig:hn05_core}}
{{cards:The core interventions|Surveillance::Track bloodstream infections monthly and feed the results back to staff.|Hand hygiene::Observe monthly and share the results.|Catheter and access care::Observe connection, disconnection, and dressing changes quarterly.|Staff competency::Train and assess at hire and at least once a year.|Patient education::Teach patients how infection starts and what to report.|Catheter reduction::Move patients to a fistula or graft where possible.|Skin antisepsis::Chlorhexidine with alcohol, or povidone-iodine if the patient cannot tolerate it.|Scrub the hub::Clean the catheter hub with antiseptic every time it is opened.|Exit-site ointment::Apply antimicrobial ointment at dressing changes, as the unit&rsquo;s policy directs.}}
<p>In a United States collaborative, facilities that adopted these together saw bloodstream infections fall from 1.09 to 0.89 per 100 patient-months, and access-related infections from 0.73 to 0.42. The modeled decreases were 32% and 54%.[[hn_patel2013]] There was no control group, and the facilities were volunteers, so the real effect may be smaller. It is still the best evidence that putting the whole bundle into practice, rather than any single product, lowers the rate.</p>
<p>The Philippine cohort in Module 4 reported 6.72 catheter infections per 1,000 catheter-days, mostly gram-negative.[[hn_pasilan2024]] That is roughly ten times the control-arm rate in a United States cap trial, a different setting with a different case definition.[[hn_hymes2017]] It comes from one center, which is exactly why you need your own number.</p>
"""),
        ("floor", "On the floor", "Making the shoreline real", """
<p><strong>Medicines.</strong> Draw up medicines in a clean area away from the stations, never at the chair. Single-dose vials are for one patient. Multidose vials are dated, stay in the clean area, and never go to a station. Nothing returns from a station to clean supply.</p>
<p><strong>Turnover.</strong> A station is ready only when the last patient has left, all disposables are gone, and every surface has been wiped with the approved disinfectant and stayed wet for its full contact time. If the gap between shifts is shorter than that takes, the schedule is the hazard. Fix the schedule, not the nurse.</p>
<p><strong>Hepatitis B.</strong> Confirm with the infection prevention lead that screening, vaccination, and the dedicated room, machine, supplies, and staff assignment can actually be delivered with today&rsquo;s roster. A policy the roster cannot staff is not in force.</p>
{{key:Watch, do not ask. A nurse asked whether she cleaned the hub will say yes. A nurse watched for twenty minutes will show you what actually happens.}}
"""),
        ("numbers", "Honest numbers", "Reporting audits and rates honestly", """
<p>Stand where you can see five stations for twenty minutes. Count every hand-hygiene opportunity and how many were met. Watch one catheter connection and one cannulation against the checklist. Give feedback the same shift, in private, about the specific step.</p>
{{formula:<strong>Compliance</strong> = opportunities met &divide; opportunities observed.<br>18 of 24 = 75%. With only 24 observations, the 95% confidence interval runs from about 55% to 88%.<br>8 of 10 = 80%, with an interval from about 49% to 94%. Ten observations tell you almost nothing.}}
<p>Aim for at least 30 observations before comparing one month with another.</p>
{{formula:<strong>Infection rate</strong> = events &divide; patient-months &times; 100.<br>3 bloodstream infections in 95 patients over one month = 3.2 per 100 patient-months.<br><strong>Catheter rate</strong> = events &divide; catheter-days &times; 1,000.<br>2 infections in 30 catheter patients over 30 days = 2.2 per 1,000 catheter-days.}}
<p>Use the same case definition every month, or the trend means nothing. Post the results where staff can see them, without patient names.</p>
"""),
        ("cluster", "A possible cluster", "When two patients shiver on the same shift", """
<p>Two events on one shift may be chance. They may also be the first sign of a shared source. Patients come first, then the investigation, and the two run together.</p>
{{fig:hn05_timing}}
{{flow:Possible cluster|Patients::Assess each patient. The physician orders cultures and treatment.|Timing::Chills in the first hour suggest a pyrogenic reaction from fluid or a product. Later onset suggests a bloodstream infection.|Notify::Infection prevention lead, the water or biomedical lead, the clinical head.|Preserve::Quarantine new lots. Keep vials, concentrates, and lines. Record lot numbers.|Line list::Patient, station, machine, access, nurse, medicines, lot numbers, time of onset.|Decide::Clinical leadership and infection prevention decide testing, case definition, and reporting.}}
{{call:Stop and call the attending nephrologist, the clinical head, and the infection prevention lead when more than one patient develops fever or chills on the same day. Tell the water or biomedical lead at once if onset was early in the session. Follow your unit&rsquo;s protocol while you call.}}
"""),
    ],
    "debrief": ["""
<p><strong>First, and for whom?</strong> Both patients. Assess them, call the physician on duty, and follow orders for blood cultures and treatment. The physician decides whether to stop dialysis. Check the patient at station 5 and the others on the shift for symptoms.</p>
<p><strong>Three groups of causes.</strong> Hands and hubs, a product, or water and dialysis fluid. Mr. Gomez&rsquo;s chills began twenty minutes after connection, which points toward a pyrogenic reaction from fluid or a product. Mrs. Pascual&rsquo;s began at two hours, which fits a bloodstream infection from the catheter. They may have different causes. Both catheter patients, and a new locking solution, keep the hub on the list. A new bicarbonate lot keeps the fluid on the list.</p>
<p><strong>Record and preserve.</strong> Quarantine the new concentrate lot and the new locking solution. Keep the opened containers and the lines. Build the line list now, while staff remember. Notify the infection prevention lead and the water lead. Testing, case definitions, and any external report are decisions for the clinical head and infection prevention. Your part is to make sure the evidence still exists when they ask for it.</p>
"""],
    "skills": {"title": "Observation audit and feedback",
               "intro": "Observe a real or simulated shift for twenty minutes and give feedback to one nurse while your facilitator observes.",
               "items": [
                   ("Positions herself to see several stations without interrupting care.", False),
                   ("Counts each hand-hygiene opportunity and each one met, using a consistent definition.", True),
                   ("Observes one catheter connection against the checklist, including hub scrubbing.", True),
                   ("Reports the result as a fraction and percentage, and states why a small sample is uncertain.", True),
                   ("Gives private feedback about one specific observed step, linked to patient risk.", True),
                   ("Asks what made the correct step difficult.", False),
                   ("Proposes one change to the setup or workflow.", False),
                   ("Calculates a bloodstream infection rate with the correct denominator.", True),
                   ("Describes the first steps for a possible cluster, putting patient care first.", True),
               ],
               "placement": "Run one hand-hygiene observation of at least 30 opportunities each week for four weeks. Post the results, without names, and discuss the trend with your facilitator."},
    "quiz": [
        ("Why does hepatitis B need a dedicated room, machine, and staff?",
         ["It is always fatal", "It survives on surfaces for days at high concentrations", "Hepatitis C is not spread by blood", "It is a PhilHealth rule"], 1,
         "Durability on surfaces drives spread through shared equipment."),
        ("Why is hepatitis C not isolated?",
         ["It is not infectious", "Guidelines rely on strict standard precautions, because it is less hardy", "It cannot be detected", "Isolation is too costly"], 1,
         "Outbreaks have followed lapses such as shared vials."),
        ("For catheters used for months, where should prevention effort focus most?",
         ["The dressing color", "The hub, each time it is opened", "The patient&rsquo;s diet", "The blood pump"], 1,
         "Most long-term catheter infections start inside the lumen."),
        ("Eighteen of 24 hand-hygiene opportunities were met. What should the audit report?",
         ["18%", "24%", "75%", "133%"], 2,
         "18 &divide; 24. The interval is wide because the sample is small."),
        ("What goes in the denominator of a hand-hygiene audit?",
         ["Only the opportunities missed", "All observed eligible opportunities", "The number of nurses", "The number of patients"], 1,
         "Every observed opportunity counts."),
        ("Why are 10 observations too few?",
         ["They take too long", "The 95% confidence interval is too wide to compare months", "They are always biased", "They cannot be calculated"], 1,
         "Eight of ten has an interval from about 49% to 94%."),
        ("Three bloodstream infections occur among 95 patients in one month. What is the rate?",
         ["0.3 per 100 patient-months", "3.2 per 100 patient-months", "32 per 100 patient-months", "95 per 100 patient-months"], 1,
         "3 &divide; 95 &times; 100."),
        ("What did the United States collaborative report?",
         ["No change", "A 54% modeled fall in access-related bloodstream infection, without a control group", "A randomized 54% fall", "A rise in infections"], 1,
         "No control group, and volunteer facilities, so the true effect may be smaller."),
        ("Two patients develop chills twenty minutes after connection. Which cause is most likely?",
         ["Late bloodstream infection", "A pyrogenic reaction from fluid or a product", "Anxiety", "Low blood sugar"], 1,
         "Early onset points to the fluid or a product."),
        ("What is the first priority when symptoms cluster?",
         ["Write the incident report", "Assess and treat the patients, then escalate and contain", "Close the unit", "Call the supplier"], 1,
         "Patients first, with the investigation running alongside."),
        ("Where should medicines be drawn up?",
         ["At the chair", "In a clean area away from the stations", "On the machine top", "At the nurses&rsquo; station next to used supplies"], 1,
         "Medicine preparation stays inside the clean boundary."),
        ("The gap between shifts is too short to clean stations properly. What is the fix?",
         ["Clean faster", "Change the schedule", "Skip disinfection on busy days", "Use more disinfectant"], 1,
         "When the schedule makes the process impossible, the schedule is the hazard."),
        ("What should you preserve when a new lot may be the source?",
         ["Nothing until results return", "The opened containers, lines, and lot numbers", "Only the patient charts", "Only the invoices"], 1,
         "Evidence must still exist when the investigation asks for it."),
        ("Why should infection results be posted for staff?",
         ["To name nurses who erred", "Feedback is one of the core interventions", "It is required by PhilHealth", "To impress visitors"], 1,
         "Surveillance with feedback to staff is part of the bundle."),
        ("Two catheter infections occur among 30 catheter patients over 30 days. What is the rate per 1,000 catheter-days?",
         ["0.2", "2.2", "6.7", "22"], 1,
         "2 &divide; 900 &times; 1,000 = 2.2."),
    ],
    "terms": [("Bloodstream infection", "Organisms growing in the blood, shown by a positive blood culture."),
              ("Pyrogenic reaction", "Fever and chills from fragments of bacteria in the fluid."),
              ("Biofilm", "A slimy layer of organisms that grows on plastic surfaces."),
              ("Patient-month", "One patient followed for one month."),
              ("Catheter-day", "One patient with a catheter for one day."),
              ("Contact time", "How long a disinfectant must stay wet on a surface to work."),
              ("Line list", "A table of affected patients and their possible exposures, used to look for a shared source."),
              ("Confidence interval", "The range within which the true value probably lies, given the size of the sample.")],
    "readings": [("dialysis-access-infection.html", "Access infection, its signs, and its prevention."),
                 ("dialysis-water-treatment-systems.html", "How water systems can carry infection."),
                 ("dialysis-qapi-vs-cqi.html", "Using surveillance data to improve.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c5", "calc-dialysis-head-nurse-toolkit.html#c6"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
