# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Receiving, storing and moving supplies so they stay sealed, dry, in date and clean; first in, first out; why you never open, sort or tidy clinical supplies; and the technical boundaries around machines, power, water and concentrates, with exactly what to report when something looks wrong.",
    "desc": "Housekeeping & Support Staff Module 13: supply receipt and storage, first in first out, damaged and expired items, clean supply rules, electrical and water hazards around dialysis machines, technical boundaries (machines, water treatment, concentrate, reprocessing) and fault reporting.",
    "keywords": "hospital supply storage first in first out, dialysis supplies storage orderly, dialysis machine fault reporting, electrical safety cleaning near medical equipment, support staff technical boundaries dialysis",
    "image_alt": "An orderly placing sealed boxes of dialysis supplies on a wire shelf off the floor in a bright storeroom, older stock moved to the front.",
    "objectives": [
        "Receive and store supplies so they stay sealed, dry, clean and within date, using first in, first out.",
        "Recognize damaged, wet or expired supplies and set them aside for the stock owner.",
        "Move heavy supplies using carts and safe lifting.",
        "State the technical boundaries: machine controls, connections, power, water system, concentrates and reprocessing.",
        "Report a machine, electrical or water fault quickly and clearly without touching the equipment.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "The sari-sari store shelf",
         "html": """
<p>A good sari-sari store owner puts new stock at the back and older stock in front, so nothing expires on the shelf. She keeps sacks of rice off the wet floor, closes the jars, and never sells a can that is dented and swollen. A dialysis unit&rsquo;s supply room works the same way, with one more rule: a sterile pack that got wet, crushed or opened is no longer sterile, however clean it looks.</p>
<p>The picture has a limit. In a store, a mistake costs some pesos. In a dialysis unit, a contaminated or expired item can reach a patient&rsquo;s bloodstream.</p>
"""},
        {"id": "storage", "nav": "Storage", "tag": "Practice", "h2": "Receiving and storing",
         "html": """
<ul>
<li><strong>Check on arrival.</strong> Count against the delivery list if assigned; look for crushed, wet, torn or opened boxes; report damage to the stock owner before signing anything.</li>
<li><strong>Store off the floor and away from walls and ceilings,</strong> on shelves that can be cleaned, away from sinks, windows that leak, and the dirty utility room. Your unit will specify heights and distances.</li>
<li><strong>First in, first out (FIFO).</strong> New stock behind, older stock in front, so the oldest dates are used first. Report items near their expiry date to the stock owner; do not throw them away yourself.</li>
<li><strong>Heavy at waist height.</strong> Store concentrate cartons, saline cases and other heavy items between knee and shoulder height (Module 12).</li>
<li><strong>Clean hands for clean supplies.</strong> Hand hygiene before handling clean stock; never bring a waste trolley or used items into the clean supply room (Module 5).</li>
<li><strong>Do not open, split or repack</strong> sterile or clinical supplies, and do not &ldquo;tidy&rdquo; the nurses&rsquo; prepared trays.</li>
</ul>
<div class="tc-stop"><span class="tc-lab">Set aside, label, report</span>A wet, crushed, torn, opened or expired package goes to a marked quarantine shelf or box, labeled &ldquo;Do not use,&rdquo; and the stock owner is told. Never decide to use it, and never discard it without telling anyone.</div>
"""},
        {"id": "machines", "nav": "Machines and power", "tag": "Scope and safety", "h2": "Machines, power and water",
         "html": """
<p>A hemodialysis machine is a medical device connected to the patient&rsquo;s blood, to treated water from the wall, and to mains power. Clinical and biomedical staff own it. Even when it is not in use, it may be running its own disinfection cycle with hot water or chemicals inside.</p>
<div class="table-wrap"><table>
<thead><tr><th>Never</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Press buttons, touch screens, silence alarms, or open panels</td><td>Settings and alarms protect the patient</td></tr>
<tr><td>Unplug a machine, move its power cord, or plug a floor polisher or kettle into its outlet</td><td>A machine may be running disinfection or be connected to a patient; overloading circuits can trip power to stations</td></tr>
<tr><td>Disconnect, reconnect or move water or drain hoses, or concentrate lines</td><td>Leaks, contamination, chemical burns</td></tr>
<tr><td>Move a machine unless assigned and trained</td><td>Damages hoses and connections</td></tr>
<tr><td>Spray liquid onto screens, vents or electrical parts</td><td>Electrical hazard and damage; use only the assigned method for external surfaces</td></tr>
</tbody></table></div>
<p>Water and electricity together are dangerous. If you see water spreading toward power outlets, cords or machines, keep people away, do not touch the equipment, and call the technician and nurse at once.</p>
"""},
        {"id": "report", "nav": "Reporting faults", "tag": "Practice", "h2": "Reporting a fault",
         "html": """
<p>You may be the first to notice that something is wrong. Report it the same way you report a patient concern: what, where, when, and stay if it is dangerous.</p>
<div class="tc-cards">
<div class="tc-card"><b>Report immediately</b>Smoke, burning smell, sparks, a hot or damaged power cord; water or fluid leaking from a machine, wall box or ceiling; an alarm with no staff nearby; a strong chemical smell; a broken chair with a patient in it.</div>
<div class="tc-card"><b>Report the same shift</b>Wobbly chair or table, torn chair cover, broken wheel or brake, flickering light, blocked sink, broken handrub dispenser, faulty call bell, damaged wall or floor.</div>
</div>
<p>Use the unit&rsquo;s fault log or repair request if one exists, and tell the person responsible. Do not try to repair anything yourself unless repair is in your written duties.</p>
"""},
        {"id": "boundaries", "nav": "Technical boundaries", "tag": "Scope", "h2": "Where technical work begins",
         "html": """
<p>Three areas belong entirely to trained technicians in separate Renal Care Academy pathways, and to licensed or designated staff: the <strong>water treatment system</strong> (testing, disinfection, filters, valves), <strong>concentrate preparation</strong> (mixing acid and bicarbonate solutions), and <strong>dialyzer reprocessing</strong> (cleaning and sterilizing filters for reuse). The Philippine Society of Nephrology guidelines treat water quality, equipment and reprocessing as areas needing qualified personnel and written procedures.[[psn2024]] Your role is to keep out unless assigned, keep routes and floors around them safe, and report what you see.</p>
<p>You may be asked to carry sealed concentrate containers or empty jugs; follow the waste plan for empties (Module 10) and lift safely (Module 12). Never pour, mix or decant concentrates.</p>
"""},
    ],
    "case": {
        "title": "The wet box",
        "html": """
<p><strong>Monday, 6:30 a.m.</strong> After an overnight typhoon, Ramon opens the storeroom. A ceiling tile has leaked onto the top shelf. Several boxes of sterile dressing packs and bloodlines are damp on the outside. The first shift starts in thirty minutes and the nurse asks him to bring a box of bloodlines.</p>
""",
        "acte": {
            "Notice": "Wet sterile and clinical packaging may be contaminated; a ceiling leak continues to threaten stock; first shift needs supplies.",
            "Communicate": "Tell the nurse which boxes are damp and that he will bring dry stock from the lower shelf; tell the stock owner and maintenance about the leak.",
            "Do": "Move dry stock out of the leak path with clean hands; set aside the damp boxes on a quarantine shelf labeled &ldquo;Do not use &ndash; wet&rdquo;; place a bucket and wet-floor sign; bring a dry, sealed box to the nurse.",
            "Escalate": "If dry stock is not enough for the day, the stock owner arranges emergency supply; the nurse decides about any items whose packaging is in doubt.",
        },
        "task": "Write the quarantine label and the maintenance report.",
        "outcome": """
<p>The nurse inspected the damp boxes and had the outer cartons removed: inner packs in sealed plastic were dry and usable after checking; paper-wrapped dressing packs were discarded. Maintenance fixed the tile by noon. The stock owner moved sterile items away from the top shelf for the rest of the rainy season.</p>
""",
    },
    "second_round": ("A patient&rsquo;s relative offers to help carry boxes from the delivery truck into the storeroom.",
                     "What you say and why, and how you move the boxes safely instead."),
    "evidence_out": "Observed FIFO restocking and quarantine labeling; fault-report role-play for one urgent and one routine fault.",
    "critical": "Using wet, opened or expired clinical supplies, unplugging or operating a dialysis machine, or touching water-system or concentrate equipment.",
    "reflect": "Where in your unit does water most often appear where it should not? Who owns that problem, and does everyone know whom to call?",
    "practice": {"intro": "Use your unit&rsquo;s storeroom and fault log.", "items": [
        "Restock one shelf using first in, first out and show your preceptor the expiry order.",
        "Set up a quarantine shelf and label a damaged item.",
        "Name the person responsible for supplies, machines, water treatment and maintenance on each shift.",
        "Complete a practice fault report for a broken wheelchair brake.",
        "Show which outlets you may use for cleaning machines and which you must never use.",
    ]},
    "readings": [("dialysis-water-treatment-systems.html", "How the water system works and why it is restricted."),
                 ("typhoon-disaster-preparedness-dialysis.html", "How units prepare for typhoons and floods.")],
    "calcs": ["calc-dialysis-support-staff-toolkit.html"],
    "terms": [("First in, first out", "Using the oldest stock first so nothing expires on the shelf."),
              ("Quarantine shelf", "A marked place where damaged, wet or doubtful items wait for the stock owner&rsquo;s decision."),
              ("Technical boundary", "The line beyond which machines, water systems, concentrates and reprocessing belong to trained technical staff.")],
    "quiz": [
        {"stem": "What does first in, first out mean?", "options": [
            ("Use the oldest stock first; new stock goes behind.", True, "Prevents expiry on the shelf."),
            ("The first person in the room takes supplies.", False, "No."),
            ("New stock is used first.", False, "Opposite."),
            ("Supplies are used in alphabetical order.", False, "No.")], "sources": []},
        {"stem": "A sterile pack is damp. What do you do?", "options": [
            ("Set it aside on the quarantine shelf, label it, and tell the stock owner or nurse.", True, "Wet packaging may be contaminated."),
            ("Dry it in the sun and use it.", False, "Sterility cannot be restored this way."),
            ("Throw it away without telling anyone.", False, "The owner must know."),
            ("Use it if it looks clean.", False, "Appearance is not a test.")], "sources": []},
        {"stem": "Where should heavy cartons be stored?", "options": [
            ("Between knee and shoulder height.", True, "Reduces lifting risk."),
            ("On the floor.", False, "Floor storage is a lifting and contamination risk."),
            ("On the top shelf.", False, "Lifting overhead is risky."),
            ("In the dirty utility.", False, "Not for clean supplies.")], "sources": ["waters1993"]},
        {"stem": "May you open and repack sterile supplies to save space?", "options": [
            ("No.", True, "Opening destroys sterility; clinical stock is not repacked by support staff."),
            ("Yes, with gloves.", False, "Still not allowed."),
            ("Yes, if supervised by another aide.", False, "Not allowed."),
            ("Only on weekends.", False, "Not allowed.")], "sources": []},
        {"stem": "A dialysis machine is alarming and no staff are nearby. What do you do?", "options": [
            ("Tell the nurse or technician immediately; do not touch it.", True, "Alarms are clinical and technical."),
            ("Press silence.", False, "Excluded."),
            ("Unplug it.", False, "Dangerous."),
            ("Ignore it.", False, "Must be reported.")], "sources": []},
        {"stem": "Where can you plug in a floor polisher?", "options": [
            ("Only in outlets your unit designates for cleaning equipment.", True, "Never in a dialysis machine outlet."),
            ("Any outlet, including a dialysis machine&rsquo;s.", False, "Can trip power to stations."),
            ("By unplugging a machine.", False, "Never."),
            ("Through an extension from the machine.", False, "Never.")], "sources": []},
        {"stem": "You see water spreading toward power cords near stations. First action?", "options": [
            ("Keep people away, do not touch equipment, and call the technician and nurse.", True, "Water and electricity together are dangerous."),
            ("Mop under the machines.", False, "Electrical risk."),
            ("Unplug the machines.", False, "Not your role; may endanger patients."),
            ("Put towels on the cords.", False, "Do not touch.")], "sources": []},
        {"stem": "Which is a technical boundary you must not cross?", "options": [
            ("Mixing or decanting dialysis concentrates.", True, "Technician work."),
            ("Restocking gloves.", False, "Allowed if assigned."),
            ("Reporting a broken chair.", False, "Everyone reports."),
            ("Mopping the storeroom floor.", False, "Allowed if assigned.")], "sources": ["psn2024"]},
        {"stem": "You smell burning near a machine. What do you do?", "options": [
            ("Report immediately to the nurse and technician and keep people back.", True, "Possible electrical fault or fire."),
            ("Look inside the machine.", False, "Never open panels."),
            ("Spray water on it.", False, "Electrical danger."),
            ("Wait to see if it gets worse.", False, "Report now.")], "sources": []},
        {"stem": "A delivery box arrives crushed. What do you do?", "options": [
            ("Report the damage to the stock owner before signing for it.", True, "Damaged deliveries are handled by the stock owner."),
            ("Sign and store it.", False, "Report first."),
            ("Open it to check.", False, "Report; the owner decides."),
            ("Return it yourself to the truck.", False, "Owner decides.")], "sources": []},
        {"stem": "A nurse&rsquo;s prepared tray is in your way. What do you do?", "options": [
            ("Ask the nurse to move it, or clean around it as she directs.", True, "Do not touch prepared clinical trays."),
            ("Move it to the floor.", False, "Contaminates it."),
            ("Tidy the items on it.", False, "Clinical."),
            ("Throw it away.", False, "Never.")], "sources": []},
        {"stem": "Why must you not spray liquid onto machine screens?", "options": [
            ("Liquid can damage electronics and create an electrical hazard.", True, "Use only the assigned method."),
            ("Screens are always sterile.", False, "Not the reason."),
            ("It makes the screen too clean.", False, "No."),
            ("Patients dislike it.", False, "Not the reason.")], "sources": []},
        {"stem": "Which fault should be reported the same shift (not an emergency)?", "options": [
            ("A wobbly side table.", True, "Routine repair."),
            ("Sparks from a cord.", False, "Immediate."),
            ("Water leaking from the ceiling onto machines.", False, "Immediate."),
            ("A burning smell.", False, "Immediate.")], "sources": []},
        {"stem": "Who works in the water treatment system?", "options": [
            ("Trained technicians under written procedures.", True, "Separate pathway."),
            ("Any aide on night shift.", False, "No."),
            ("Patients&rsquo; relatives.", False, "No."),
            ("Whoever finds a leak.", False, "Report; do not intervene.")], "sources": ["psn2024"]},
        {"stem": "A relative offers to help carry boxes. What do you say?", "options": [
            ("Thank them, decline, and use a cart or a trained colleague.", True, "Visitors are not trained or insured for this work, and supplies must stay clean."),
            ("Accept to save time.", False, "Risk to them and to supplies."),
            ("Let them carry the light ones.", False, "Still not appropriate."),
            ("Ask them to carry waste instead.", False, "Never.")], "sources": []},
    ],
    "exam": [
        {"stem": "A box of bloodlines is damp after a ceiling leak. What do you do?", "options": [
            ("Quarantine and label it, tell the nurse or stock owner, and bring dry stock.", True, "Owner decides."),
            ("Use it if the inner packs look fine.", False, "Not your decision."),
            ("Dry it with a fan.", False, "Does not restore sterility."),
            ("Throw it away silently.", False, "The owner must know.")], "sources": []},
        {"stem": "Which action crosses a technical boundary?", "options": [
            ("Unplugging a dialysis machine to plug in a polisher.", True, "Never."),
            ("Reporting a leak.", False, "Correct action."),
            ("Storing boxes off the floor.", False, "Correct."),
            ("Using FIFO.", False, "Correct.")], "sources": []},
        {"stem": "What is the safest response to a machine alarm with no staff in sight?", "options": [
            ("Find and tell the nurse or technician immediately without touching the machine.", True, "Get the right person."),
            ("Silence it.", False, "Excluded."),
            ("Turn it off.", False, "Excluded."),
            ("Wait.", False, "Delay.")], "sources": []},
    ],
}
