# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 06: eClaims 3.0, Filing Deadlines, and Acknowledgments."""

MODULE = {
    "image_alt": "A slim receipt slip emerging from a small desktop printer, with a laptop and a desk calendar softly blurred behind it.",
    "objectives": [
        "Describe the eClaims 3.0 transition and what it means for every case-rate claim filed today.",
        "Run a complete simulated transmission: validate, approve, send once, and capture the official receipt.",
        "Compute a filing deadline and an internal target from an approved trigger date, and record their basis.",
        "Separate the filing, return-response, and appeal clocks, and verify each from its own source.",
        "Handle a portal timeout without creating a duplicate claim.",
    ],
    "big": """
{{plain:Filing a claim is like posting a registered letter. Dropping it in the box is not enough; what counts is the receipt with a number and a time stamp. Without the receipt, you cannot prove you sent it, and if you post it twice, someone has to sort out the duplicate.}}
<p>The picture has a limit. A registered letter&rsquo;s receipt also proves it arrived. A transmission receipt proves only that PhilHealth&rsquo;s system received the claim at that stage. Whether it will be paid is a separate question, answered later by adjudication. Track the two separately.</p>
{{cards:Key terms for this module|eClaims 3.0::PhilHealth&rsquo;s current electronic claims system; the only version accepted from July 1, 2026.|Transmission::Sending a released claim to PhilHealth, once.|Acknowledgment::The official receipt or claim reference, with a time stamp.|Filing trigger::The approved date from which the filing period is counted.|Internal target::Your own earlier date, which leaves time to fix problems.|Fortuitous event::A declared disaster for which PhilHealth may extend filing by advisory.}}
""",
    "case": {"title": "The screen that froze at 10:04", "html": """
<p>The claims officer, Mr. Noel Bautista, releases the claim for SIM-06 at 10:04 on a Tuesday. The screen freezes, then shows a timeout message. A message from the vendor&rsquo;s help desk suggests &ldquo;just upload it again.&rdquo; The approved filing trigger for this claim is September 1, and today is October 20.</p>
""", "questions": ["What do you do, in order, before anything is sent again?",
                  "What is the filing deadline, and how much time is left?",
                  "Where do you report the system problem, and what do you record?"]},
    "sections": [
        ("transition", "eClaims 3.0", "The move to eClaims 3.0", """
<p>The move to eClaims 3.0 happened in three steps. From April 1, 2026, claims under all case rates could be filed electronically only through eClaims 3.0, and lower versions were disabled at 11:59 PM on March 31.[[pc_pa2026_0022]] Claims submitted on lower versions from April 15 to June 30, 2026 were returned to the facility. From July 1, 2026, only eClaims 3.0 is operational and lower versions are decommissioned.[[pc_pa2026_0027]] Under 3.0, the statement of account must be XML.</p>
{{flow:A clean transmission|1. Draft::From verified records only.|2. Validate::Run claim and XML validations and resolve exceptions.|3. Approve::Release approval by the authorized officer.|4. Send once::Transmit through your certified system and individual authorized account.|5. Capture::Save the acknowledgment or claim reference with its time stamp.|6. Track::Follow adjudication separately.}}
<p>Use your own authorized account, never a shared password. A transmission receipt is evidence of receipt at that stage, not payment.</p>
"""),
        ("deadlines", "Filing clocks", "Deadlines and internal targets", """
<p>By law, claims are filed within 60 calendar days; PhilHealth Circular 2025-0019 restates the period, and the hemodialysis circular applies a 60-day filing period to the package.[[pc_pc2025_0019]][[pc_pc2024_0023]] The general statute counts from discharge; for repetitive procedures, the trigger for single and grouped sessions follows the package and claims guidance. Confirm the exact trigger with your PRO and your facility SOP, then set an internal target well before the deadline so there is time to fix a problem.</p>
{{formula:<strong>Worked example (training only).</strong> Approved trigger September 1; 60 calendar days counted from the following day. Day 1 is September 2, so day 60 is October 31. An internal target at day 30 is October 1. Calendar days include weekends and holidays unless an issuance says otherwise. Calculator 1 in the claims toolkit does this arithmetic and shows the basis.}}
<p><strong>Extensions.</strong> PhilHealth may extend filing for declared disasters by advisory; for example, it gave covered regions 120 days from discharge after Typhoon Kristine in 2024.[[pc_pa2024_0057]] Use an extension only with a dated advisory that names your region and dates, and record the advisory number with the recomputed deadline.</p>
<p><strong>History, not a remedy.</strong> PhilHealth Circular 2025-0006 let facilities refile claims that had been denied for late filing between January 1, 2018 and December 31, 2024. That window ran from March 21 to September 21, 2025, and is closed. It never applied to routine new claims.[[pc_pc2025_0006]][[pc_pa2025_0037]]</p>
{{fig:pc_clocks}}
"""),
        ("timeout", "A timeout", "When the portal times out", """
<p>After a timeout, the claim may have arrived or not. Sending it again without checking can create a duplicate, which is then denied, and may trigger audit questions about every claim in the batch.</p>
{{fignarrow:pc_timeout}}
<p>Since July 15, 2026, information technology requests from external stakeholders go through the PhilHealth Ticketing System.[[pc_pa2026_0037]] Record the vendor ticket, the PhilHealth ticket, the affected claims, and the service dates in your chronology. When a system problem threatens a deadline, ask your PRO early about the applicable procedure, in writing.</p>
{{call:Never resend a claim until the official status shows it was not accepted. A vendor&rsquo;s &ldquo;success&rdquo; message or a local batch file is not proof of filing, and a second transmission of a received claim is a duplicate.}}
"""),
    ],
    "debrief": ["""
<p><strong>In order.</strong> Save evidence of the attempt (the time and a screenshot). Check the portal and batch history for a receipt. If a receipt exists, stop: record it and do not resend. If you are still unsure, hold and escalate; do not resend. Only if authorized staff confirm that the claim was not accepted, make one authorized retry and capture the receipt. Ignore the vendor&rsquo;s &ldquo;just upload it again&rdquo; until the status is known.</p>
<p><strong>The deadline.</strong> Day 60 from a September 1 trigger is October 31. On October 20 there are 11 days left, and the internal target (October 1) has already passed: escalate now.</p>
<p><strong>The report.</strong> Open a vendor ticket and a PhilHealth Ticketing System ticket, and record both numbers with the affected claim and service dates in the chronology. If the problem may cost the deadline, write to your PRO the same day.</p>
"""],
    "skills": {"title": "Simulated transmission and timeout",
               "intro": "In a sandbox or paper simulation, release a fictional claim, capture its receipt, then handle a planted timeout.",
               "items": [
                   ("Runs validations and resolves exceptions before release approval.", False),
                   ("Transmits once with an individual authorized account.", True),
                   ("Captures the acknowledgment or claim reference with its time stamp.", True),
                   ("Computes the deadline and internal target and records the trigger and basis.", False),
                   ("Checks official status before any retry after a timeout.", True),
                   ("Opens vendor and PhilHealth tickets and records them in the chronology.", False),
               ],
               "placement": "Observe one real batch release at your unit and list each receipt captured."},
    "quiz": [
        ("Is a successfully generated local batch file evidence of filing?",
         ["Yes", "No; check the official receiving workflow for an acknowledgment or claim reference", "Only for grouped claims", "Only after 5 PM"], 1,
         "Only the official receipt proves receipt."),
        ("Who can grant or confirm a deadline exception?",
         ["The vendor", "PhilHealth, under the applicable issuance; a vendor ticket is only evidence", "The clerk", "The patient"], 1,
         "Follow the formal authority."),
        ("From which date was only eClaims 3.0 operational, with lower versions decommissioned?",
         ["January 1, 2026", "July 1, 2026", "October 9, 2024", "March 31, 2025"], 1,
         "PhilHealth Advisory 2026-0027."),
        ("Trigger November 15, 60 calendar days counted from the next day. What is the deadline?",
         ["January 13", "January 14", "January 15", "December 31"], 1,
         "November 16 is day 1."),
        ("Your region is named in a typhoon advisory granting 120 days. What do you record?",
         ["Nothing", "The advisory number, region, covered dates, and the recomputed deadline approved by the claims lead", "Only the new date", "A screenshot of the news"], 1,
         "Extensions rest on a dated advisory."),
        ("Since July 15, 2026, where do information technology requests to PhilHealth go?",
         ["Social media", "The PhilHealth Ticketing System", "The LHIO counter only", "The vendor"], 1,
         "PhilHealth Advisory 2026-0037."),
        ("Is a vendor &ldquo;success&rdquo; message proof of filing?",
         ["Yes", "No; only the official acknowledgment or claim reference", "Only if printed", "Only on weekdays"], 1,
         "Capture the official receipt."),
        ("The screen times out after you send. What is your first step?",
         ["Resend immediately", "Save evidence of the attempt, then check the portal and batch history", "Call the patient", "Close the browser"], 1,
         "Check state before any retry."),
        ("What happened to the late-filing flexibility under Circular 2025-0006?",
         ["It applies to all new claims", "It ran from March 21 to September 21, 2025 and is closed", "It is permanent", "It applies only to dialysis"], 1,
         "History, not a remedy."),
        ("What must the statement of account be under eClaims 3.0?",
         ["A PDF", "XML", "A photo", "A spreadsheet"], 1,
         "PDF statements are returned."),
        ("Why set an internal target before the deadline?",
         ["To impress PhilHealth", "To leave time to fix problems before the legal clock ends", "Because PhilHealth requires day 30", "It is optional decoration"], 1,
         "Problems take time to fix."),
        ("Do calendar-day filing periods skip weekends and holidays?",
         ["Yes", "No, unless an issuance says otherwise", "Only Sundays", "Only holidays"], 1,
         "Count every day."),
        ("Status shows &ldquo;still unsure&rdquo; after a timeout. What do you do?",
         ["Resend", "Hold, escalate, and do not resend", "Delete the claim", "File on paper"], 1,
         "Uncertainty is not permission to resend."),
        ("What does a transmission acknowledgment prove?",
         ["That the claim will be paid", "Receipt at that stage", "That the codes are correct", "Eligibility"], 1,
         "Track adjudication separately."),
        ("What should you use to log in to eClaims?",
         ["A shared office password", "Your own individual authorized account", "The vendor&rsquo;s account", "The doctor&rsquo;s account"], 1,
         "Accounts make the audit trail."),
    ],
    "terms": [("eClaims 3.0", "PhilHealth&rsquo;s current electronic claims system."),
              ("Acknowledgment", "The official receipt or claim reference with a time stamp."),
              ("Filing trigger", "The approved date from which the filing period is counted."),
              ("Internal target", "Your own earlier date for finishing a claim."),
              ("Fortuitous event", "A declared disaster that may justify an extension by advisory."),
              ("Duplicate", "A second transmission of a claim PhilHealth already received.")],
    "readings": [("philhealth-acr-to-drg.html", "How PhilHealth is moving from case rates to diagnosis-related groups.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
