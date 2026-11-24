# -*- coding: utf-8 -*-
"""Situations and tips for Physician on Duty, Module 07. Fictional and original.
Each scenario: (title, what you see, what is likely going on, what to do, why it matters)."""

SITUATIONS = {"07": {
    "scenarios": [
        ("The catheter that cannot keep up",
         "Mr. Danilo Reyes, 58, dialyzes through a neck catheter. His order lists a blood flow the nurse cannot reach. Each time she raises the pump speed, the arterial pressure alarm sounds, and she has settled well below the written rate.",
         "The catheter cannot deliver the ordered flow, possibly from a clot or a fibrin sheath at its tip. Every minute at the lower flow delivers less dose than the order assumes.",
         "Accept the flow the access can safely give, as the unit&rsquo;s protocol allows, and record the actual rate and pressures. Call the attending nephrologist with the numbers. Module 10 covers catheter troubleshooting.",
         "A dose problem that starts at the access will appear weeks later as a low Kt/V. Recording the delivered flow today makes that result explainable."),
        ("A low URR after a late draw",
         "Aling Rosario Mendoza&rsquo;s monthly urea reduction ratio has dropped sharply, although her session log shows full time and the ordered blood flow. The nurse on that day was new and drew the post-dialysis sample about 40 minutes after the session ended, once Aling Rosario had been disconnected and weighed.",
         "This is likely not a dose problem at all. A late post-dialysis sample catches urea rebound from the tissues, so the post-dialysis BUN reads high and the dose looks lower than it was. The single result does not fit her log.",
         "Check how the sample was drawn. Report to the attending nephrologist that the sampling technique was not the unit&rsquo;s standard and ask whether to repeat the measurement. Review the method with the nurse.",
         "Changing the prescription for a sampling error adds treatment the patient does not need. The cheapest explanation is the first one to check."),
        ("Calcium bath after parathyroid surgery",
         "Mr. Arnold Villanueva had his parathyroid glands removed last week and is back for dialysis. He reports tingling around the mouth and in his fingers. His standing order, written before the operation, still shows his usual dialysis fluid calcium.",
         "After parathyroid surgery the bones take up calcium fast, and blood calcium can fall steeply. A bath written before surgery may now remove calcium he cannot spare.",
         "Do not start until you have spoken to the attending nephrologist. Ask for the latest calcium result, or for one to be drawn per protocol, and report the symptoms. Follow the unit&rsquo;s protocol for symptomatic low calcium.",
         "The order was right for the patient he was before surgery. Any recent procedure is a reason to check whether the order still fits."),
        ("Hemodiafiltration that falls short",
         "Ms. Teresita Lim is on online hemodiafiltration. Her order states a substitution volume for the session. Her fistula has been hard to cannulate and the blood flow has been lower than written for a week. The machine summary shows the convection volume well below the order at each session.",
         "Convection volume depends on blood flow. With less blood through the filter, less water can be safely pushed across it, so the machine delivers less convection.",
         "Record the delivered blood flow and convection volume and examine the fistula. Report to the attending nephrologist that the session cannot reach the ordered volume and that the access may be failing. Module 09 covers fistula assessment.",
         "The trials that showed fewer deaths tested a high convection volume. A label of hemodiafiltration without the volume is not the treatment that was tested."),
        ("Two sessions of forty minutes",
         "Mr. Eduardo Santos has signed off early twice this week because of back pain in the chair. Each time he lost about forty minutes. He asks you to sign the early end again today.",
         "Lost time is lost dose. Back pain in the chair may also be treatable, and treating it may keep him on the machine.",
         "Examine him and address the pain per protocol. Explain plainly that the remaining minutes carry part of his treatment. If he still declines, respect his decision, document the minutes lost and the advice given, and inform the attending nephrologist.",
         "Short treatment time was associated with sudden death in a large international cohort. A pattern of early sign-off is a prescription problem, not only a comfort problem."),
    ],
    "tips": [
        "Read the order at the chair, beside the machine, with the nurse. An order read at the desk is not checked against what is set.",
        "Ask for today&rsquo;s potassium before the pump starts in any patient who has vomited, had diarrhea, eaten poorly, or started digoxin.",
        "On adequacy days, watch one post-dialysis draw yourself. You will learn more about your unit&rsquo;s numbers in five minutes than from a month of results.",
        "Write delivered minutes and delivered blood flow in every note. They are the first two facts the attending nephrologist will ask for when a Kt/V is low.",
        "When an order does not fit, say so out loud before anything is started. A circuit that is primed is not a reason to proceed.",
    ],
}}
