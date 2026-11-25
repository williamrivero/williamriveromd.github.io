# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 22: Serious events, insurance, and external scrutiny. Written for this course from published sources."""

MODULE = {
    "image_alt": "An older medical director sitting quietly with a grieving daughter in a small family room, a box of tissues between them.",
    "objectives": [
        "Order the owner&rsquo;s actions in the first hours after a serious event.",
        "Support honest disclosure and explain what the evidence says about communication-and-resolution programs.",
        "Support staff involved in an event.",
        "Map risks to insurance and respond to regulators and media truthfully.",
    ],
    "big": """
{{plain:After a serious event, the unit is like a house after a fire. First you get everyone out and safe, then you keep the scene as it is for the investigators, then you tell the family the truth, and only then do you think about the insurance claim.}}
<p>The picture has a limit. A fire has an obvious cause. Most serious events in dialysis have several small causes that lined up. That is why the response protects the evidence and looks for systems, not only for a person to blame.</p>
{{cards:Key terms for this module|Serious event::Harm or death that was, or may have been, caused by care.|Disclosure::Telling the patient or family honestly what happened and what will be done.|Communication-and-resolution program::A structured approach to disclosure, apology, and fair compensation.|Second victim::A staff member who is distressed after being involved in an event.}}
<p>Your work is to put care, safety, and honesty first, support your staff, and know before the event what your insurance does and does not cover.</p>
""",
    "case": {"title": "Air in the line", "html": """
<p>At a unit in Cebu City, a patient collapses during a session and dies despite resuscitation. Staff suspect an air embolism after a bloodline was reconnected. That evening, a local reporter calls the owner, Mrs. Marivic Go, and asks whether the unit is &ldquo;killing patients to save money.&rdquo; The nurse involved has gone home in tears.</p>
""", "questions": ["What happens in the first hours?", "What do you tell the family, and when?", "What do you tell the reporter?"]},
    "sections": [
        ("first-hours", "First hours", "The first hours", """
{{fig:duo22a}}
<p>Order matters. First, care for the patient and other patients on the floor. Second, make the unit safe: hold the equipment and lines involved. Third, preserve evidence: the machine, the lines, the logs, and the records stay as they are. Fourth, tell the family honestly. Fifth, support the staff involved. Sixth, report to the authorities and insurers as required. The clinical head leads the clinical review; the owner provides resources and makes sure nothing is altered or hidden.</p>
{{stop:Never alter, discard, or tidy records, equipment, or logs after a serious event.}}
{{key:Care, safety, evidence, family, staff, then reports, in that order.}}
"""),
        ("disclosure", "Disclosure", "Honest disclosure", """
<p>Families want to know what happened, that someone is sorry, and that it will not happen again. Fear of lawsuits often stops units from saying so. Evidence from programs that combine disclosure, apology, investigation, and fair offers of compensation is reassuring: in Massachusetts hospitals, a communication-and-resolution program was not associated with higher claims or costs,[[dch_kachalia2018]] and a study of New York hospitals described how cases were resolved under such a program, including when compensation was offered.[[dch_mello2016]] Both are observational and from another legal system; involve your lawyer, but do not let fear replace honesty.</p>
{{key:Tell the family what you know, say you are sorry, and promise to share what you learn.}}
"""),
        ("insurance", "Insurance", "What each policy covers", """
{{fig:duo22b}}
<p>Map each major risk to a policy before anything happens: patient injury to professional and facility liability; fire and flood to property; a cyberattack to a cyber policy if you have one; staff injury to the employer&rsquo;s legal obligations; and a long closure to business interruption cover. Mark every risk with no matching cover as a gap, and decide whether to insure it, reduce it, or accept it. Notify insurers promptly after an event, as the policy requires.</p>
{{key:Find the gaps in your cover before an event finds them for you.}}
"""),
        ("scrutiny", "Staff and scrutiny", "Staff, regulators, and the media", """
<p>Staff involved in harm often suffer guilt, fear, and sleeplessness; this second-victim response is common across health care.[[dch_seys2013]] Offer immediate support, time off if needed, and a fair review process. Most events have system causes, and a unit that punishes honest staff teaches the rest to stay silent.</p>
<p>With regulators, be prompt, complete, and truthful. With the media, name one spokesperson, protect the patient&rsquo;s privacy, express sympathy, say that a review is under way, and share findings later. Never speculate and never blame an individual in public.</p>
{{key:Support the staff, cooperate fully, and say only what is true and known.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first hours.</strong> Care for the other patients, hold the machine and lines, preserve every log, inform the family in person with the clinical head, support the nurse, and report as required.</p>
<p><strong>The family.</strong> That night, by the clinical head and a senior leader: what is known, that the unit is sorry, that a full review has started, and when they will hear more.</p>
<p><strong>The reporter.</strong> One spokesperson. Sympathy for the family, a review under way, cooperation with the authorities, no speculation, no patient details, no blame.</p>
"""],
    "skills": {"title": "Serious-event response checklist and insurance coverage review",
               "intro": "Write a first-hours checklist and map your unit&rsquo;s risks to its insurance.",
               "items": [("Orders the first-hours actions correctly.", False),
                         ("Preserves equipment, logs, and records unaltered.", True),
                         ("Supports honest disclosure to the family by the clinical team.", True),
                         ("Offers support to staff involved.", False),
                         ("Maps risks to policies and marks gaps.", False),
                         ("Names one spokesperson and prepares a truthful holding statement.", False)],
               "placement": "Ask your broker for a one-page summary of what each policy covers and excludes."},
    "quiz": [
        ("After a serious event, what comes first?",
         ["Calling the insurer", "Caring for the patient and others on the floor", "Speaking to the media", "Cleaning the station"],
         1, "Care and safety come first."),
        ("Why preserve the machine, lines, and logs?",
         ["For storage", "So the review can find the real causes", "To sell them", "PhilHealth requires it monthly"],
         1, "Altered evidence hides system causes."),
        ("What did the Massachusetts communication-and-resolution study find?",
         ["Claims and costs rose sharply", "The program was not associated with higher claims or costs", "It was illegal", "It increased deaths"],
         1, "Observational evidence from another legal system."),
        ("A nurse involved in an event is distressed. This is called:",
         ["Burnout", "A second-victim response", "Malpractice", "Insubordination"],
         1, "Support, not blame, is the right response."),
        ("What should the media hear?",
         ["Speculation about the cause", "The nurse&rsquo;s name", "Sympathy, that a review is under way, and no patient details", "Nothing at all, ever"],
         2, "One spokesperson, truthful and respectful of privacy."),
        ("A risk with no matching insurance policy is:",
         ["Covered automatically", "A gap to insure, reduce, or accept deliberately", "Illegal", "Irrelevant"],
         1, "Know your gaps before an event."),
    ],
    "terms": [("Holding statement", "A short, truthful public statement given before all facts are known.")],
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
