# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A biomedical technician placing an out-of-service tag on a hemodialysis machine.",
    "objectives": [
        "Describe what a biomedical technician in a dialysis center is and is not responsible for.",
        "Protect yourself and others from blood, electricity, water, and chemicals while servicing equipment.",
        "Take a machine out of use and hand it back in a way that cannot be misunderstood.",
        "Explain why a dialysis machine may only be serviced by the manufacturer&rsquo;s method.",
    ],
    "big": """
{{plain:A dialysis machine is a kitchen, a pump station, and a safety inspector in one cabinet. It mixes a fluid, moves blood, and stops itself when something is wrong. Your job is to make sure that what the machine displays is true and that its safety systems still work. You do this for people you may never meet, so the proof is in your records.}}
{{cards:Key terms for this module|Medical device::Equipment made for diagnosis or treatment, built and maintained under strict rules.|Service manual::The manufacturer&rsquo;s technical document for maintaining and repairing one machine model.|Out of service::Formally removed from patient use, with a tag that says so.|Return to service::The documented decision that a machine is safe to use again.|Lockout/tagout::Locking and labeling an energy source so a machine cannot start while you work on it.|Decontamination::Cleaning and disinfecting equipment so it is safe to handle.}}
""",
    "case": {
        "title": "A quick look between shifts",
        "html": """
<p>Between shifts a nurse asks the technician to &ldquo;take a quick look&rdquo; at a machine that gave two conductivity alarms that morning. The technician opens the rear panel while the machine is still plugged in and wet from a rinse, finds a loose connector, pushes it back, and closes the panel. The machine passes its self-test. The nurse asks, &ldquo;So it is fine for the next patient?&rdquo;</p>
""",
        "questions": ["What risks did the technician take in those five minutes?",
                      "Does a passed self-test answer the nurse&rsquo;s question?",
                      "What should happen before this machine is used again?"],
    },
    "sections": [
        ("role", "The role", "What the role covers", """
{{cards:Who does what around a machine|Hemodialysis technician and nurse::Operate the machine, run pre-use checks, and report faults.|Biomedical technician::Maintains, calibrates, tests, repairs, and documents. Decides whether the machine is technically fit.|Manufacturer or distributor::Provides the service manual, training, parts, and software, and handles complex repairs.|Charge nurse and medical director::Accept the machine back into clinical use and decide clinical matters.}}
<p>The line between &ldquo;technically fit&rdquo; and &ldquo;used on a patient&rdquo; matters. You certify the first. The clinical team decides the second. Neither can do the other&rsquo;s part.</p>
<p>Dialysis machines are built to international safety standards that require, among other things, independent protective systems for temperature, conductivity, air, blood leak, and fluid removal.[[iec60601]][[iec60601_2_16]] Those protections only hold if the machine is maintained the way its maker specifies. Using an unapproved part, skipping a step, or improvising a repair can silently remove a protection that the operator still believes is there.</p>
{{key:If it is not in the service manual, do not do it. If you are not trained on the model, do not open it.}}
"""),
        ("hazards", "Hazards", "Four hazards and how to control them", """
{{cards:Hazards in dialysis equipment work|Blood and body fluids::Every machine that has been in clinical use is treated as contaminated. It is disinfected before service; you wear gloves and eye protection; hands are cleaned afterward.|Electricity::Mains voltage and water share one cabinet. Unplug and lock out before opening unless the manual calls for a powered test.|Hot water and pressure::Heat disinfection cycles and internal heaters can scald. Let the machine cool and depressurize.|Chemicals::Disinfectants and descalers burn skin and eyes and can release toxic gas if mixed. Read the safety data sheet.}}
{{fig:machine_categories|Machines are assigned to patient groups by hepatitis status. Know a machine&rsquo;s assignment before you move or service it, and return it to the same area.}}
{{flow:Before you open a machine|Confirm status::No patient connected; nurse informed; machine tagged out of service.|Decontaminate::Run the disinfection program; wipe external surfaces.|Isolate::Switch off, unplug, close the water supply, and lock out.|Protect::Gloves, eye protection, and dry hands and floor.|Work by the manual::Right model, right revision, right tools.}}
<p>Static electricity can destroy circuit boards without any visible sign. Use a grounded wrist strap and antistatic bags when handling boards.</p>
"""),
        ("tagging", "Out of service", "Taking a machine out and bringing it back", """
<p>Most equipment errors in a busy unit are communication errors: a faulty machine wheeled back to the floor because nobody knew it was faulty, or a repaired machine used before its tests were done. Tags and handovers exist to make the status visible to anyone who walks past.</p>
{{flow:The life of a fault|Reported::The operator records the exact message and what was happening.|Tagged::A visible out-of-service tag with date, reason, and name.|Diagnosed and repaired::By an authorized technician, by the manual.|Tested::Function, alarms, calibration, and safety tests as the manual requires after that repair.|Disinfected::Before returning to the floor.|Released::Service record completed; tag removed by the technician; charge nurse accepts the machine.}}
{{stop:A machine that passes its self-test after an unexplained fault is not cleared. Self-tests check that alarms work. They do not find the cause of this morning&rsquo;s problem.}}
"""),
        ("records", "Why records", "Why your records matter", """
<p>A service record is the only evidence that a machine was safe on a given day. Regulators inspect it, clinicians rely on it, and the next technician starts from it.[[doh2012]][[who_maint]] Write what you found, what you did, which parts and test instruments you used, what you measured before and after, and who accepted the machine back. If it is not written down, it did not happen.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> In five minutes the technician worked on a live, wet machine without isolating it, handled internal parts of a machine in clinical use without confirming it had been disinfected, made a repair without the manual, and left no record. A loose connector may indeed have been the cause, but nobody yet knows whether conductivity is now measured correctly. A passed self-test does not answer the nurse&rsquo;s question. Before the next patient: tag the machine out of service; disinfect, isolate, and inspect it properly; verify conductivity against a reference meter as the manual states; run the required alarm tests; write the service record; and release it formally to the charge nurse. Meanwhile the patient uses another machine that has passed its own checks.</p>
"""],
    "skills": {
        "title": "Safe preparation for service and formal release",
        "intro": "Materials: an out-of-clinical-use machine, the service manual, tags, a lockout device, protective equipment, and blank service and release forms.",
        "items": [("Confirms with the charge nurse that the machine is free and records its identity and assigned area.", False),
                  ("Applies a visible out-of-service tag with date, reason, and name.", True),
                  ("Confirms the machine has completed disinfection before opening it.", True),
                  ("Switches off, unplugs, closes the water supply, and applies lockout.", True),
                  ("Wears gloves and eye protection and uses static protection when handling boards.", False),
                  ("Locates the correct service manual and revision for the model.", False),
                  ("States which tests are required after the simulated repair, by the manual.", True),
                  ("Completes the service record and obtains acceptance from the charge nurse before removing the tag.", True)],
        "placement": "Follow one real fault from report to release with a senior technician, and list every person who needed to know the machine&rsquo;s status.",
    },
    "quiz": [
        ("Who decides that a repaired machine is technically fit, and who accepts it for patient use?",
         ["The nurse decides both", "The biomedical technician certifies fitness; the charge nurse accepts it for clinical use", "The patient decides", "The supplier decides both"], 1,
         "Technical fitness and clinical use are separate decisions made by different people."),
        ("How should any machine that has been used on patients be regarded before service?",
         ["As clean", "As contaminated until disinfected", "As safe if it looks dry", "As broken"], 1,
         "Treat every used machine as contaminated: disinfect it, wear protective equipment, and clean hands afterward."),
        ("What is the purpose of lockout/tagout?",
         ["To hide a fault", "To prevent equipment from being energized while someone works on it", "To record working hours", "To speed up repairs"], 1,
         "Locking and labeling the energy source protects the person working inside."),
        ("A machine passes its self-test after an unexplained conductivity alarm. What does this prove?",
         ["The cause is fixed", "Only that the tested alarm functions work; the cause is still unknown", "The dialysate is correct", "Nothing was ever wrong"], 1,
         "Self-tests verify protective functions; they do not diagnose an earlier fault."),
        ("Why must repairs follow the manufacturer&rsquo;s service manual?",
         ["It is quicker", "Improvised repairs can remove a protection the operator still relies on", "Manuals are required for billing", "It is optional for experienced staff"], 1,
         "Safety depends on the machine being maintained exactly as designed."),
        ("What is the main purpose of an out-of-service tag?",
         ["Decoration", "To make the machine&rsquo;s status obvious to everyone so it is not used by mistake", "To record the price", "To mark it for sale"], 1,
         "Most equipment errors are communication errors."),
        ("Which practice protects circuit boards from static damage?",
         ["Working on carpet", "A grounded wrist strap and antistatic bags", "Wet hands", "Rubber gloves alone"], 1,
         "Static discharge can damage components without visible signs."),
        ("A machine assigned to the hepatitis B isolation area is repaired in the workshop. Where does it go afterward?",
         ["Any free station", "Back to the same assigned area", "To the general area", "To storage permanently"], 1,
         "Machine assignment is a clinical infection-control rule; servicing does not change it."),
    ],
    "terms": [("Self-test", "The automatic check a machine runs on its own alarms and sensors at start-up."),
              ("Service record", "The written history of everything done to one machine."),
              ("Safety data sheet", "The document listing a chemical&rsquo;s hazards and first aid."),
              ("Electrostatic discharge", "A small static shock that can damage electronics.")],
    "readings": [("dialysis-machine-assignment.html", "Why machines are assigned by hepatitis status."),
                 ("dialysis-qapi-vs-cqi.html", "How equipment faults are tracked in quality review.")],
}
