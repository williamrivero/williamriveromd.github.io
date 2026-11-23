# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A biomedical technician placing an out-of-service tag on a hemodialysis machine.",
    "objectives": [
        "Describe what a biomedical technician in a dialysis center is responsible for, and what belongs to others.",
        "Protect yourself and others from blood, electricity, water, and chemicals while you service equipment.",
        "Take a machine out of use and hand it back in a way that no one can misunderstand.",
        "Explain why a dialysis machine may be serviced only by the manufacturer&rsquo;s method.",
    ],
    "big": """
{{plain:Think of a dialysis machine as a carinderia kitchen, a barangay pump station, and a building inspector packed into one cabinet. It mixes a fluid, it moves blood, and it shuts itself down when something is wrong. Your work is to make sure that what the screen says is true and that the shut-down systems still work. You do this for patients you may never meet, so the proof of your work lives in your records.}}
<p>The picture has a limit. A cook tastes the food, and a building inspector can see a crack with his own eyes. The machine has neither. It knows only what its sensors tell it, and it trusts them completely. A sensor that has drifted, or a protection that has been bypassed by a careless repair, leaves the machine confident and wrong. That is why the people who maintain it matter as much as the machine itself.</p>
{{cards:Key terms for this module|Medical device::Equipment made for diagnosis or treatment, built and maintained under strict rules.|Service manual::The manufacturer&rsquo;s technical document for maintaining and repairing one machine model.|Out of service::Formally removed from patient use, with a tag that says so.|Return to service::The documented decision that a machine is safe to use again.|Lockout/tagout::Locking and labeling an energy source so that a machine cannot start while you work on it.|Decontamination::Cleaning and disinfecting equipment so that it is safe to handle.}}
""",
    "case": {
        "title": "A quick look between shifts",
        "html": """
<p>It is a Tuesday, a few minutes before the noon shift. The nurse, Ms. Liza Domingo, stops the biomedical technician, Mr. Paolo Garcia, in the corridor. Machine 4 gave two conductivity alarms during the morning session, and she asks him to &ldquo;take a quick look&rdquo; before the next patient arrives.</p>
<p>Mr. Garcia opens the rear panel while the machine is still plugged in and still wet from its rinse. He finds a loose connector, pushes it back into place, and closes the panel. The whole job takes five minutes. The machine passes its self-test. Ms. Domingo asks, &ldquo;So it is fine for the next patient?&rdquo;</p>
""",
        "questions": ["What risks did the technician take in those five minutes?",
                      "Does a passed self-test answer the nurse&rsquo;s question?",
                      "What should happen before this machine is used again?"],
    },
    "sections": [
        ("role", "The role", "What the role covers", """
<p>Several people touch one dialysis machine in a single day. Each of them decides something different, and the machine is safe only when each decision is made by the right person.</p>
{{cards:Who does what around a machine|Hemodialysis technician and nurse::Operate the machine, run the checks before each use, and report faults.|Biomedical technician::Maintains, calibrates, tests, repairs, and documents. Decides whether the machine is technically fit.|Manufacturer or distributor::Provides the service manual, training, parts, and software, and handles complex repairs.|Charge nurse and medical director::Accept the machine back into clinical use and decide clinical matters.}}
<p>Notice the line between &ldquo;technically fit&rdquo; and &ldquo;used on a patient.&rdquo; You certify the first. The clinical team decides the second. Neither side can do the other&rsquo;s part.</p>
<p>Dialysis machines are built to international safety standards. Among other things, these standards require independent protective systems for temperature, conductivity, air, blood leak, and fluid removal.[[iec60601]][[iec60601_2_16]] Those protections hold only if the machine is maintained the way its maker specifies. An unapproved part, a skipped step, or an improvised repair can quietly remove a protection that the operator still believes is there. Nothing on the screen will tell anyone it is gone.</p>
{{key:If it is not in the service manual, do not do it. If you are not trained on the model, do not open it.}}
"""),
        ("hazards", "Hazards", "Four hazards and how to control them", """
<p>A dialysis machine brings together four things that can hurt you: blood from patients, mains electricity, hot water under pressure, and strong chemicals. Each one has a simple control, and each control must be in place before your hands go inside the cabinet.</p>
{{cards:Hazards in dialysis equipment work|Blood and body fluids::Treat every machine that has been in clinical use as contaminated. Disinfect it before service, wear gloves and eye protection, and clean your hands afterward.|Electricity::Mains voltage and water share one cabinet. Unplug and lock out before you open it, unless the manual calls for a powered test.|Hot water and pressure::Heat disinfection cycles and internal heaters can scald. Let the machine cool and release its pressure first.|Chemicals::Disinfectants and descalers burn skin and eyes, and some release toxic gas if they are mixed. Read the safety data sheet.}}
{{fig:machine_categories|Machines are assigned to patient groups by hepatitis status. Know a machine&rsquo;s assignment before you move or service it, and return it to the same area.}}
{{flow:Before you open a machine|Confirm status::No patient is connected, the nurse knows, and the machine is tagged out of service.|Decontaminate::Run the disinfection program and wipe the outside surfaces.|Isolate::Switch off, unplug, close the water supply, and lock out.|Protect::Wear gloves and eye protection, and keep your hands and the floor dry.|Work by the manual::Use the right model, the right revision, and the right tools.}}
<p>One hazard is invisible and harms the machine, not you. A static spark from your body can destroy a circuit board without leaving any mark. Wear a grounded wrist strap and keep boards in antistatic bags whenever you handle them.</p>
"""),
        ("tagging", "Out of service", "Taking a machine out and bringing it back", """
<p>In a busy unit, most equipment errors are really communication errors. A faulty machine is wheeled back to the floor because nobody knew it was faulty. A repaired machine is used before its tests are finished. The fault was never hidden on purpose. The status simply did not travel from one person to the next.</p>
<p>Tags and handovers fix this. They make the machine&rsquo;s status visible to anyone who walks past, without depending on anyone&rsquo;s memory.</p>
{{flow:The life of a fault|Reported::The operator records the exact message and what was happening at the time.|Tagged::A visible out-of-service tag goes on, with the date, the reason, and a name.|Diagnosed and repaired::An authorized technician does the work, by the manual.|Tested::Function, alarm, calibration, and safety tests, as the manual requires after that repair.|Disinfected::Before the machine returns to the floor.|Released::The service record is completed, the technician removes the tag, and the charge nurse accepts the machine.}}
{{stop:A machine that passes its self-test after an unexplained fault is not cleared. Self-tests check that alarms work. They do not find the cause of this morning&rsquo;s problem.}}
"""),
        ("records", "Why records", "Why your records matter", """
<p>A service record is the only evidence that a machine was safe on a given day. Regulators inspect it, clinicians rely on it, and the next technician starts from it.[[doh2012]][[who_maint]] Write what you found and what you did. Write which parts and which test instruments you used, what you measured before and after the work, and who accepted the machine back. If it is not written down, it did not happen.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What risks did the technician take?</strong> Four, in five minutes. He worked on a live, wet machine without isolating it from power and water. He handled the inside of a machine in clinical use without confirming that it had been disinfected. He made a repair without the manual. He left no record. Any one of these could injure him, or leave the next technician without a history to work from.</p>
<p><strong>Does a passed self-test answer the nurse&rsquo;s question?</strong> No. The loose connector may well have been the cause, but nobody yet knows whether conductivity is now measured correctly. The self-test shows that the alarms respond. It does not show that the reading behind them is true.</p>
<p><strong>What should happen before the machine is used again?</strong> Tag it out of service. Disinfect it, isolate it, and inspect it properly. Verify conductivity against a reference meter as the manual states. Run the required alarm tests. Write the service record, and release the machine formally to the charge nurse. In the meantime, the next patient uses another machine that has passed its own checks. Tell Ms. Domingo exactly that, so that she can plan the station.</p>
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
