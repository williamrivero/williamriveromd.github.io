# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 19: Patient experience, access, and ethical growth. Written for this course from published sources."""

MODULE = {
    "image_alt": "A young woman arriving at a dialysis clinic entrance on a tricycle, greeted by a smiling older receptionist with a cane.",
    "objectives": [
        "Gather patient experience from every patient, including those least likely to answer surveys.",
        "Use grievances and compliments as quality data.",
        "Review marketing and referral arrangements for honesty and inducements.",
        "Grow only as fast as safe capacity allows.",
    ],
    "big": """
{{plain:A patient&rsquo;s experience is like the taste of food: the cook cannot judge it from the kitchen. You have to ask the person eating, and you have to ask the ones who stopped eating, not only the ones who came back for more.}}
<p>The picture has a limit. A diner can choose another restaurant. A dialysis patient often cannot choose another unit easily and may fear that complaining will cost them their slot. That makes listening harder and more important.</p>
{{cards:Key terms for this module|Patient experience::What patients report about their care: respect, information, waiting, comfort.|Response bias::When the people who answer a survey differ from those who do not.|Inducement::A gift or payment that attracts patients or referrals.|Ethical growth::Growing only as fast as the unit can safely serve more patients.}}
<p>Your work is to hear every patient, to market honestly, and to grow at the pace of safety.</p>
""",
    "case": {"title": "The free first session", "html": """
<p>A marketing officer at a new unit in Pasig proposes flyers offering &ldquo;FREE first session and a grocery pack every month&rdquo; and a 500-peso &ldquo;thank-you&rdquo; for every referral from a barangay health worker. The unit has 14 free slots, and the head nurse says she can safely add 8 patients this quarter.</p>
""", "questions": ["What is wrong with the flyer?", "What about the referral payment?", "How many new patients should the unit accept?"]},
    "sections": [
        ("experience", "Hearing everyone", "Hearing every patient", """
{{fig:duo19a}}
<p>Surveys help, but they miss people. In a United States study of the In-Center Hemodialysis Consumer Assessment of Healthcare Providers and Systems (ICH CAHPS) survey, only 36% of eligible patients responded, and responders had lower mortality and fewer hospitalizations than nonresponders: they were healthier.[[duo_dad2020]] A unit&rsquo;s survey can look good while its sickest patients go unheard.</p>
<p>Use several channels: short bedside conversations by someone who does not control the patient&rsquo;s schedule, a complaints and compliments log, family meetings, and a patient representative at quality meetings. Ask about respect, information, waiting, comfort, and fear.</p>
{{key:Survey results speak for the healthier patients. Go and ask the others.}}
"""),
        ("grievance", "Grievances as data", "Grievances are data", """
<p>Count grievances and compliments by cause each month and put them on the dashboard (Module 18). Waiting times, transport, cold rooms, and how staff speak are common causes, and most are fixable. A rising count is not always bad; it can mean patients feel safe to speak. A count of zero is not always good.</p>
{{key:A unit with no complaints may be a unit where nobody feels safe to complain.}}
"""),
        ("marketing", "Honest marketing", "Honest marketing and no inducements", """
{{fig:duo19b}}
<p>Test every advertisement and referral arrangement with four questions. Is every claim true and current? Does it present something the package already covers as a free gift? Does it pay or reward anyone for referrals? Can we safely serve the patients it will attract?</p>
<p>Gifts and referral payments pull patients by inducement rather than quality and can create obligations that keep them from leaving. They also raise legal and professional questions; have counsel review any arrangement. Compete on what patients can see and rely on: punctual sessions, respect, clear prices, and good outcomes.</p>
{{stop:No payments, gifts, or rewards for patient referrals, and no advertising that presents covered care as a free gift.}}
{{key:Market what is true and what you can deliver safely.}}
"""),
        ("growth", "Ethical growth", "Grow at the pace of safety", """
<p>Every new patient needs a chair, a cleared nurse, released water, make-up slack, and the outside services from Module 8. Accept new patients at the rate the narrowest gate allows, and widen the gate before you market more. Growth that outruns staffing shows up first as missed checks and late alarms, and later as admissions.</p>
{{key:Accept patients at the pace of your narrowest gate.}}
"""),
    ],
    "debrief": ["""
<p><strong>The flyer.</strong> The first session is covered by the package for eligible members, so &ldquo;free&rdquo; misleads, and monthly grocery packs are an inducement. Rewrite it to describe what the unit actually offers.</p>
<p><strong>The referral payment.</strong> Decline it. Paying for referrals pulls patients by inducement; have counsel review any arrangement.</p>
<p><strong>How many.</strong> Eight this quarter, the number the head nurse can safely staff, not fourteen.</p>
"""],
    "skills": {"title": "Patient experience plan and marketing review",
               "intro": "Write a patient experience plan with at least three channels and review one advertisement with the four questions.",
               "items": [("Explains response bias and uses channels beyond surveys.", False),
                         ("Reports grievances and compliments by cause monthly.", False),
                         ("Applies the four marketing questions to an advertisement.", False),
                         ("Refuses payments or gifts for referrals.", True),
                         ("Accepts new patients only at the rate of safely staffed capacity.", True),
                         ("Includes a patient representative in quality meetings.", False)],
               "placement": "Sit with two patients who rarely speak up and ask what one thing would make their sessions better."},
    "quiz": [
        ("In the ICH CAHPS study by Dad and colleagues, how did responders compare with nonresponders?",
         ["Sicker", "Healthier, with lower mortality and fewer hospitalizations", "Identical", "Younger only"],
         1, "Surveys under-represent the sickest patients."),
        ("A flyer offers a &ldquo;free first session&rdquo; covered by the package. The problem is:",
         ["Font size", "It presents covered care as a free gift", "It is too short", "It is in English"],
         1, "Misleading claims attract by inducement."),
        ("A 500-peso thank-you for every referral is:",
         ["Good community relations", "A referral payment to avoid", "Required by PhilHealth", "A tax"],
         1, "Referral payments create inducements and legal risk."),
        ("A unit has 14 free slots but can safely staff 8 more patients. How many should it accept?",
         ["14", "8", "22", "0"],
         1, "The narrowest gate sets the pace."),
        ("A unit reports zero complaints all year. This means:",
         ["Perfect care, certainly", "Possibly that patients do not feel safe to complain", "PhilHealth will pay more", "No action is needed"],
         1, "Silence is not proof of quality."),
        ("Who is best placed to collect bedside feedback?",
         ["The person who controls the patient&rsquo;s schedule", "Someone who does not control the patient&rsquo;s schedule or slot", "The owner only", "Nobody"],
         1, "Patients speak more freely to someone without power over their slot."),
    ],
    "terms": [("Barangay health worker", "A community health volunteer in the barangay.")],
    "readings": [],
    "calcs": [],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
