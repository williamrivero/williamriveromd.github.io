# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 12: Infection prevention and safety investment. Written for this course from published sources."""

MODULE = {
    "image_alt": "Gloved hands disinfecting a catheter connector with an alcohol swab, beside a clean dressing and a sharps container.",
    "objectives": [
        "Explain why dialysis patients are at high risk of bloodstream infection and which access carries the most risk.",
        "Describe the core interventions and what the owner must fund to keep them running.",
        "Explain the owner&rsquo;s role in preventing bloodborne virus transmission.",
        "Govern an outbreak: resources and reporting, while clinicians lead.",
    ],
    "big": """
{{plain:Every dialysis session opens a door into the bloodstream, three times a week, for years. Infection prevention is the set of locks on that door. Each lock is cheap; a missing one can be fatal.}}
<p>The picture has a limit. Locks stay locked. Infection controls work only when people use them every time, which takes training, supplies, time, and audits. That is why infection prevention is an owner&rsquo;s budget line, not only a nurse&rsquo;s habit.</p>
{{cards:Key terms for this module|Bloodstream infection (BSI)::Infection in the blood, often from the dialysis access.|Catheter-related bloodstream infection (CRBSI)::A bloodstream infection that started at a dialysis catheter.|Core interventions::The Centers for Disease Control and Prevention (CDC) package of practices that reduce dialysis bloodstream infections.|Bloodborne viruses::Viruses spread through blood, such as hepatitis B virus (HBV) and hepatitis C virus (HCV).|Cluster::More infections than expected in a short time or place.}}
<p>Your work is to fund the locks, ask for the rates, and support the clinical head without delay when something goes wrong.</p>
""",
    "case": {"title": "Two infections in a month", "html": """
<p>At a 20-station unit in Quezon City, two patients with tunneled catheters are admitted with bloodstream infections in the same month. The clinical head, Dr. Ramon Velasco, wants a hand-hygiene and catheter-care audit, an extra infection-control nurse shift for a month, and a supply of chlorhexidine dressings the unit stopped buying to save money. The total is 85,000 pesos.</p>
""", "questions": ["Is two infections a signal?", "What does the owner approve, and how fast?", "Who reports, and to whom?"]},
    "sections": [
        ("risk", "The risk", "Why dialysis patients get bloodstream infections", """
{{fig:duo12a}}
<p>People on dialysis, the sickest group among those with chronic kidney disease (CKD), face a risk of bloodstream infection with <em>Staphylococcus aureus</em> about 100 times that of other adults in the United States, according to CDC surveillance data.[[dch_rha2023]] The access is the main door. A catheter in a large vein carries the highest risk; a fistula made from the patient&rsquo;s own vessels carries the lowest. Philippine data describe the same pattern: a recent study set out how often catheter-related bloodstream infections occur in local dialysis patients and which bacteria cause them.[[dch_pasilan2024]]</p>
<p>That is why getting patients off catheters and onto fistulas or grafts is one of the most important infection controls a unit has, and why it depends on the access-surgeon agreement from Module 8.</p>
{{key:Every catheter-day removed is risk removed. Track the plan for every catheter.}}
"""),
        ("core", "Core interventions", "The core interventions and what they cost", """
<p>The CDC core interventions include monthly surveillance of bloodstream infections, hand hygiene audits, catheter and vascular access care audits, staff competency, patient education, chlorhexidine skin antisepsis, catheter hub disinfection, and efforts to reduce catheter use.[[dch_cdc_core]] In a CDC collaborative, bloodstream infection rates fell after facilities adopted the package; the study compared before and after without a separate control group.[[dch_patel2013]][[uom_yi2016]]</p>
<p>Each intervention needs something an owner provides: time for audits, enough staff to do the steps properly, and supplies that are never cut to save money. When a unit stops buying a supply that the infection protocol requires, the saving is paid by patients.</p>
{{key:Fund the time, the staff, and the supplies the infection protocol requires. Ask for the rate per 1,000 catheter-days every month.}}
"""),
        ("viruses", "Bloodborne viruses", "Bloodborne viruses", """
<p>Hepatitis B spreads easily in dialysis units through contaminated surfaces, equipment, and hands, and outbreaks have followed lapses in basic practice.[[uom_cdc1996]][[uom_cdc2001]] Prevention rests on testing patients regularly, vaccinating those not immune, dialyzing patients with hepatitis B in a separate area with dedicated machines and staff, and cleaning between every patient. Hepatitis C prevention depends on strict infection control and testing; guidelines advise against isolating patients with hepatitis C but require careful practice.[[uom_kdigo_hcv2018]]</p>
<p>These controls need space, machines, and staff time, which are owner decisions. The decision about who is isolated is not.</p>
{{key:Fund the isolation area, the dedicated machines, and the vaccines. Leave the decisions about individual patients to the clinical head.}}
"""),
        ("outbreak", "Outbreaks", "When there is a cluster", """
{{fig:duo12b}}
<p>A cluster is more infections than expected. Two in a month may or may not be a signal; the clinical head decides that, using the unit&rsquo;s usual rate and its denominator. The owner&rsquo;s part is to release resources without delay, support honest reporting to the authorities as required, and ask for the rate to be followed for months afterward to show the fix worked.</p>
{{stop:Never delay or discourage reporting of an infection cluster to protect the unit&rsquo;s reputation.}}
{{key:In an outbreak, the clinical head leads and the owner pays, quickly.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is it a signal?</strong> Possibly. Ask for the unit&rsquo;s usual rate per 1,000 catheter-days and plot it. Either way, Dr. Velasco&rsquo;s request is reasonable and cheap compared with one admission or a death.</p>
<p><strong>What to approve.</strong> All 85,000 pesos, today. Restart the chlorhexidine supply permanently, since stopping it was a saving paid by patients.</p>
<p><strong>Reporting.</strong> The clinical head reports as the rules require. The owner makes sure no one is discouraged from reporting and asks for the rate monthly for at least three months.</p>
"""],
    "skills": {"title": "Infection prevention resource plan and outbreak governance checklist",
               "intro": "Build a resource plan for the core interventions and an owner&rsquo;s outbreak checklist.",
               "items": [("Explains why catheters carry the highest infection risk.", False),
                         ("Lists each core intervention with the resource it needs.", False),
                         ("Restores any supply the infection protocol requires that was cut to save money.", True),
                         ("Releases outbreak resources without delay on the clinical head&rsquo;s request.", True),
                         ("Supports reporting as required and does not delay it.", True),
                         ("Asks for monthly infection rates with denominators.", False)],
               "placement": "Ask for your unit&rsquo;s infection rate per 1,000 catheter-days for the last twelve months."},
    "quiz": [
        ("Which vascular access carries the highest bloodstream infection risk?",
         ["Fistula", "Graft", "Central venous catheter", "Peritoneal catheter"],
         2, "Catheters carry the highest risk."),
        ("According to CDC data, how does the risk of <em>S. aureus</em> bloodstream infection in dialysis patients compare with other adults?",
         ["About the same", "About 2 times", "About 100 times", "Lower"],
         2, "CDC surveillance put the risk at about 100 times higher."),
        ("A supply required by the infection protocol was cut to save money. What should the owner do?",
         ["Keep the saving", "Restore it", "Ask patients to buy it", "Replace it with a cheaper unapproved product"],
         1, "Savings on required infection supplies are paid by patients."),
        ("How should a unit report bloodstream infections internally?",
         ["As a raw count only", "As a rate per 1,000 catheter-days, monthly", "Once a year", "Only when a patient dies"],
         1, "A rate with a denominator shows whether risk is changing."),
        ("Who decides whether a patient with hepatitis B dialyzes in the isolation area?",
         ["The owner", "The clinical team under the infection rules", "The billing officer", "The patient&rsquo;s employer"],
         1, "Individual isolation decisions are clinical; the owner funds the area and machines."),
        ("What did the CDC collaborative on the core interventions report?",
         ["No change", "Bloodstream infection rates fell after adoption, in a before-and-after design", "Rates rose", "It was a randomized trial"],
         1, "The design had no separate control group, so it suggests rather than proves benefit."),
    ],
    "terms": [("Chlorhexidine", "An antiseptic used on skin and catheter exit sites."),
              ("Catheter-day", "One patient with a catheter for one day; the denominator for catheter infection rates.")],
    "readings": [("dialysis-access-infection.html", "How dialysis access infections happen and how they are prevented."),
                 ("viral-infections-vaccinations-ckd.html", "Vaccines and viral infections in kidney disease.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html#c11", "calc-dialysis-clinical-head-toolkit.html#c3"],
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
