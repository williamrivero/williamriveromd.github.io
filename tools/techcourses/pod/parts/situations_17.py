# -*- coding: utf-8 -*-
"""Situations and tips for Physician on Duty, Module 17. Fictional and original.
Each scenario: (title, what you see, what is likely going on, what to do, why it matters)."""

SITUATIONS = {"17": {
    "scenarios": [
        ("Three chills in one hour",
         "On the morning shift, three patients on machines of the same model begin shivering within the first hour. Two have fistulas and one has a catheter. None felt unwell on arrival.",
         "Several patients with the same symptom at the same time point to a shared cause: contaminated water, dialysis fluid, or a solution used on the floor. A pyrogenic reaction is more likely than three separate infections.",
         "Say aloud that this is a possible cluster. Follow the unit&rsquo;s cluster protocol, hold new starts on the affected machines, and do not return blood until the attending nephrologist advises. Draw blood cultures from each patient, call the attending nephrologist, and inform the Medical Director at once.",
         "A cluster is a unit problem. Treating each patient alone leaves the source in place for the next shift."),
        ("Rigors at the moment of connection",
         "A man with a tunneled catheter starts shaking within minutes of the catheter being flushed and connected. He was well on arrival. His exit site looks clean.",
         "Rigors soon after a catheter is opened and flushed raise suspicion that bacteria in the catheter lumen were pushed into the blood. A clean exit site does not exclude infection inside the catheter.",
         "Check his pressure, breathing, and mentation. Have cultures drawn from the catheter hub and the circuit, per protocol, before any antibiotic. Call the attending nephrologist and confirm the antibiotic order.",
         "The timing is a clue, not a test. The cultures and the attending nephrologist&rsquo;s plan decide the rest."),
        ("No fever, but something is wrong",
         "An elderly woman with diabetes and a catheter is quieter than usual. Her temperature is normal. Her pressure is lower than her usual pre-dialysis reading, and her breathing is fast.",
         "Fever may be blunted in kidney failure and in older patients. Low pressure, fast breathing, and a change in mentation can be the first signs of sepsis.",
         "Stop fluid removal if the pressure is low, per protocol. Screen for sepsis and draw cultures. Call the attending nephrologist and describe the change from her baseline, not only the temperature.",
         "Waiting for a fever before acting loses time in the patients who are least able to mount one."),
        ("Back pain after last month&rsquo;s bacteremia",
         "A man treated for a <em>Staphylococcus aureus</em> catheter infection four weeks ago now has new low back pain. He has a low-grade fever today.",
         "Bacteria that reached the blood may have settled in a disc or vertebra. Spine infection is easy to miss because back pain is common.",
         "Examine his back, legs, and bladder function, and ask about weakness or numbness. Call the attending nephrologist the same day and report the earlier bacteremia. Any new weakness or numbness is an emergency.",
         "A delayed diagnosis can leave permanent weakness. The earlier bacteremia is the key to the story."),
        ("Pus at the exit site",
         "A woman&rsquo;s catheter exit site is red, and pus appears when the dressing is removed. She has no fever and her pressure is normal.",
         "This is an exit-site infection, and the pus is a sign that the catheter may need to come out. Module 10 covers local catheter care.",
         "Have the pus swabbed and blood cultures drawn per protocol. Call the attending nephrologist before the session starts. Do not decide alone whether to use the catheter today.",
         "A catheter with pus at its exit is a door that is already open. The plan for the catheter belongs to the nephrologist."),
    ],
    "tips": [
        "When a patient shivers, look around the floor before you look at the chart.",
        "Write the clock time on every culture bottle and on the first antibiotic dose. The gap between them is a quality measure.",
        "Ask every febrile dialysis patient about back pain and listen for a new murmur.",
        "Treat each arm vein as a future fistula. Draw from the catheter and the circuit unless the protocol says otherwise.",
        "At handover, name every patient on antibiotics for a bloodstream infection and the date their cultures were drawn.",
    ],
}}
