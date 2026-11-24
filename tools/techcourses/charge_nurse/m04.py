# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 04: The Live Board. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse standing still at the center of a busy dialysis unit, scanning the room while nurses work around her.",
    "objectives": [
        "Describe the three levels of situational awareness and give a dialysis example of each.",
        "Keep a live board that the whole team can read from the center of the floor.",
        "Round the floor at set times and look at the patient before the machine.",
        "Run a three-minute safety huddle at opening and at mid-shift.",
        "Protect high-risk tasks from interruption, and close every flag with an owner and a time.",
    ],
    "big": """
{{plain:A basketball point guard dribbles with one hand and keeps his head up. He knows where the other nine players are without staring at any one of them. If he looks down at the ball, the defense steals it.}}
<p>The point guard is a fair picture of situational awareness: noticing what is happening, understanding what it means, and expecting what comes next. A charge nurse doing her own difficult cannulation is looking at the ball. The board, the timed rounds, and the huddle are how she keeps her head up when her hands are busy.</p>
<p>The picture has a limit. A point guard sees the whole court at once. A dialysis floor hides its trouble: under a blanket, behind a curtain, inside a patient who is quietly drowsy. Awareness on a dialysis floor has to be built on purpose, with tools and habits, because the eye alone will miss things.</p>
{{cards:Key terms for this module|Situational awareness::Knowing what is happening around you, what it means, and what is likely to happen next.|Live board::A whiteboard with one line per chair, readable at a glance by the whole team.|Flag::Green steady, amber watch with a timed recheck, red act now.|Round::A timed walk past every chair, looking at the patient first.|Huddle::A three-minute standing meeting about what could hurt someone in the next hours.|Protected task::A task nobody interrupts except for an emergency.}}
""",
    "case": {"title": "&ldquo;Nobody told me Bed 7 was dropping&rdquo;", "html": """
<p>At 7:40 in the morning, Nurse Lea Santos, in charge of a 14-station unit, is placing needles in a difficult fistula at Bed 2. At Bed 7, the patient&rsquo;s pressure has fallen from 150 to 102 over forty minutes. The assigned nurse is at Bed 11, where a venous pressure alarm keeps sounding.</p>
<p>At 7:52 the man in Bed 7 says he feels faint. Lea hears about it at 7:55. There is no board on the wall; the assignment is on a sheet of paper on the desk.</p>
""", "questions": ["What failed: a person, or the way information moved?",
                  "What would a board and a mid-shift huddle have shown?",
                  "What should Lea change tomorrow?"]},
    "sections": [
        ("aware", "Three levels", "Seeing, understanding, predicting", """
<p>Situational awareness has three levels. <strong>Seeing</strong>: the pressure at Bed 7 is 102. <strong>Understanding</strong>: that is a 48-point drop for a man who usually tolerates fluid removal poorly. <strong>Predicting</strong>: unless fluid removal is reduced, he will faint in the next ten minutes.</p>
{{fig:cn04_awareness}}
<p>Most floor emergencies were visible at the first level long before anyone reached the third. The reading was on the screen; nobody with the time to think about it was looking. A charge nurse&rsquo;s job is to put the first-level information where someone will reach the second and third levels in time.</p>
"""),
        ("board", "The board", "The live board", """
<p>Give each chair one line: bed number, access type, the one key risk, fluid goal, start time, end time, and a flag column. Green means steady. Amber means watch, with a timed recheck by a named nurse. Red means act now. Use bed numbers or initials, not full names, if patients and visitors can see the board.</p>
{{fig:cn04_board}}
<p>The board is not a chart. It does not replace the treatment record. It is a picture the whole team can read from the center of the room in five seconds, so that the nurse walking past Bed 7 on the way to Bed 11 knows that Bed 7 is amber.</p>
{{scene:The board that paid for itself|<p>At a 20-station unit in Pampanga, the head nurse introduced a board after a month of near misses at shift change. Within a week, nurses began glancing at it on their way past. On the second Monday, an assistant noticed that Bed 15 was red (&ldquo;potassium result pending, physician to call&rdquo;) and that the patient was being walked to the scale for disconnection. She told the nurse. The result came back high, and the physician ordered a repeat before the patient left. Nobody had to remember; the board remembered for them.</p>}}
"""),
        ("rounds", "Rounds", "Rounds by the clock", """
<p>Walk the floor at set times: about fifteen minutes after the last connection, every hour after that, and thirty minutes before the first disconnection. Recheck amber chairs every fifteen minutes, or more often if your unit&rsquo;s protocol says so.</p>
<p>At each chair, look at the patient before the machine. Color, breathing, speech, sweat, the access uncovered and dry. Ask one question: &ldquo;How are you feeling?&rdquo; The machine shows numbers. The patient shows trouble first. A patient who is drowsy, sweaty, or silent may have low pressure, low blood sugar, or something worse (Module 7).</p>
{{key:Patient before machine. The screen tells you what was measured; the patient tells you what is happening.}}
"""),
        ("huddle", "Huddles", "Three-minute huddles", """
<p>A huddle is a short standing meeting with one question: what could hurt someone in the next hours, and who owns it? Run one at opening (assignment, flagged patients, closed gates, breaks) and one at mid-shift (amber and red flags, breaks still due, the second shift&rsquo;s first chairs).</p>
<p>How strong is the evidence? A systematic review of twelve studies found mostly positive effects of huddles on teamwork, engagement, and job satisfaction, but the studies were small and low in rigor.[[cn_rowan2022]] That is an honest picture: huddles are cheap, rarely harmful, and probably helpful, but they have not been shown to reduce adverse events. Keep them short, standing, and focused, so they stay cheap.</p>
{{scene:When a huddle becomes a complaint session|<p>The mid-shift huddle at a Bulacan unit drifts into the broken air conditioner and the canteen schedule. At minute four, the charge nurse says, &ldquo;Let&rsquo;s park those for the staff meeting. What could hurt someone before noon?&rdquo; Kris answers: Bed 9&rsquo;s catheter dressing is wet. Arnel: Bed 3&rsquo;s potassium result has not come back. Two owners, two times, back to the floor at minute five.</p>}}
"""),
        ("interrupt", "Interruptions", "Interruptions are a hazard", """
<p>In an observational study of nurses giving medicines on hospital wards, each interruption was associated with a 12.7% increase in clinical errors, and the most experienced nurses were not protected.[[cn_westbrook2010]] The study was not in dialysis, but the dialysis floor is full of interruptions: alarms, phone calls, patients asking for blankets.</p>
<p>Protect three tasks from interruption: medicine preparation (especially heparin and intravenous iron), the order-to-machine check before connection, and catheter connection. Agree on a signal your unit will use, such as a colored apron or a sign on the trolley, that means &ldquo;interrupt me only for an emergency.&rdquo; The charge nurse enforces it, including on physicians and visitors, politely.</p>
"""),
        ("close", "Closing flags", "Every flag gets an owner and a time", """
<p>An amber or red flag without a name is a wish. Every flag on the board has an owner (&ldquo;Kris&rdquo;) and a time (&ldquo;recheck 7:45&rdquo;). At the end of the shift, the board becomes the handoff: every open flag is either closed or passed to a named person on the next shift (Module 14).</p>
"""),
    ],
    "debrief": ["""
<p><strong>What failed.</strong> Nobody was careless. Information did not move, because there was no board, no timed round, and no rule for rechecking a patient known to drop his pressure. The assigned nurse was pulled to a noisy alarm, and nobody else knew Bed 7 needed watching.</p>
<p><strong>What a board and a huddle would have shown.</strong> At the 7:20 round, the board would have shown Bed 7 amber: &ldquo;drops after hour 1; fluid goal 3.2 L; started 6:20; recheck every 15 minutes, Kris.&rdquo; The 7:35 reading of 108 would have reached a nurse with time to act. A 7:30 mid-shift huddle would have handed Bed 11&rsquo;s recurring alarm to the technician, freeing the assigned nurse.</p>
<p><strong>What Lea changes.</strong> She puts up a board. She takes no difficult cannulation of her own after the first connections. Amber chairs get a named nurse and a fifteen-minute recheck. These are system changes, not instructions to try harder.</p>
"""],
    "skills": {"title": "Keeping the floor in view",
               "intro": "On a supervised shift, build and keep the board, run both huddles, and do timed rounds.",
               "items": [
                   ("Builds a board line for each chair with access, key risk, fluid goal, times, and flag.", False),
                   ("Gives every amber and red flag an owner and a recheck time.", True),
                   ("Rounds at the set times and looks at each patient before the machine.", True),
                   ("Runs an opening huddle in three minutes, standing, ending with owners.", False),
                   ("Runs a mid-shift huddle and parks non-safety topics.", False),
                   ("Names three tasks protected from interruption and enforces the signal.", True),
                   ("Closes or hands over every open flag at the end of the shift.", True),
               ],
               "placement": "For one week, note each time you learned of a patient problem later than you should have, and what on the board or in the rounds would have shown it sooner."},
    "quiz": [
        ("Expecting that a patient will faint in the next ten minutes is which level of awareness?",
         ["Seeing", "Understanding", "Predicting", "Recording"], 2,
         "Predicting is the third level, and the one that gives time to act."),
        ("In the medicine-administration study, each interruption was associated with:",
         ["No change", "About 12.7% more clinical errors", "Fewer errors among experienced nurses", "Faster work"], 1,
         "Experience did not protect against interruption errors."),
        ("What is a huddle&rsquo;s core question?",
         ["Who is late today?", "What could hurt someone in the next hours, and who owns it?", "What supplies are low?", "Who is on leave next week?"], 1,
         "Short, standing, and about safety."),
        ("How is the evidence on huddles best described?",
         ["Proven to cut deaths", "Mostly positive for teamwork, from low-rigor studies", "Harmful", "Absent"], 1,
         "Probably helpful and cheap; not shown to reduce adverse events."),
        ("During rounds, look first at:",
         ["The machine screen", "The patient", "The chart", "The clock"], 1,
         "The patient shows trouble before the numbers do."),
        ("Which task should be protected from interruption?",
         ["Restocking gauze", "Heparin preparation", "Updating the board", "Taking a break"], 1,
         "Medicine preparation, the order-machine check, and catheter connection."),
        ("What does an amber flag mean?",
         ["Disconnect now", "Watch, with a named nurse and a timed recheck", "Nothing", "Call a code"], 1,
         "Amber without an owner and a time is a wish."),
        ("In the case, the main failure was:",
         ["The nurse at Bed 7", "The way information moved", "The patient", "The machine"], 1,
         "A system without a board or timed rechecks."),
        ("What belongs on a board line?",
         ["The patient&rsquo;s full name and diagnosis", "Bed, access, key risk, fluid goal, times, flag", "The patient&rsquo;s PhilHealth number", "The nurse&rsquo;s schedule"], 1,
         "Enough to see at a glance, nothing private."),
        ("When should the first round happen?",
         ["Only at the end", "About fifteen minutes after the last connection", "Once a shift", "Only when an alarm sounds"], 1,
         "Early problems cluster soon after connection."),
        ("The huddle drifts into complaints about the air conditioner. What do you do?",
         ["Let it run", "Park the topic and return to what could hurt someone", "Cancel future huddles", "Leave"], 1,
         "Keep it short and focused so it stays cheap."),
        ("A physician interrupts you during heparin preparation. What do you do?",
         ["Stop mid-step and talk", "Finish the step, then talk", "Ignore him all shift", "Hand the syringe to him"], 1,
         "Protect the task; then give him your full attention."),
        ("What happens to the board at the end of the shift?",
         ["It is erased", "It becomes the handoff: every open flag closed or passed to a named person", "It is photographed for PhilHealth", "Nothing"], 1,
         "Open flags move with an owner."),
        ("Why should a charge nurse avoid her own difficult cannulations after the first connections?",
         ["They are boring", "Her attention is needed for the whole floor", "It is against the law", "Cannulation is not nursing work"], 1,
         "A busy pair of hands means a lowered head."),
        ("A drowsy patient&rsquo;s machine shows normal numbers. What do you do?",
         ["Trust the machine", "Assess the patient: rouse, pressure, glucose if indicated", "Let him sleep", "Turn off the alarm"], 1,
         "The patient shows trouble first."),
    ],
    "terms": [("Situational awareness", "Knowing what is happening, what it means, and what comes next."),
              ("Live board", "One line per chair, readable at a glance by the whole team."),
              ("Flag", "Green steady, amber watch with a timed recheck, red act now."),
              ("Huddle", "A three-minute standing meeting about what could hurt someone."),
              ("Protected task", "A task nobody interrupts except for an emergency.")],
    "readings": [("hemodialysis-complications.html", "The complications that rounds are meant to catch early."),
                 ("dialysis-qapi-vs-cqi.html", "How a unit turns repeated near misses into improvement.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c1"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
