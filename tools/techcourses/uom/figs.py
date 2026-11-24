# -*- coding: utf-8 -*-
"""Figures for the Dialysis Unit Operations Manager / Unit Manager in Hospital track. key: (file in images/, alt text, caption).
Prompts: image-prompt-pack.md and corrected-prompts.md in the UOM/UMH v2 packet (Constitution v1.0). A figure whose file is absent
(the ten that failed the image audit) leaves an empty slot until the replacement art is produced."""

FIGS = {
    'uom00_hero': ('dialysis-unit-manager-hero-academy-v2.webp', 'Course hero: the dialysis unit manager at the center of four authority lines', 'Course hero: the dialysis unit manager at the center of four authority lines.'),  # HERO
    'uom00_map': ('dialysis-unit-manager-course-path-map-v2.webp', 'Course path map: common core, two setting branches, shared finish', 'Course path map: common core, two setting branches, shared finish.'),  # COURSE-MAP
    'uom00_calcs': ('dialysis-unit-manager-calculator-gallery-v2.webp', "The manager's toolkit: thirteen operations calculators", "The manager's toolkit: thirteen operations calculators."),  # CALC-GALLERY
    'uom01a': ('dialysis-unit-manager-decision-rights-map-v2.webp', 'Decision-rights map: four authority lines feeding one patient', 'Decision-rights map: four authority lines feeding one patient.'),  # FIG-01
    'uom01b': ('dialysis-unit-manager-opening-huddle-closed-loop-v2.webp', 'The four-minute opening huddle with closed-loop read-back', 'The four-minute opening huddle with closed-loop read-back.'),  # FIG-01B
    'uom01c': ('dialysis-unit-manager-0530-phone-call-case-v2.webp', 'Field case: the 05:30 phone call and the safe opening plan', 'Field case: the 05:30 phone call and the safe opening plan.'),  # FIG-01C
    'uom02a': ('dialysis-unit-manager-evidence-index-tracer-v2.webp', 'Evidence index and tracer: following one patient and one machine', 'Evidence index and tracer: following one patient and one machine.'),  # FIG-02
    'uom02b': ('dialysis-unit-manager-capa-five-parts-worked-example-v2.webp', 'Writing a CAPA a surveyor accepts: a worked example', 'Writing a CAPA a surveyor accepts: a worked example.'),  # FIG-02B
    'uom02c': ('dialysis-unit-manager-surprise-inspection-case-v2.webp', 'Field case: the unannounced inspection handled in ten minutes', 'Field case: the unannounced inspection handled in ten minutes.'),  # FIG-02C
    'uom03a': ('dialysis-unit-manager-roster-competency-matrix-v2.webp', 'Roster-to-competency matrix and FTE relief', 'Roster-to-competency matrix and FTE relief.'),  # FIG-03
    'uom03b': ('dialysis-unit-manager-roster-reallocation-flow-v2.webp', 'Reallocating the roster after an absence: five decisions', 'Reallocating the roster after an absence: five decisions.'),  # FIG-03B
    'uom03c': ('dialysis-unit-manager-exhausted-nurse-case-v2.webp', 'Field case: the competent but exhausted nurse', 'Field case: the competent but exhausted nurse.'),  # FIG-03C
    'uom04a': ('dialysis-unit-manager-capacity-board-interval-v2.webp', 'Station-shift capacity board and the long interdialytic gap', 'Station-shift capacity board and the long interdialytic gap.'),  # FIG-04
    'uom04b': ('dialysis-unit-manager-reschedule-priority-ladder-v2.webp', 'After a disruption: who gets the first available slot', 'After a disruption: who gets the first available slot.'),  # FIG-04B
    'uom04c': ('dialysis-unit-manager-holiday-week-calendar-case-v2.webp', 'Field case: rebuilding a holiday week so no gap exceeds three days', 'Field case: rebuilding a holiday week so no gap exceeds three days.'),  # FIG-04C
    'uom05a': ('dialysis-unit-manager-bsi-pathway-core-interventions-v2.webp', 'Bloodstream infection pathway and the CDC Core Interventions', 'Bloodstream infection pathway and the CDC Core Interventions.'),  # FIG-05
    'uom05b': ('dialysis-unit-manager-serology-result-to-action-v2.webp', 'From serology result to action within 48 hours', 'From serology result to action within 48 hours.'),  # FIG-05B
    'uom05c': ('dialysis-unit-manager-hbv-transmission-routes-v2.webp', 'How bloodborne viruses travel in a dialysis bay — and how design stops them', 'How bloodborne viruses travel in a dialysis bay — and how design stops them.'),  # FIG-05C
    'uom06a': ('dialysis-unit-manager-water-pathway-release-gate-v2.webp', 'Dialysis water pathway, sampling points and the release gate', 'Dialysis water pathway, sampling points and the release gate.'),  # FIG-06
    'uom06b': ('dialysis-unit-manager-water-log-audit-card-v2.webp', 'Auditing a water log: six required elements and three red flags', 'Auditing a water log: six required elements and three red flags.'),  # FIG-06B
    'uom06c': ('dialysis-unit-manager-copied-value-case-v2.webp', 'Field case: the missing chlorine result at 05:15', 'Field case: the missing chlorine result at 05:15.'),  # FIG-06C
    'uom07a': ('dialysis-unit-manager-incident-command-floor-v2.webp', 'Incident command roles during a dialysis-floor emergency', 'Incident command roles during a dialysis-floor emergency.'),  # FIG-07
    'uom07b': ('dialysis-unit-manager-emergency-readiness-board-v2.webp', 'Emergency readiness board: what is checked, how often, by whom', 'Emergency readiness board: what is checked, how often, by whom.'),  # FIG-07B
    'uom07c': ('dialysis-unit-manager-evacuation-drill-assembly-v2.webp', 'Facility drill: emergency disconnection, evacuation and headcount', 'Facility drill: emergency disconnection, evacuation and headcount.'),  # FIG-07C
    'uom08a': ('dialysis-unit-manager-asset-lot-traceability-v2.webp', 'Asset and lot traceability chain with reorder point', 'Asset and lot traceability chain with reorder point.'),  # FIG-08
    'uom08b': ('dialysis-unit-manager-recall-one-hour-workflow-v2.webp', 'Executing a recall within one hour', 'Executing a recall within one hour.'),  # FIG-08B
    'uom08c': ('dialysis-unit-manager-cheaper-dialyzer-decision-v2.webp', 'Field case: the cheaper dialyzer — clinical review before cost', 'Field case: the cheaper dialyzer — clinical review before cost.'),  # FIG-08C
    'uom09a': ('dialysis-unit-manager-run-chart-pdsa-v2.webp', 'Run chart with signal rules and the PDSA cycle', 'Run chart with signal rules and the PDSA cycle.'),  # FIG-09
    'uom09b': ('dialysis-unit-manager-indicator-data-dictionary-v2.webp', 'Anatomy of an indicator: the data dictionary entry', 'Anatomy of an indicator: the data dictionary entry.'),  # FIG-09B
    'uom09c': ('dialysis-unit-manager-qapi-meeting-scene-v2.webp', 'The QAPI meeting: run charts, owners and due dates', 'The QAPI meeting: run charts, owners and due dates.'),  # FIG-09C
    'uom10a': ('dialysis-unit-manager-session-claim-payment-trace-v2.webp', 'Session-to-claim-to-payment trace and session-cap meter', 'Session-to-claim-to-payment trace and session-cap meter.'),  # FIG-10
    'uom10b': ('dialysis-unit-manager-session-cap-counseling-flow-v2.webp', 'When a patient nears the 156-session cap: counsel early, never cut silently', 'When a patient nears the 156-session cap: counsel early, never cut silently.'),  # FIG-10B
    'uom10c': ('dialysis-unit-manager-privacy-need-to-know-v2.webp', 'Privacy on the dialysis floor: who needs to know what', 'Privacy on the dialysis floor: who needs to know what.'),  # FIG-10C
    'uom11a': ('dialysis-unit-manager-cost-break-even-v2.webp', 'Cost structure and break-even curve', 'Cost structure and break-even curve.'),  # FIG-11
    'uom11b': ('dialysis-unit-manager-cash-timing-waterfall-v2.webp', 'Why profitable units run short of cash: the timing gap', 'Why profitable units run short of cash: the timing gap.'),  # FIG-11B
    'uom11c': ('dialysis-unit-manager-budget-case-meeting-v2.webp', 'Defending safe staffing with numbers: the budget case meeting', 'Defending safe staffing with numbers: the budget case meeting.'),  # FIG-11C
    'uom12a': ('dialysis-unit-manager-typhoon-continuity-timeline-v2.webp', 'Typhoon continuity timeline: before, during and after', 'Typhoon continuity timeline: before, during and after.'),  # FIG-12
    'uom12b': ('dialysis-unit-manager-outage-decision-tree-v2.webp', 'During an outage: find the binding constraint, then act', 'During an outage: find the binding constraint, then act.'),  # FIG-12B
    'uom12c': ('dialysis-unit-manager-partner-unit-transfer-packet-v2.webp', 'Transferring a patient to a partner unit with the right packet', 'Transferring a patient to a partner unit with the right packet.'),  # FIG-12C
    'uom13a': ('dialysis-unit-manager-freestanding-ecosystem-v2.webp', 'Freestanding unit ecosystem of outside lifelines', 'Freestanding unit ecosystem of outside lifelines.'),  # FIG-13
    'uom13b': ('dialysis-unit-manager-healthcare-waste-flow-v2.webp', 'Healthcare waste: segregate, store, transport, document', 'Healthcare waste: segregate, store, transport, document.'),  # FIG-13B
    'uom13c': ('dialysis-unit-manager-transfer-drill-timed-v2.webp', 'Field case fixed: two hospitals, two ambulances, a timed drill', 'Field case fixed: two hospitals, two ambulances, a timed drill.'),  # FIG-13C
    'uom14a': ('dialysis-unit-manager-hospital-interfaces-ipass-v2.webp', 'Hospital interface map and the I-PASS dialysis handoff', 'Hospital interface map and the I-PASS dialysis handoff.'),  # FIG-14
    'uom14b': ('dialysis-unit-manager-hospital-demand-triage-v2.webp', 'Balancing inpatient and outpatient demand: a four-tier rule', 'Balancing inpatient and outpatient demand: a four-tier rule.'),  # FIG-14B
    'uom14c': ('dialysis-unit-manager-unprepared-inpatient-case-v2.webp', 'Field case: the inpatient who arrived unprepared — and the checklist that fixed it', 'Field case: the inpatient who arrived unprepared — and the checklist that fixed it.'),  # FIG-14C
    'uom15a': ('dialysis-unit-manager-wellbeing-safety-experience-loop-v2.webp', 'Staff wellbeing, safety and patient experience loop', 'Staff wellbeing, safety and patient experience loop.'),  # FIG-15
    'uom15b': ('dialysis-unit-manager-coaching-conversation-steps-v2.webp', 'A five-step coaching conversation', 'A five-step coaching conversation.'),  # FIG-15B
    'uom15c': ('dialysis-unit-manager-grievance-to-system-fix-v2.webp', "Field case: the 'difficult' patient and the system fix", "Field case: the 'difficult' patient and the system fix."),  # FIG-15C
    'uom16a': ('dialysis-unit-manager-session-to-cash-sod-v2.webp', 'Session-to-cash reconciliation and segregation of duties', 'Session-to-cash reconciliation and segregation of duties.'),  # FIG-16
    'uom16b': ('dialysis-unit-manager-three-way-match-imprest-v2.webp', 'Paying suppliers and handling petty cash the controlled way', 'Paying suppliers and handling petty cash the controlled way.'),  # FIG-16B
    'uom16c': ('dialysis-unit-manager-esa-variance-investigation-v2.webp', 'Field case: forty missing ESA vials — find the system gap, not a culprit', 'Field case: forty missing ESA vials — find the system gap, not a culprit.'),  # FIG-16C
    'uom17a': ('dialysis-unit-manager-roster-timecard-payroll-v2.webp', 'Roster-to-timecard-to-payroll flow with premium clock', 'Roster-to-timecard-to-payroll flow with premium clock.'),  # FIG-17
    'uom17b': ('dialysis-unit-manager-payroll-cutoff-review-v2.webp', 'Payroll cutoff review in six steps', 'Payroll cutoff review in six steps.'),  # FIG-17B
    'uom17c': ('dialysis-unit-manager-premium-pay-transparent-payslip-v2.webp', 'Premium pay made visible: one shift, every component', 'Premium pay made visible: one shift, every component.'),  # FIG-17C
    'uom18a': ('dialysis-unit-manager-contribution-remittance-trace-v2.webp', 'Contribution and remittance trace for one employee', 'Contribution and remittance trace for one employee.'),  # FIG-18
    'uom18b': ('dialysis-unit-manager-statutory-leaves-timeline-v2.webp', 'Statutory leaves at a glance (private sector)', 'Statutory leaves at a glance (private sector).'),  # FIG-18B
    'uom18c': ('dialysis-unit-manager-unposted-contributions-case-v2.webp', 'Field case: deducted but not posted — the mistyped ID', 'Field case: deducted but not posted — the mistyped ID.'),  # FIG-18C
    'uom19a': ('dialysis-unit-manager-integrated-readiness-dashboard-v2.webp', 'Integrated readiness dashboard for the capstone', 'Integrated readiness dashboard for the capstone.'),  # FIG-19
    'uom19b': ('dialysis-unit-manager-capstone-72-hour-injects-v2.webp', 'Capstone: 72 hours, six injects, one coordinated response', 'Capstone: 72 hours, six injects, one coordinated response.'),  # FIG-19B
    'uom19c': ('dialysis-unit-manager-portfolio-defense-panel-v2.webp', 'Defending the readiness portfolio', 'Defending the readiness portfolio.'),  # FIG-19C
}
