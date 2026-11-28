# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 13: Team, Code Status, Debrief and Practice. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dialysis team in a short standing debrief after a drill around a manikin in a recliner, the facilitator holding a clipboard.",
    "objectives": [
        "Assign and combine resuscitation roles for a small, standard or large team, and transfer leadership cleanly when another team arrives.",
        "Use closed-loop communication for every order, and keep the recorder&rsquo;s timeline accurate.",
        "Check code status before the emergency, respect a documented decision, and support families with presence and plain language.",
        "Lead a five-question debrief after a drill or a real event, and turn findings into owned system changes.",
        "Use three separate performance reports (clinical skills, team coordination, system readiness), state their data sources, and plan a practice cadence.",
    ],
    "big": """
{{plain:A resuscitation team is like a small orchestra without rehearsal time. Everyone knows how to play; the danger is that they play at different speeds, or two people play the same part while another part is silent. A conductor, a shared score and a habit of listening to each other turn skilled individuals into a team.}}
<p>The picture has a limit. An orchestra rehearses the same piece many times; a dialysis team meets each arrest with a different patient, different staff on the roster, and a machine in the middle of the room. That is why the team skills (roles, closed-loop orders, leadership handover, debrief) must be practiced as deliberately as compressions, and why the debrief afterward is where most of the learning happens.</p>
<p>This module closes the course. It covers the team, the ethical questions that come before and after an arrest, and the practice system that keeps the whole unit ready.</p>
{{cards:Key terms for this module|Closed-loop communication::An order directed to a named person, repeated back, and confirmed when done.|Leadership handover::The explicit transfer of the leader role to an arriving clinician.|Code status::A documented decision about whether to start cardiopulmonary resuscitation (CPR) if the heart stops.|Family presence::Allowing family members to be present during resuscitation, with a staff member supporting them.|Debrief::A short structured review after a drill or event.|Psychological safety::A team climate where anyone can speak up about a problem without fear.}}
""",
    "case": {"title": "The debrief nobody wanted", "html": """
<p>At 11:05 a.m., after a 25-minute resuscitation that ended with transfer of a patient with ROSC, the team at a unit in Pampanga is exhausted. The patient&rsquo;s daughter arrived during the arrest and was kept in the waiting area alone. During the event, two physicians gave conflicting orders for a minute after the attending arrived; one dose of epinephrine was given twice; and the watcher was pulled into compressions, during which another patient&rsquo;s blood pressure fell unnoticed for ten minutes.</p>
<p>The charge nurse, Ms. Maricel Bernardo, says, &ldquo;Let us have a quick debrief.&rdquo; A senior nurse replies, &ldquo;We did our best. Nobody wants to be blamed. Let us just go back to work.&rdquo;</p>
""", "questions": ["Should the team debrief now, and how can it avoid blame?",
                  "Which problems were system problems, and who owns each fix?",
                  "What should have happened for the daughter?"]},
    "sections": [
        ("roles", "Roles and leadership", "Roles, combined roles, and the arriving team", """
<p>Roles named at the start of the shift (Module 1) are confirmed at the start of the arrest: the leader says them aloud. Small teams combine roles; large teams risk crowding. The leader stays hands-off whenever staffing allows.</p>
{{fig:rl13_roles}}
<div class="table-wrap"><table>
<thead><tr><th>Team size</th><th>Roles</th></tr></thead>
<tbody>
<tr><td>3 staff</td><td>Leader + defibrillator and drugs; compressor + airway (swapping every 2 minutes); circuit nurse + recorder. Watcher: called from another area</td></tr>
<tr><td>5 to 6 staff</td><td>Leader; two compressors (one also airway); defibrillator and drugs; circuit nurse then recorder; watcher</td></tr>
<tr><td>8 or more</td><td>Every role separate; extra staff wait outside the circle until called; the watcher never joins</td></tr>
</tbody></table></div>
<h3>Leadership handover</h3>
<p>When the physician-on-duty, the attending nephrologist or a hospital code team arrives, two leaders giving orders at once is a known source of error. The arriving clinician asks for a 15-second summary (time down, rhythms, shocks, drugs and times, circuit status, suspected cause), then says aloud: &ldquo;I am taking the lead.&rdquo; The previous leader confirms: &ldquo;You have the lead,&rdquo; and takes a named role.</p>
{{key:The leader names roles aloud. When a new leader arrives: summary, &ldquo;I am taking the lead,&rdquo; &ldquo;You have the lead.&rdquo; One voice gives orders.}}
"""),
        ("communication", "Closed loop", "Closed-loop orders and the recorder&rsquo;s timeline", """
<p>Most medication errors in resuscitation come from orders that nobody owned: said to the room, heard by two people, or by nobody. Closed-loop communication fixes this with three parts: an order to a named person, a read-back, and a report when done.</p>
{{fig:rl13_closed_loop}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Name and order</td><td>&ldquo;Joy, epinephrine 1 milligram IV now.&rdquo;</td></tr>
<tr><td>Read-back</td><td>&ldquo;Epinephrine 1 milligram IV.&rdquo;</td></tr>
<tr><td>Done</td><td>&ldquo;Epinephrine 1 milligram in, 10:43.&rdquo;</td></tr>
<tr><td>Recorded</td><td>Recorder writes the time and calls the next dose due: &ldquo;Next epinephrine due 10:47.&rdquo;</td></tr>
</tbody></table></div>
<p>The recorder is not a passive scribe. The recorder keeps the clock, calls the two-minute checks and drug intervals, and keeps the timeline that the debrief and the handover depend on. In the case, the doubled epinephrine dose is the predictable result of orders given to the room, without a recorder calling the last dose. The facilitator recorder in the <a href="resuscitation-lab-practice.html">Practice Lab</a> produces a timestamped timeline in drills.</p>
{{key:Every order: a name, a read-back, a &ldquo;done&rdquo; with the time. The recorder keeps the clock and calls what is due next.}}
"""),
        ("ethics", "Code status and families", "Code status, families, and dignity", """
<p>The 2025 AHA ethics chapter discusses advance directives and shared decision-making, decisions to start, withhold or stop resuscitation, cultural and religious considerations, family presence, and the effect of resuscitation on families and staff.[[aha2025_ethics]] For a dialysis unit, the practical work happens before the emergency.</p>
<div class="table-wrap"><table>
<thead><tr><th>Before</th><th>During</th><th>After</th></tr></thead>
<tbody>
<tr><td>Ask about goals of care at admission and at changes; document code status where the night shift and the charge nurse can see it</td><td>Follow a documented decision; if none exists, start CPR</td><td>Tell the family in plain words, early, in a private space</td></tr>
<tr><td>Involve the attending nephrologist and the family in decisions about CPR for patients with very poor prognosis</td><td>Offer the family a supported chance to be present, if your unit allows it, with one staff member beside them</td><td>Offer the family time with the patient and the social worker</td></tr>
<tr><td>Check advance directives and the Philippine legal context with your facility&rsquo;s policy</td><td>Never debate code status at the chair while CPR is needed</td><td>Document what was said and who said it</td></tr>
</tbody></table></div>
<p>In the Philippines, the legal standing of advance directives and do-not-resuscitate orders is set by facility policy and evolving law; this course does not give legal advice. What it does say is practical: a code status decision made calmly, with the patient and family and the attending nephrologist, protects everyone from an impossible decision at the worst moment. In the case, the daughter waited alone; a staff member could have stayed with her, told her what was happening, and, if unit policy allowed, offered her a supported place in the room.</p>
{{key:Settle code status before the emergency, follow a documented decision, and never leave a family alone during a resuscitation.}}
"""),
        ("debrief", "Debrief and practice", "The debrief, the three reports, and the practice system", """
<p>A debrief is not a search for someone to blame. It is the cheapest system fix available: ten minutes, while memories are fresh, to find what delayed care and who will change it. Structured debriefing after simulation is associated with better learning outcomes than no debriefing, in a meta-analysis of simulation studies.[[cheng2014]]</p>
{{fig:rl13_debrief}}
{{flow:The five-question debrief|What happened?::A short factual timeline from the recorder&rsquo;s sheet.|What helped?::Name the actions that worked, so they are repeated.|What delayed care?::Equipment, communication, roles, information. Systems, not personalities.|What will change?::One to three concrete changes.|Who owns it, and when do we rehearse?::A name and a date for each change, and the next drill.}}
<h3>Three reports, never one score</h3>
<p>Performance after a drill is reported in three parts: <strong>clinical skills</strong> (recognition, time to first compression, pads, first shock, drug timing, ROSC check), <strong>team coordination</strong> (roles named, closed-loop orders, leadership handover, watcher kept, handover complete), and <strong>system readiness</strong> (cart in place, defibrillator charged, oxygen full, numbers posted, ambulance called on time). Each report states its data source: a feedback device, a defibrillator download, observer timestamps, or participant entry. Browser buttons cannot measure compression depth or ventilation quality. The <a href="calc-resuscitation-lab-toolkit.html#tool-2">megacode timeline analyzer</a> computes the times from a recorder log.</p>
{{fig:rl13_reports}}
<p>Safety-critical errors (compressions not started, a shock while someone touches the patient, contaminated blood returned, an adult dose given to a child, an access left open) require coached repeat practice even when the overall score is high. Pass marks the unit sets for itself are educational standards, not validated measures of competence. There are no public individual rankings.</p>
<h3>How often to practice</h3>
<p>Spaced practice is at least as effective as one long session: a 2026 systematic review of 15 comparative studies found spaced simulation training generally as effective as massed training, with some advantage for retention, and no study of patient outcomes.[[patocka2026]] A 2024 ILCOR review of nine simulation studies found that rapid cycle deliberate practice shortened simulated time to defibrillation and epinephrine, at very low certainty and with no patient outcomes.[[abelairas2024]] Neither defines the best interval for a dialysis unit. This course proposes onboarding, a weekly five-minute refresher, a monthly short drill, a quarterly integrated megacode and a targeted rehearsal after any real event; that cadence is an Academy teaching choice.</p>
{{key:Debrief every drill and every real event in five questions, report skills, teamwork and systems separately, and practice little and often.}}
{{call:After any real resuscitation, the charge nurse arranges a debrief the same day and reports system findings to the head nurse and the Dialysis Clinical Head. Follow your unit protocol for incident reporting, and always inform the attending nephrologist.}}
"""),
    ],
    "debrief": ["""
<p><strong>Debrief now, without blame.</strong> Yes, briefly, the same day. Ms. Bernardo sets the rule aloud: &ldquo;We are looking at our system, not at people.&rdquo; She uses the five questions and the recorder&rsquo;s sheet. Ten minutes is enough. The senior nurse&rsquo;s fear of blame is the reason to structure the debrief, not a reason to skip it.</p>
<p><strong>System problems and owners.</strong> Conflicting orders: no leadership handover script; owner, the Dialysis Clinical Head, who adds the &ldquo;I am taking the lead&rdquo; script to the unit protocol and the next drill. The doubled epinephrine: orders given to the room and no recorder calling doses; owner, the head nurse, who makes the recorder role and closed-loop orders part of every drill. The watcher pulled into compressions: owner, the charge nurse, who adds &ldquo;the watcher never joins&rdquo; to the shift huddle. Each change gets a date and a rehearsal.</p>
<p><strong>The daughter.</strong> A staff member, or the social worker, should have stayed with her, told her what was happening in plain words, and offered her a supported chance to be present if unit policy allowed. Afterward she should hear from the leader or the attending nephrologist, privately, before she hears it from anyone else.</p>
"""],
    "skills": {"title": "Team leadership and debrief",
               "intro": "Lead a facilitated megacode with role assignment and a leadership handover, then lead the debrief while a supervisor observes.",
               "items": [
                   ("Names every role aloud at the start of the arrest, combining roles safely for the team size.", True),
                   ("Uses closed-loop orders for every drug and shock.", True),
                   ("Performs a leadership handover with a summary and the explicit words.", False),
                   ("Keeps the watcher out of the arrest.", True),
                   ("Checks code status before or during the event per protocol and assigns a staff member to the family.", False),
                   ("Leads a five-question debrief focused on systems, ending with owners and dates.", True),
                   ("Reports clinical, team and system findings separately, with data sources.", False),
               ],
               "placement": "Facilitate one monthly drill in your unit using the facilitator recorder, and present the three reports and the action list at the staff meeting."},
    "terms": [("Closed-loop communication", "Named order, read-back, and confirmation when done."),
              ("Leadership handover", "Explicit transfer of the leader role."),
              ("Code status", "A documented decision about CPR."),
              ("Family presence", "Supported presence of family during resuscitation."),
              ("Debrief", "A short structured review after an event or drill."),
              ("Psychological safety", "A climate where anyone can speak up without fear.")],
    "readings": [("same-event-every-role.html", "Same event, every role: the Academy&rsquo;s cross-role drill.")],
    "calcs": ["calc-resuscitation-lab-toolkit.html#tool-2", "calc-resuscitation-lab-toolkit.html#tool-5"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["13"])
