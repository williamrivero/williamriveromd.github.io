# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Why one dialysis session produces three records, the chart, the registry and the claim, and why they must tell the same truth; how to audit for accuracy, correct an error without concealing it, protect privacy, and make reporting reliable without signing what you cannot attest.",
    "desc": "Special Dialysis Nurse Roles Module 11: the documentation, registry and PhilHealth liaison nurse. Clinical record versus registry versus claim, delivered treatment documentation, PhilHealth quality standards, data dictionaries, audits, amendments with audit trails, RA 10173 privacy and reporting reliability.",
    "keywords": "dialysis documentation nurse, PhilHealth hemodialysis claims documentation, renal registry Philippines, PRDR dialysis reporting, nursing record amendment audit trail, Data Privacy Act health records, delivered treatment time documentation",
    "image_alt": "A Filipino dialysis nurse at a computer comparing a session's treatment record with a printed claim summary, highlighting one line.",
    "objectives": [
        "Distinguish the clinical record, registry reporting and PhilHealth claims, and say what each is for.",
        "Audit documentation for accuracy, completeness and consistency, and reconcile discrepancies.",
        "Correct records with a visible amendment and audit trail, and protect confidentiality.",
        "Coordinate reporting without making clinical or billing attestations the nurse cannot support.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "One session, three records, one truth",
         "html": """
<p>Imagine a single event photographed from three angles: the clinical record (what happened to the patient), the registry entry (how this patient counts in the national picture of kidney failure), and the PhilHealth claim (what service the facility is asking to be paid for). The three pictures have different frames, but they show the same event. If one picture shows a four-hour session and another shows two hours and forty minutes, at least one is false.</p>
<p>The picture has a limit. Photographs cannot be edited quietly. Records can, and that is the danger: a small change to "make everything match" can turn an honest clinical note into a false one. The documentation nurse's rule is that the clinical record follows what happened, and the other records follow the clinical record, never the other way around.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Write what happened. Correct openly. Never change a clinical entry to fit a claim.</div>
"""},
        {"id": "three", "nav": "Three records", "tag": "Concepts", "h2": "Know which record serves which purpose",
         "html": """
<div class="table-wrap"><table>
<thead><tr><th>Record</th><th>Purpose</th><th>Who relies on it</th><th>The nurse's part</th></tr></thead>
<tbody>
<tr><td>Clinical record</td><td>Safe care and continuity: orders, treatment delivered, events, assessments, teaching</td><td>Every clinician; the patient; inspectors; courts</td><td>Accurate, timely, signed entries of what was observed and done</td></tr>
<tr><td>Registry (for example the Philippine Renal Disease Registry, PRDR)</td><td>National data on kidney failure: incidence, modality, outcomes</td><td>Planners, researchers, the PSN and DOH</td><td>Accurate census events (new patient, transfer, modality change, death) through the designated records function</td></tr>
<tr><td>PhilHealth claim</td><td>Payment for covered services under the current circulars</td><td>The facility; PhilHealth</td><td>Truthful source documentation; the claim is prepared and certified by authorized staff</td></tr>
</tbody></table></div>
<p>The DOH licensing order names a records function and registry participation as facility duties, and the PSN guidelines describe a designated records and registry role.[[doh2012]][[psn2024]] PhilHealth's quality standards for maintenance hemodialysis include provisions on the prescription and on documenting the treatment delivered.[[phic2024_29]] None of these makes the nurse the default claims officer. The Academy's Billing & Claims Officer and Medical Records Officer tracks cover those roles in depth.</p>
"""},
        {"id": "truth", "nav": "Audit for truth", "tag": "Practice", "h2": "Audit truth, completeness and consistency",
         "html": """
<p>A documentation audit asks three questions of a sample of records.</p>
<div class="tc-cards">
<div class="tc-card"><b>True</b>Does the entry match what happened? Treatment start and end times, delivered minutes, fluid removed, events and actions.</div>
<div class="tc-card"><b>Complete</b>Are required fields present: order, identity checks, vital signs, access assessment, medicines given, signature?</div>
<div class="tc-card"><b>Consistent</b>Do the chart, machine log, registry and claim agree? Where they differ, which is right?</div>
</div>
<p><strong>Use a data dictionary.</strong> Agree written definitions for the fields that matter: "treatment start" (pump on with blood flow), "treatment end" (blood return complete), "delivered minutes," "session ended early (reason)." Without definitions, two nurses record the same event differently, and audits measure handwriting instead of care.</p>
<p><strong>Source hierarchy.</strong> When records disagree, the primary source of truth is the contemporaneous clinical record and the machine's treatment log, supported by the order. Claims and registry entries are derived records and are corrected to match the source.</p>
<div class="sd-calc"><span class="tc-lab">Worked example &middot; Portfolio Toolkit, tool 1</span>An audit of 40 session records finds 31 complete and consistent across chart, machine log and claim. Accuracy is 31 of 40 (78 percent, 95 percent range about 63 to 88). The nine failures are listed by type: four missing end times, three delivered minutes copied from the prescription, two missing signatures. Copying prescribed minutes is the most serious, because it states something that did not happen.</div>
"""},
        {"id": "amend", "nav": "Correct openly", "tag": "Integrity", "h2": "Correct without concealing",
         "html": """
<p>Errors happen. The rule is that a correction must be visible: the original entry stays readable (a single line through it on paper, or a tracked amendment in an electronic record), and the correction carries the date, time, the name of the person correcting, and the reason. A late entry is labeled as late, with the time it was written and the time it refers to.</p>
<div class="tc-stop"><span class="tc-lab">Never</span>Erase, overwrite, use correction fluid, back-date, sign for someone else, or change a clinical entry so that it matches a claim, a target or a colleague's request.</div>
<div class="tc-scene"><span class="tc-lab">'Just make the fields match' &middot; fictional</span><p>Mrs. Leonora Cruz's session ended after 2 hours 40 minutes because of symptomatic hypotension; the nurse recorded this, the blood pressures and the physician's instruction. Preparing the month's claims, a colleague notices the draft claim lists the full 4-hour prescription and asks Nurse Records Liaison Pia to "adjust the nursing notes so all the fields match."</p><p>Pia declines. The nursing record is true; the draft claim is the record that is wrong. She flags the discrepancy to the claims officer and the head nurse in writing, so the claim can be corrected under PhilHealth's current rules by the people authorized to certify it.</p><p class="tc-scene-take"><b>What this shows.</b> Derived records follow the clinical truth. A matching set of false records is worse than an honest mismatch, because it hides what happened to the patient.</p></div>
"""},
        {"id": "privacy", "nav": "Privacy", "tag": "Law", "h2": "Protect confidentiality",
         "html": """
<p>Health information is sensitive personal information under the Data Privacy Act; processing it needs a lawful basis, and the facility must protect it with organizational, physical and technical measures.[[ra10173]] For the records liaison this means:</p>
<ul>
<li><strong>Role-based access</strong>: staff see what their role needs; passwords are personal and never shared.</li>
<li><strong>Minimum necessary</strong>: send only what the receiver needs, through approved channels.</li>
<li><strong>Secure release</strong>: copies to patients, insurers or other facilities follow the release policy, with consent or another lawful basis, recorded.</li>
<li><strong>No personal devices or chats</strong> for patient data unless the facility's policy explicitly allows and secures them.</li>
<li><strong>Breach reporting</strong>: a suspected breach goes to the facility's data protection officer at once; the officer decides on any notification under the law.</li>
</ul>
<p><strong>Downtime.</strong> When the electronic system fails, use the facility's paper downtime forms, keep them secure, and enter them into the system afterward, labeled as late entries from downtime.</p>
"""},
        {"id": "reporting", "nav": "Reliable reporting", "tag": "Coordination", "h2": "Make reporting reliable and recoverable",
         "html": """
<ol class="tc-flow">
<li><b>Reconcile the census</b>Monthly: new patients, transfers in and out, modality changes, hospitalizations, deaths, transplants.</li>
<li><b>Validate before submission</b>Check a sample of submitted fields against the source.</li>
<li><b>Keep receipts</b>Submission confirmations, dates and reference numbers.</li>
<li><b>Work rejections</b>Each rejection gets a reason, an owner and a corrected resubmission, never a quiet change to the clinical record.</li>
<li><b>Version control</b>Use the current forms and data definitions; note when they change.</li>
</ol>
<p><strong>Know your limits.</strong> The liaison nurse supports accurate reporting. She does not assign diagnosis codes without authority, sign or certify claims on behalf of others, guarantee payment, or become the facility's data protection officer by default. Those are designated roles.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>Reward accuracy, not matching. A rising rejection rate that comes from honest corrections is better than a perfect record that hides early terminations.</div>
"""},
    ],
    "case": {
        "title": "Make the fields match",
        "html": """
<p><strong>Thursday, end of month.</strong> The claims officer has prepared 120 session claims for the month. While checking a sample, you find that Mrs. Leonora Cruz's session on the 9th ended after 2 hours 40 minutes because of symptomatic hypotension (documented with blood pressures and the physician's instruction), but the draft claim lists 4 hours. Three other sessions show delivered minutes in the chart that exactly equal the prescription, although the machine logs show shorter times.</p>
<p>A colleague says, "It's easier to fix the nursing notes than to redo the claims. Just make the fields match before the deadline tomorrow."</p>
""",
        "acte": {
            "Assess": "The clinical record for Mrs. Cruz is true; the draft claim is wrong. The three other charts may have copied prescribed minutes, contradicting the machine logs: a documentation problem in the clinical record itself.",
            "Communicate": "Decline to alter true entries. Notify the claims officer and head nurse in writing about the claim discrepancy. For the three charts, ask the nurses who wrote them to review against the machine logs and make visible, dated amendments where they were wrong.",
            "Teach": "Explain the source hierarchy and why copying prescribed minutes is a false entry. Propose a data-dictionary definition of delivered minutes and a field for 'ended early, reason.'",
            "Escalate": "If pressure to alter records continues, raise it with the head nurse and clinical head. Add delivered-versus-prescribed time to the next documentation audit.",
        },
        "outcome": """
<p>The claims were corrected and submitted on time by the claims officer. Two of the three charts had copied prescribed minutes; the nurses amended them openly. The unit added a delivered-minutes field read from the machine log, and the next audit showed no copied values.</p>
""",
        "task": "Write a visible amendment for one of the three charts (original entry, correction, date and time, reason, name) and a two-line note to the claims officer.",
    },
    "second_round": ("A week later, an insurer emails asking for 'all records' of a patient for a claim, without a signed authorization.",
                     "A short reply plan citing your facility's release policy: what you will ask for, what minimum information may be released once authorized, and through which channel."),
    "evidence_out": "A 20-record documentation audit with findings by type, and one correctly amended record.",
    "critical": "Altering a true clinical entry to match a claim or target, back-dating, or signing for another person.",
    "reflect": "Which field in your unit's records is most often copied rather than observed? What would make observing it easier than copying it?",
    "practice": {
        "intro": "Use de-identified records with permission, or the fictional data in this module.",
        "items": [
            "Audit 20 session records for truth, completeness and consistency against the machine log.",
            "Draft data-dictionary definitions for treatment start, end and delivered minutes.",
            "Practice a visible amendment on paper and in your electronic system's training mode.",
            "Map who in your facility certifies claims, maintains the registry and acts as data protection officer.",
            "Reconcile one month's census against registry submissions.",
        ],
    },
    "job_aid": ("Documentation audit sheet", [
        "Record code, session date, auditor, date of audit",
        "Order present and current (yes/no)",
        "Start and end times recorded; match machine log (yes/no)",
        "Delivered minutes observed, not copied from prescription (yes/no)",
        "Events and actions recorded with times",
        "Medicines given recorded and signed",
        "Signature and identity of the writer",
        "Chart, registry and claim consistent (yes/no; which differs)",
        "Finding type (missing, copied, inconsistent, unsigned)",
        "Action: owner, amendment or correction route, date",
    ]),
    "metric": "Records that are accurate and complete divided by records sampled; reporting rejection rate and time to resolve discrepancies are tracked separately, so that concealment is never rewarded.",
    "readings": [
        ("philhealth-z-packages.html", "PhilHealth packages explained."),
        ("zero-balance-billing-philhealth.html", "Zero balance billing in PhilHealth."),
        ("dialysis-prescription.html", "What the dialysis prescription contains."),
    ],
    "academy": [("PhilHealth Liaison and Claims Officer track", "philhealth-claims.html"), ("Medical Records Officer and Custodian track", "medical-records-officer.html")],
    "calcs": ["calc-dialysis-nurse-portfolio-toolkit.html"],
    "terms": [
        ("Clinical record", "The contemporaneous record of a patient's care, the primary source of truth."),
        ("Registry", "A database of patients with a condition, used for national planning and research."),
        ("Data dictionary", "Written definitions of each recorded field so everyone records it the same way."),
        ("Audit trail", "A visible history of who changed a record, when and why."),
        ("Late entry", "An entry written after the event, labeled with both the time written and the time it refers to."),
    ],
    "quiz": [
        {"stem": "A session ended early for hypotension; the draft claim lists the full prescription. A colleague asks you to change the nursing notes to match. What do you do?",
         "options": [["Decline; flag the claim discrepancy to the claims officer and head nurse in writing.", True, "Derived records follow the clinical truth."],
                     ["Change the notes, since the claim is due tomorrow.", False, "Falsifies the clinical record."],
                     ["Delete the session from both.", False, "Concealment."],
                     ["Ignore it; billing is not nursing.", False, "Truthful source documentation is the nurse's duty."]], "sources": ["phic2024_29"], "critical": True},
        {"stem": "How should an incorrect paper entry be corrected?",
         "options": [["A single line through it, leaving it readable, with the correction, date, time, name and reason.", True, "Corrections must be visible."],
                     ["Correction fluid and rewrite.", False, "Conceals the original."],
                     ["Tear out the page.", False, "Concealment."],
                     ["Write over it.", False, "Obscures the original."]], "sources": [], "critical": True},
        {"stem": "When the chart, machine log and claim disagree on delivered minutes, which is the primary source?",
         "options": [["The contemporaneous clinical record and machine treatment log.", True, "Claims and registry are derived records."],
                     ["The claim.", False, "Derived."],
                     ["The prescription.", False, "States the plan, not what happened."],
                     ["Whichever is most convenient.", False, "Not a hierarchy."]], "sources": []},
        {"stem": "What is the main purpose of a registry entry?",
         "options": [["National data on kidney failure for planning and research.", True, "Different purpose from the chart and claim."],
                     ["Payment for services.", False, "That is the claim."],
                     ["Daily clinical care.", False, "That is the clinical record."],
                     ["Staff evaluation.", False, "Not its purpose."]], "sources": ["doh2012"]},
        {"stem": "Why is copying the prescribed minutes into 'delivered minutes' a serious error?",
         "options": [["It records something that did not happen and hides short treatments.", True, "A false entry, and a clinical blind spot."],
                     ["It is only a spelling issue.", False, "It is a truth issue."],
                     ["It makes the record shorter.", False, "Irrelevant."],
                     ["It is acceptable if the patient agreed.", False, "Not acceptable."]], "sources": []},
        {"stem": "Under RA 10173, how is health information classed?",
         "options": [["Sensitive personal information requiring a lawful basis and protection.", True, "Higher protection applies."],
                     ["Public information.", False, "Not public."],
                     ["Ordinary contact data.", False, "More sensitive."],
                     ["Facility property with no limits.", False, "Rights and duties apply."]], "sources": ["ra10173"]},
        {"stem": "An insurer requests 'all records' without authorization. What is correct?",
         "options": [["Follow the release policy: require authorization or another lawful basis, and release the minimum necessary.", True, "Secure release."],
                     ["Send everything by email.", False, "Breach risk."],
                     ["Refuse permanently.", False, "Release is possible once authorized."],
                     ["Ask the patient's neighbor.", False, "Irrelevant."]], "sources": ["ra10173"]},
        {"stem": "What is a data dictionary used for?",
         "options": [["Defining each field so that everyone records it the same way.", True, "Makes audits measure care, not handwriting."],
                     ["Translating records into Tagalog.", False, "Not the purpose."],
                     ["Storing passwords.", False, "Never."],
                     ["Listing staff names.", False, "Not the purpose."]], "sources": []},
        {"stem": "A colleague asks you to sign a claim on her behalf because she is off. What do you do?",
         "options": [["Decline; only the authorized person signs for what they can attest.", True, "Surrogate signatures are false attestations."],
                     ["Sign her name.", False, "Forgery."],
                     ["Sign your name for her claim.", False, "You cannot attest to it."],
                     ["Leave it unsigned and submit.", False, "Incomplete and improper."]], "sources": [], "critical": True},
        {"stem": "The electronic system is down for a shift. What should happen to documentation?",
         "options": [["Use paper downtime forms, keep them secure, and enter them later labeled as late entries.", True, "Downtime procedures preserve truth and timing."],
                     ["Skip documentation.", False, "Never."],
                     ["Write on personal phones.", False, "Privacy risk."],
                     ["Back-date entries later.", False, "Late entries are labeled, not back-dated."]], "sources": []},
        {"stem": "Is the records liaison nurse the facility's data protection officer by default?",
         "options": [["No; that is a designated role.", True, "Do not assume roles not assigned."],
                     ["Yes, always.", False, "Not by default."],
                     ["Only on weekends.", False, "No."],
                     ["Only if PhilHealth says so.", False, "No."]], "sources": ["ra10173"]},
        {"stem": "An audit finds 31 of 40 records accurate. What is the honest report?",
         "options": [["78 percent (31 of 40), with failures listed by type.", True, "Counts, percentage and types."],
                     ["'Almost 80 percent, fine.'", False, "Hides the failures."],
                     ["100 percent of signed records.", False, "Selective."],
                     ["Only the failures.", False, "Report both."]], "sources": []},
        {"stem": "What should happen to a rejected registry submission?",
         "options": [["Record the reason, assign an owner and resubmit a corrected entry based on the source.", True, "Never change the clinical record to fit."],
                     ["Change the clinical record to match the registry.", False, "Wrong direction."],
                     ["Ignore it.", False, "Must be resolved."],
                     ["Delete the patient.", False, "Concealment."]], "sources": []},
        {"stem": "Which measure best rewards honest documentation?",
         "options": [["Accurate and complete records divided by records sampled.", True, "Measures truth, not matching."],
                     ["Claims with zero discrepancies, however achieved.", False, "May reward concealment."],
                     ["Speed of claim submission only.", False, "May reward copying."],
                     ["Number of records signed.", False, "Activity, not accuracy."]], "sources": []},
        {"stem": "What is a late entry?",
         "options": [["An entry written after the event, labeled with the time written and the time it refers to.", True, "Transparent timing."],
                     ["An entry back-dated to look on time.", False, "Back-dating is prohibited."],
                     ["An entry by a late-arriving nurse.", False, "Not the definition."],
                     ["An entry deleted later.", False, "Not the definition."]], "sources": []},
    ],
    "exam": [
        {"stem": "Which action is never acceptable in documentation?",
         "options": [["Changing a true clinical entry to match a claim.", True, "Derived records follow the clinical truth."],
                     ["Adding a labeled late entry.", False, "Acceptable."],
                     ["Making a visible amendment with reason.", False, "Correct practice."],
                     ["Flagging a claim discrepancy.", False, "Correct practice."]], "sources": [], "critical": True},
        {"stem": "What makes a record correction acceptable?",
         "options": [["The original remains readable, with date, time, name and reason for the correction.", True, "Visible audit trail."],
                     ["The original is erased cleanly.", False, "Concealment."],
                     ["The correction is made by anyone available.", False, "The author corrects, with identity."],
                     ["The correction matches the claim.", False, "Not the test."]], "sources": []},
    ],
}

# ── v2 completion (24 Nov 2026): second worked scenario ──
def _sec(sid):
    return next(s for s in MODULE["sections"] if s["id"] == sid)

_sec("privacy")["html"] += """
<div class="tc-scene"><span class="tc-lab">The census photo in the group chat &middot; fictional</span><p>At 5:50 a.m., a nurse posts a phone photo of the shift census board to the unit's messaging group so the incoming staff can "see the schedule early." The board shows twenty full names, hepatitis B status, access types and two notes reading "for PhilHealth follow-up, unpaid." The group includes two former staff members and a driver.</p><p>Nurse Grace, the documentation and privacy liaison, asks the poster to delete the photo and asks the group administrator to remove it for everyone. She checks who could have seen it, tells the head nurse and the unit's data protection officer the same morning, and records the facts: what was shared, when, with whom, and when it was removed. The data protection officer decides whether it must be reported further under the unit's breach procedure.[[ra10173]]</p><p>The fix is a system change, not a lecture. The unit removes former staff and nonclinical members from the clinical group, moves the census to the access-controlled system, and agrees that schedule messages carry initials and station numbers only.</p><p class="tc-scene-take"><b>What this shows.</b> Well-meant convenience can expose sensitive health information. The liaison contains it, reports it the same day, and changes the channel so it does not happen again.</p></div>
"""
