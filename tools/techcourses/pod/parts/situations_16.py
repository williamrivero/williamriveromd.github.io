# -*- coding: utf-8 -*-
"""On-the-floor situations for Physician on Duty, Module 16. All scenarios are fictional."""

SITUATIONS = {"16": {
    "scenarios": [
        ("The alarm that keeps being silenced",
         "A machine&rsquo;s arterial pressure alarm has sounded four times in ten minutes. Each time a busy staff member resets it. The patient now says her upper abdomen hurts.",
         "A kinked or partly blocked line may be damaging red cells as the pump forces blood through the narrow point. Repeated alarms were the early warning.",
         "Go to the chair. Look at the color of the blood in the venous line and trace the tubing for a kink. If hemolysis is possible, have the pump stopped and the lines clamped, do not return the blood, follow the unit protocol, and call the attending nephrologist.",
         "An alarm that returns after a reset is a finding. Resetting it without finding the cause removes the machine&rsquo;s protection."),
        ("Cold arm, warm blanket",
         "An elderly man with dementia is restless and cold. His daughter tucks a blanket over his fistula arm. Twenty minutes later he is pale and drowsy, and the machine shows no alarm.",
         "The venous needle may have come out under the blanket. The venous pressure can fall too little to trigger the alarm.",
         "Lift the blanket. If the needle is out, have the pump stopped and the line clamped, press on the needle site, lay him flat, and follow the unit&rsquo;s blood loss protocol while someone calls the attending nephrologist.",
         "Severe blood loss can occur within minutes. A visible access is the only monitor that always works."),
        ("Itching in the third minute",
         "A new patient on his first session with a new dialyzer model says his palms itch and his chest feels tight three minutes after the start. His voice sounds hoarse.",
         "An early, severe (type A) dialyzer reaction, which is a form of anaphylaxis.",
         "Have dialysis stopped and the lines clamped at once. The blood is not returned. Start the unit&rsquo;s anaphylaxis protocol, call for help, and call the attending nephrologist. Keep the dialyzer and its packaging.",
         "Returning the circuit blood would deliver more of the trigger. Minutes matter for the airway."),
        ("Froth in the chamber during a power dip",
         "After a brief power interruption a staff member begins to return blood by hand. You see froth in the venous chamber and a line of small bubbles moving toward the patient.",
         "During manual return the machine&rsquo;s air detector and venous clamp do not protect the patient.",
         "Say &ldquo;stop&rdquo; and have the venous line clamped. Blood with air in the line is not returned. If the patient coughs or becomes breathless, treat as air embolism per protocol and call the attending nephrologist.",
         "The person turning the handle is the only air detector during a manual return."),
        ("Two chairs, same headache",
         "Within ten minutes, two patients in the same row report headache and nausea. A third, across the aisle, is vomiting. All started within the same half hour.",
         "A shared cause is likely: the water, the dialysis fluid, or a common batch of supplies.",
         "Treat it as a cluster event. Have the charge nurse stop treatments per the cluster protocol and hold new starts. Ask the technician to check the water and dialysis fluid now. Call the Medical Director and the attending nephrologists.",
         "The second and third patients are the diagnosis. Waiting for a fourth costs time for everyone still connected."),
    ],
    "tips": [
        "On every walk around the floor, look at three things at each chair: the patient&rsquo;s face, the access, and the color of the blood in the lines.",
        "Ask that needle sites and line connections stay uncovered. Offer a second blanket for the rest of the body instead.",
        "Learn where the clamps are and where the hand crank is stored on your unit&rsquo;s machines before you need them.",
        "When you decide that blood is not returned, say it aloud to the nurse and write the reason. It avoids a well-meant rinse-back.",
        "Keep what failed. The dialyzer, the lines, the packaging with lot numbers, and a sample of the dialysis fluid are evidence the Medical Director will need.",
    ],
}}
