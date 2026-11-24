# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 13: The Schedule, Absences, and Replacements. Written for this series from published sources."""

MODULE = {
    "image_alt": "At 5:20 in the morning a head nurse reads a message on her phone at the nurses' station while reaching for the desk telephone; the roster board behind her has one empty slot.",
    "objectives": [
        "Calculate how many nurses a unit must employ from its stations, shifts, staffing rule, and relief factor.",
        "Build a roster that keeps at least 11 hours between shifts and avoids long runs and long weeks.",
        "Approve or decline a shift swap with a written rule that protects skills on the floor and rest between shifts.",
        "Fill a same-day absence in a fixed order, and escalate instead of opening below the minimum.",
        "Handle absenteeism and tardiness fairly: log every event, talk first, and follow due process with HR.",
        "Plan the bridge between a resignation and a new nurse who is cleared to work alone.",
    ],
    "big": """
{{plain:A roster is like a bridge built for a load. The engineer does not design it for the weight of an average day; she adds a safety margin for the heavy truck, the storm, and the bolt that rusts early. A roster built with no margin works on paper until the first nurse calls in sick.}}
<p>The picture has a limit. A bridge fails all at once. A roster with no margin fails a little every week: an extra shift here, a quick return there, a tired nurse who skips the check without an alarm. Module 8 showed how thin staffing reaches the patient. This module is about the schedule that decides how thin it gets.</p>
{{fig:hn13_fte}}
{{cards:Key terms for this module|Full-time equivalent (FTE)::One nurse working a full regular week. Two half-time nurses are one FTE.|Relief factor::The multiplier that adds staff to cover leave, sick days, and training. A factor of 1.2 adds one nurse for every five on the roster.|Quick return::Less than 11 hours of rest between the end of one shift and the start of the next.|Change request::A written request to change an assigned shift, including a swap with another nurse.|Reliever pool::Qualified nurses who have agreed in advance to be called for open shifts.|Tardiness::Arriving after the scheduled start of a shift.|Habitual::The point at which a pattern of absence or lateness becomes a formal matter under your employer&rsquo;s rules.}}
""",
    "case": {"title": "The 5:20 text", "html": """
<p>At 5:20 on Monday, Ms. Rica Santos texts that she has a fever and cannot come in. It is her third Monday absence this month. Twelve stations open at 6:00. With her out, two signed-off nurses are on the morning roster; one of them, Mr. Jun Reyes, holds the only current ACLS certificate.</p>
<p>Mr. Reyes replies in the group chat that he can &ldquo;just stay for the afternoon too.&rdquo; He worked the late shift on Sunday until 9:00 PM and started at 5:30 this morning. On the roster board you also find a note: Ms. Ana Lim and Mr. Paolo Cruz have agreed between themselves to swap Wednesday shifts. Nobody asked you.</p>
""", "questions": ["How do you fill the gap for this morning, and in what order?",
                  "Should you accept Mr. Reyes&rsquo;s offer to stay for the afternoon?",
                  "What do you do about Ms. Santos&rsquo;s Monday absences, and about the private swap?"]},
    "sections": [
        ("why", "Why the roster matters", "Why the roster is a safety tool", """
<p>Tired nurses make more errors, and the roster decides how tired they are. In a logbook study of 393 hospital staff nurses, the risk of an error rose when shifts ran past twelve hours, when nurses worked overtime, and when they worked more than forty hours a week.[[hn_rogers2004]] Rest between shifts matters as much as shift length. Among 1,538 Norwegian nurses, a month with more quick returns was followed by more sick leave the next month, and 83% of the nurses had at least one quick return in a year.[[hn_vedaa2017]]</p>
<p>Finnish payroll records from more than 12,000 shift workers tell the same story from another angle: weeks over 40 hours, several night shifts in a row, and five or more quick returns in 28 days were each followed by more short sickness absence.[[hn_ropponen2019]] In Danish and Finnish nurses, long runs of night shifts were associated with more long-term sickness absence.[[hn_larsen2020]]</p>
<p>These are observational studies from hospitals in other countries, and none was done in a dialysis unit. They show associations, not a proven limit. They still point the same way, and the mechanism is plain: short rest means short sleep, short sleep means slower attention and more illness, and illness means more absences that someone else must cover. That is a loop, like the overload loop in Module 8, and the roster is where you can break it.</p>
{{key:A roster that causes quick returns and long weeks creates the very absences it then has to fill.}}
"""),
        ("fte", "How many nurses", "How many nurses the schedule really needs", """
<p>Staffing starts with the stations, not with the people you happen to have. Build the number in five steps and write each one down, so that anyone can check it.</p>
{{flow:From stations to nurses|Nurses per shift::Stations &divide; 4, rounded up. The DOH provision is one nurse for every four hemodialysis stations.[[doh2012]] The head nurse is not counted when she is not assigned patients.|Shifts per week::Treatment shifts per day &times; operating days per week.|Nurse-shifts::Nurses per shift &times; shifts per week.|Full-time nurses::Nurse-shifts &divide; shifts one nurse works per week.|Relief::Multiply by the relief factor and round up. This is the number on payroll.}}
{{formula:<strong>Worked example.</strong> 12 stations &divide; 4 = 3 nurses per shift. 3 shifts &times; 6 days = 18 shifts. 3 &times; 18 = 54 nurse-shifts a week. 54 &divide; 5 = 10.8 full-time nurses. 10.8 &times; 1.2 = 13.0, so 13 nurses on payroll.}}
<p><strong>Where the relief factor comes from.</strong> Every nurse is away for some scheduled days: leave, sick days, training, and the days she spends orienting someone else. If a nurse is scheduled for 260 days a year and is away for 40, the unit needs 260 &divide; 220 = 1.18 nurses to fill each position. Calculate your own factor from last year&rsquo;s attendance records rather than borrowing a number. A unit staffed at exactly 10.8 nurses has a relief factor of 1.0, which means the first sick day breaks the ratio.</p>
<p>Count ACLS cover separately. A roster can have enough nurses and still leave a shift with no one who holds a current ACLS certificate. Mark it as a column on the roster, not as a hope.</p>
{{scene:Eleven nurses on payroll|<p>A twelve-station unit running three shifts six days a week has 11 nurses on payroll. On paper, 11 is more than the 10.8 the arithmetic asks for. In practice, one nurse is on maternity leave from July, another takes her vacation in May, and two are booked for an ACLS course in March.</p>
<p>From April to September, the unit is short almost every week, and the gaps are filled with overtime and quick returns. Sick leave rises, which makes the gaps worse. The head nurse calculates the unit&rsquo;s own relief factor from last year&rsquo;s attendance: 1.21. At 10.8 &times; 1.21 = 13.1, the unit needs 13 nurses. She brings the calculation, the overtime hours, and the quick-return count to nursing administration. The request is easier to approve because every step can be checked.</p>}}
"""),
        ("rest", "Protecting sleep", "Building a roster that protects sleep", """
{{fig:hn13_fatigue}}
{{cards:Three roster rules|At least 11 hours between shifts::No quick returns. An early shift after a late shift is the most common one.|No early after late::Rotate forward: early, then late, then rest.|Avoid long runs and long weeks::Watch runs of five or more days and weeks over 40 hours.}}
<p>The 11-hour line comes from the research on quick returns, not from a Philippine regulation. Use it as your unit&rsquo;s rule unless your employer sets a stricter one. Philippine law sets the normal hours of work, overtime pay, night-shift pay, and the weekly rest day; your HR office applies them to your unit.[[hn_laborcode]]</p>
<p><strong>Fairness is part of safety.</strong> When the same nurses always get the hard shifts, they leave. Publish the roster at least two weeks ahead, rotate Saturdays and holidays by a visible rule, and keep a running count of who worked them. Collect leave requests by a fixed date and approve them in the order received, within a cap per week. A nurse who can predict her schedule can arrange childcare and transport; a nurse who cannot is the one who calls in at 5:20.</p>
{{call:Stop and raise it with nursing administration when the only way to fill the roster is to schedule quick returns or regular weeks over 40 hours. That is a staffing shortage, and it needs a staffing decision, not a tired nurse.}}
"""),
        ("swaps", "Change requests", "Change requests and shift swaps", """
{{fig:hn13_swap}}
<p>Swaps keep nurses&rsquo; lives workable, and a good unit allows them. The risk is a swap that quietly removes the only ACLS nurse from a shift, or that gives one nurse a late shift followed by an early one. A written rule prevents both, and it also makes your decisions look fair, because they are the same for everyone.</p>
{{flow:The swap rule|In writing, before the deadline::For example, 48 hours before the earlier of the two shifts, using the unit form. Emergencies go to the head nurse directly.|Same skills on the floor::The incoming nurse holds the same sign-offs needed on that shift, including ACLS if she replaces the ACLS nurse.|No quick return or overtime created::Check both nurses&rsquo; weeks, not just the swapped days.|Head nurse approves::Approve or decline, and give the reason in writing when you decline.|Roster updated and posted::The posted roster is the only roster. A swap that is not on it did not happen.}}
<p>A swap agreed privately and not approved is not a swap. If both nurses come, the unit pays twice; if neither comes, a station closes. Explain the rule at a staff meeting before you enforce it, then enforce it the same way every time.</p>
{{scene:The swap that removed the only ACLS nurse|<p>Mr. Carlo Reyes and Ms. Bea Santos agree to swap: he takes her Thursday afternoon shift, and she takes his Saturday morning. They submit the form on time. Both nurses are signed off to work alone, and neither swap creates a quick return.</p>
<p>When you check the Saturday roster, though, Mr. Reyes is the only nurse on that shift with a current ACLS certificate, and Ms. Santos does not hold one. The swap passes every rule except the one about skills on the floor. You decline it in writing, give the reason, and suggest a different Saturday nurse who holds ACLS and is willing to trade. The rule did not stop the nurses from swapping. It stopped the Saturday shift from opening without ACLS cover.</p>}}
"""),
        ("callout", "Same-day absence", "When someone calls in sick", """
{{fig:hn13_callout}}
{{flow:Filling a same-day gap|Log the call::Time, name, and the reason given. Do not interrogate a sick nurse on the phone; you only need enough to plan.|Check against the minimum::Stations planned &divide; 4, and ACLS cover. Use calculator 4.|Call relievers in list order::The reliever list names qualified nurses, their sign-offs, and how to reach them. Calling in a fixed order is fair and avoids favorites.|Extra hours only within rest rules::A nurse who offers to stay may do so only if it keeps 11 hours of rest before her next shift and does not create a very long day.|Adjust the day with the physician::Stagger start times, or move patients to another shift, only with the nephrologist&rsquo;s agreement.}}
{{call:Stop and call nursing administration, the clinical head, and the physician on duty if relief has not arrived by the scheduled start and you are below the minimum or without ACLS cover. Do not open short. Follow your unit&rsquo;s protocol while you call.}}
<p>Write the reliever list before you need it, and test it. A list with outdated numbers, or names that have not worked in your unit for a year, is not a plan. Keep relievers current: orientation to your machines, sign-offs on file, and at least one shift every few months.</p>
"""),
        ("attendance", "Absence and lateness", "Absenteeism and tardiness: fair, documented, consistent", """
{{fig:hn13_attendance}}
<p>Absence and lateness are both safety issues and people issues. A late nurse at 6:00 delays four patients and pushes every session later; a pattern of absences tells you something is wrong in that nurse&rsquo;s life or in the job. Your role is to notice the pattern early, respond the same way for everyone, and leave the formal decisions to the process your employer has set.</p>
{{flow:From pattern to process|Log every event::Same fields for everyone: date, minutes late or shift missed, notice given, reason offered. A log kept only for nurses you are worried about is not fair and will not stand up.|Notice the pattern::Your employer&rsquo;s code of conduct defines when lateness or absence becomes a disciplinary matter. Review the log monthly.|Talk first::In private, describe the pattern, then ask what is going on. Transport, childcare, a sick parent, and the nurse&rsquo;s own health are common answers. Many can be solved with a different shift or an earlier jeepney.|Agree and record::What will change, what support you will give, and when you will review it.|Due process::If the pattern continues, refer it to HR. Do not issue sanctions on your own.}}
<div class="table-wrap"><table>
<thead><tr><th>Where you work</th><th>What governs discipline</th><th>What it means for you</th></tr></thead>
<tbody>
<tr><td>Private unit</td><td>The Labor Code and DOLE Department Order 147-15: a first written notice stating the specific facts and giving at least five calendar days to explain, a chance to be heard, then a written decision.[[hn_dole147]]</td><td>Your log and your notes from the talk are the facts HR will use. Keep them specific: dates and minutes, not &ldquo;always late.&rdquo;</td></tr>
<tr><td>Government unit</td><td>Civil Service Commission rules. Habitual tardiness is lateness ten times a month for at least two months in a semester, or two consecutive months. Habitual absenteeism is unauthorized absence beyond the 2.5 days of monthly leave credit for at least three months in a semester, or three consecutive months.[[hn_csc1991]][[hn_csc1998]]</td><td>Your attendance records feed the semestral report. Make sure leave is filed and approved so that authorized absences are not counted as unauthorized.</td></tr>
</tbody></table></div>
<p>This is not legal advice. Check the current rules with your HR office before any notice is written. What you control is the quality of the record and the fairness of the first conversation.</p>
{{scene:Twelve minutes late, three times a week|<p>The log shows that Ms. Andrea Flores has been 10 to 15 minutes late for the 6:00 shift eleven times in five weeks, always on Mondays, Wednesdays, and Fridays. Her work at the chair is excellent.</p>
<p>In a private conversation, you describe the pattern and ask what is happening. Her mother started dialysis at another unit on those same days, and Ms. Flores drops her off at 5:30 on the way. The first jeepney after that gets her to work just after 6:00. With nursing administration, you move her to the 7:00 start on those days, where a nurse is also needed. The lateness stops. Had the first step been a written warning, the unit might have lost a good nurse over a problem the schedule could fix. Had the talk not helped, the log would already hold a fair, consistent record for the formal process.</p>}}
{{key:Log every event the same way for everyone, talk before you write, and let HR run the process.}}
"""),
        ("backfill", "Replacing a nurse", "Replacing a nurse who leaves", """
{{fig:hn13_backfill}}
<p>A resignation opens a gap longer than the notice period. Under the Labor Code, a nurse who resigns without just cause gives at least one month&rsquo;s written notice.[[hn_laborcode]] A new nurse is not on the roster on her first day, though. She needs orientation to your machines, your water system, and your emergency roles, and each skill must be signed off before she counts toward the ratio. That usually takes weeks. The real gap runs from the departing nurse&rsquo;s last day to the day the new nurse is cleared to work alone.</p>
{{flow:Closing the replacement gap|The day the letter arrives::Tell nursing administration and start recruiting at once. Do not wait for the last day.|During the notice period::Ask the departing nurse to hand over her preceptees, her duties, and her knowledge of individual patients.|Plan the bridge::Book relievers for the gap by name and date. Check rest rules for anyone taking extra shifts.|Orient on a schedule::A named preceptor, a dated checklist, and sign-offs recorded in the competency matrix.|Learn from the exit::Ask why she is leaving. If it is workload, schedule, or support, it will happen again.}}
<p>The Philippines has a well-documented nurse shortage, driven in large part by migration overseas, and dialysis units compete with hospitals and with each other for experienced nurses. Retention is cheaper than recruitment. The schedule is one of the few things that matter to nurses that a head nurse fully controls.</p>
{{scene:Seven weeks, not four|<p>Ms. Joy Mercado hands in her resignation on October 1. Her last day is October 31. The administrator says, &ldquo;We have a month. That&rsquo;s plenty of time.&rdquo;</p>
<p>You count the real gap. Recruiting takes two weeks, and the new nurse starts on November 15. She needs about five weeks of orientation and sign-offs before she can work alone, so she counts toward the ratio around December 20. The real gap runs from November 1 to December 20, about seven weeks, not four. You book relievers by name for those seven weeks on October 2, check that no one taking extra shifts will have a quick return, and ask Ms. Mercado to spend her last week handing over her two preceptees. The gap still exists, but now it is planned.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Filling this morning.</strong> Log Ms. Santos&rsquo;s message. Two signed-off nurses are present for twelve stations, so at most eight can open on nursing grounds. ACLS cover is met, because Mr. Reyes holds it. Call the reliever list in order now. If a reliever arrives before 6:00, open all twelve. If not, tell the physician on duty which four patients are waiting and ask which can start later or move to another shift. Inform nursing administration.</p>
<p><strong>Mr. Reyes&rsquo;s offer.</strong> Decline it, kindly. He finished at 9:00 PM and started at 5:30 AM, so he has already had a quick return of 8.5 hours. Adding the afternoon would make a very long day on short sleep, and he is your only ACLS nurse. Thank him, and solve the afternoon from the reliever list.</p>
<p><strong>The Monday absences.</strong> Three Mondays is a pattern worth a conversation, not yet a disciplinary matter. Log today the same way you log everyone. This week, talk with Ms. Santos in private: describe the dates, then ask what is going on. If it is illness, suggest she see a physician and file her leave properly. If it is something else, such as childcare on Mondays, a different shift may solve it. Record what you agreed and when you will review it.</p>
<p><strong>The private swap.</strong> It is not approved, so the posted roster stands. Ask Ms. Lim and Mr. Cruz to submit it on the form today. Then check it: same sign-offs, ACLS cover on Wednesday, and no quick return or overtime for either of them. If it passes, approve and post it. Use it as the example when you explain the swap rule at the next staff meeting.</p>
"""],
    "skills": {"title": "Roster and attendance",
               "intro": "Build a two-week roster for a synthetic unit, process two change requests and a same-day absence, and hold a practice attendance conversation while your facilitator observes.",
               "items": [
                   ("Calculates nurses per shift, nurse-shifts, full-time nurses, and payroll nurses with the relief factor shown.", True),
                   ("Marks ACLS cover on every shift of the roster.", True),
                   ("Builds the roster with no quick returns and no regular weeks over 40 hours.", True),
                   ("Rotates weekend and holiday shifts by a written rule.", False),
                   ("Applies the swap rule and states the reason for any decline in writing.", False),
                   ("Fills a same-day absence in list order and checks rest before accepting extra hours.", True),
                   ("Escalates instead of opening below the minimum or without ACLS cover.", True),
                   ("Logs attendance events with the same fields for every nurse.", True),
                   ("Opens the attendance conversation with specific dates and an open question.", False),
                   ("Refers continuing patterns to HR without issuing sanctions alone.", True),
               ],
               "placement": "Pull last quarter&rsquo;s roster. Count quick returns, weeks over 40 hours, and same-day absences per nurse, and bring the three numbers to your next meeting with nursing administration."},
    "quiz": [
        ("A unit has 16 stations, runs 3 shifts a day, 6 days a week. How many nurse-shifts does it need each week at one nurse per four stations?",
         ["48", "72", "64", "96"], 1,
         "16 &divide; 4 = 4 per shift; 3 &times; 6 = 18 shifts; 4 &times; 18 = 72."),
        ("What does a relief factor of 1.2 mean?",
         ["Each shift gets 20% more patients", "One extra nurse is employed for every five on the roster, to cover leave, sickness, and training", "Nurses work 20% longer shifts", "The ratio becomes 1 to 5"], 1,
         "It is the margin that keeps the ratio when people are away."),
        ("What is a quick return?",
         ["A patient who returns early", "Less than 11 hours of rest between two shifts", "Two shifts in one week", "Coming back from leave early"], 1,
         "An early shift right after a late one is the most common example."),
        ("In the Norwegian registry study, what followed a month with more quick returns?",
         ["Fewer errors", "More sick leave the next month", "Better sleep", "Higher pay"], 1,
         "Quick returns were associated with more sick-leave days and spells."),
        ("What kind of evidence links shift patterns to errors and sickness absence?",
         ["Randomized trials in dialysis units", "Observational studies in hospital nurses and public-sector workers", "Animal studies", "No evidence at all"], 1,
         "Consistent associations and a plain mechanism, but no trial and no dialysis-specific data."),
        ("A nurse finished at 9:00 PM. When is the earliest she should start again under an 11-hour rule?",
         ["5:30 AM", "6:00 AM", "8:00 AM", "Noon"], 2,
         "9:00 PM plus 11 hours is 8:00 AM."),
        ("Two nurses swap shifts by text and tell no one. What is the status of the swap?",
         ["Valid, because both agreed", "Not a swap until it is approved and posted", "Valid if the head nurse finds out later", "Valid on weekends only"], 1,
         "The posted roster is the only roster."),
        ("Which check is most likely to be missed when approving a swap?",
         ["The nurses&rsquo; names", "Whether the swap removes the only ACLS nurse from a shift or creates a quick return", "The color of the form", "The date of the request"], 1,
         "Check skills on the floor and both nurses&rsquo; whole weeks."),
        ("A nurse calls in sick at 5:20. What do you do first?",
         ["Ask for a medical certificate on the phone", "Log the call and check the shift against the minimum and ACLS cover", "Open all stations and hope", "Cancel the morning shift"], 1,
         "Log it, then count, then call relievers in order."),
        ("Why call relievers in a fixed list order?",
         ["It is faster", "It is fair, avoids favorites, and makes the process predictable", "It is required by PhilHealth", "It saves phone credit"], 1,
         "Fairness is part of keeping relievers willing."),
        ("Relief has not arrived at 6:00 and you are below the minimum. What do you do?",
         ["Open all stations", "Escalate to administration, the clinical head, and the physician; do not open short", "Ask the orientee to take four patients", "Send all patients home"], 1,
         "Which patients wait or move is the physician&rsquo;s decision."),
        ("What is the best first response to a pattern of Monday absences?",
         ["A written warning", "A private conversation that states the dates and asks what is going on", "Posting the dates on the board", "Ignoring it"], 1,
         "Talk first. The cause is often solvable."),
        ("In a private unit, what does the first written notice under DOLE Department Order 147-15 give the employee?",
         ["Twenty-four hours to reply", "At least five calendar days to explain in writing", "No chance to reply", "Thirty days of paid leave"], 1,
         "Then an opportunity to be heard, then a written decision."),
        ("In a government unit, which pattern meets the CSC definition of habitual tardiness?",
         ["Late three times in one month", "Late ten times a month for two consecutive months", "Late once a week for a year", "Late twice on one day"], 1,
         "Or ten times a month for at least two months in a semester."),
        ("A nurse resigns with one month&rsquo;s notice. When does the staffing gap really end?",
         ["On her last day", "When the new nurse is cleared to work alone", "When the vacancy is posted", "When the new nurse is hired"], 1,
         "Orientation and sign-off take weeks; plan the bridge."),
    ],
    "terms": [("Full-time equivalent (FTE)", "One nurse working a full regular week."),
              ("Relief factor", "The multiplier that adds staff to cover leave, sick days, and training."),
              ("Quick return", "Less than 11 hours of rest between two shifts."),
              ("Change request", "A written request to change an assigned shift, including a swap."),
              ("Reliever pool", "Qualified nurses who have agreed in advance to be called for open shifts."),
              ("Tardiness", "Arriving after the scheduled start of a shift."),
              ("Twin-notice rule", "In private employment, a notice to explain, a chance to be heard, and a written decision."),
              ("Competency matrix", "A table of each nurse&rsquo;s signed-off skills, with dates.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Using attendance and staffing data in quality review."),
                 ("code-blue-acls-dialysis-unit.html", "Why ACLS cover matters on every shift.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c13", "calc-dialysis-head-nurse-toolkit.html#c4"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
