# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 15: Access infection and sepsis. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "In an emergency bay, a nurse draws blood cultures while a surgeon examines a red, swollen upper-arm graft on a patient receiving intravenous fluid.",
    "objectives": [
        "Explain why synthetic grafts and catheters are hard to cure of infection, using biofilm and tissue incorporation.",
        "Put sepsis care first, then decide what source control the access needs.",
        "State what the evidence shows for catheter lock solutions and unit-wide prevention bundles.",
        "Hand off antimicrobial treatment, culture review and dialysis access across transitions.",
    ],
    "big": """
{{plain:An infected graft is like a splinter in a wound. You can give antibiotics for weeks, but while the splinter stays, the infection keeps coming back.}}
<p>The picture has a limit. A splinter is inert; a graft or catheter is coated within days by biofilm, a matrix in which bacteria grow slowly and are shielded from antibiotics and white cells. A living fistula can often clear infection with antibiotics because its wall has a blood supply and immune cells. Synthetic material cannot. The organism, the extent of infection and the patient&rsquo;s condition decide whether the foreign material must go.</p>
{{cards:Key terms for this module|Sepsis::Life-threatening organ dysfunction caused by the body&rsquo;s response to infection.|Source control::Removing or draining the source of infection.|Catheter-related bloodstream infection (CRBSI)::Bacteremia attributed to a dialysis catheter.|Lock solution::A solution left in catheter lumens between sessions to prevent clotting or infection.|Antimicrobial stewardship::Choosing, dosing and reviewing antibiotics to treat well and limit resistance.}}
<p>A patient with an infected access and low blood pressure is a sepsis patient first. Your work is to make sure sepsis care starts now, then to decide with the team whether the access stays, is revised, or is removed, and who owns the antibiotics.</p>
""",
    "case": {"title": "The draining graft", "html": """
<p>Mrs. Aurora Fernandez, 64, has a left forearm loop graft placed 14 months ago. For a week the skin over the arterial limb has been red and tender, and two days ago it began draining pus. The dialysis unit prescribed oral antibiotics, but the prescription was never filled. She arrives at your hospital&rsquo;s emergency department febrile at 39.0 &deg;C, with a blood pressure of 84/52 mm Hg and a heart rate of 118 per minute. The graft still has a thrill. The emergency resident asks whether this can wait for your Thursday wound clinic.</p>
""", "questions": [
        "What happens in the first hour?",
        "Will the graft stay?",
        "What must be handed over when she leaves the emergency department?"]},
    "sections": [
        ("biology", "Why it is hard to cure", "Why access infections persist", """
<p>Bacteria from the skin reach an access through needle sites, the incision or, for catheters, the hub and the exit site. On synthetic surfaces they form biofilm within days. Antibiotic concentrations that kill free-floating bacteria often fail inside biofilm, and the bacteria shed into the blood intermittently. This is why a catheter infection with the same organism recurs after treatment, and why an infected graft, especially with an exposed segment, an abscess, or bleeding, usually needs removal of the infected material.</p>
{{fig:vs15_a}}
<p>Fistulas behave differently. Their walls are living tissue, perfused and defended, and localized fistula infections often respond to antibiotics, though infection at an anastomosis or with bleeding is dangerous in any access. The UK Kidney Association (UKKA) 2025 guideline suggests systemic antibiotics without catheter replacement for exit-site infection without bacteremia (statement 6.4, grade 1D), antibiotics without replacement as the initial strategy for uncomplicated coagulase-negative staphylococcal bacteremia (6.5, grade 2C), and favoring catheter replacement when bacteremia is recurrent, severe, or due to <em>Staphylococcus aureus</em> (6.6, grade 2C).[[vs_ukka]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Access</th><th>Why it matters</th><th>Usual source control</th></tr></thead>
<tbody>
<tr><td>Catheter</td><td>Biofilm on the surface</td><td>Exchange or removal for severe, recurrent or <em>S. aureus</em> infection</td></tr>
<tr><td>Graft, localized</td><td>Infected segment of synthetic material</td><td>Partial excision and bypass of the infected segment</td></tr>
<tr><td>Graft, extensive, anastomotic, or with sepsis</td><td>Material cannot be sterilized</td><td>Total or near-total removal</td></tr>
<tr><td>Fistula</td><td>Living wall</td><td>Often antibiotics; surgery for abscess, bleeding or anastomotic involvement</td></tr>
</tbody></table></div>
"""),
        ("sepsis", "Sepsis first", "Sepsis first, then the access", """
<p>Hypotension, tachycardia and fever with an infected access are sepsis until proven otherwise. Start the institution&rsquo;s sepsis pathway: resuscitate, take blood cultures (and wound cultures) without delaying treatment, and give empiric antibiotics chosen from the local antibiogram, dosed for dialysis. The question of preserving the access waits until the patient is stable.</p>
{{fig:vs15_b}}
<p>Then decide on source control with the nephrologist and, where available, infectious disease colleagues. An unstable patient with an infected graft generally needs the infected material removed urgently. Plan the next dialysis route before you take the graft out. Make sure one named clinician reviews culture results, adjusts antibiotics and sets the duration, and that the plan travels with the patient to the ward and back to the dialysis unit. The Centers for Disease Control and Prevention (CDC) stewardship core elements stress training in sepsis recognition, appropriate dosing, microbiology review and communication at transitions.[[vs_cdc_stew]]</p>
{{flow:Infected access with sepsis|Recognize::Fever, hypotension, tachycardia, pus, a red tender access.|Resuscitate and culture::Sepsis pathway; blood and wound cultures without delay.|Treat::Empiric antibiotics from the local antibiogram, dosed for dialysis.|Source control::Surgical review now; remove infected synthetic material when indicated.|Bridge::Temporary dialysis access chosen to protect future sites.|Hand off::Named owner for cultures, antibiotic duration and follow-up.}}
{{call:Do not debate access preservation while a septic patient is hypotensive. Start sepsis care and call the surgeon for source-control review now.}}
"""),
        ("prevention", "Prevention", "Preventing access infection: what the evidence shows", """
<p>Unit-wide practice matters. In a CDC collaborative of outpatient hemodialysis facilities implementing core interventions (surveillance, hand hygiene and catheter-care audits, chlorhexidine skin antisepsis, staff education), modeled access-related bloodstream infection rates fell 54% at the start of the intervention period.[[vs_patel2013]] There was no control group, so part of the improvement may reflect other changes, but the effect was large and sustained. The CDC core interventions remain the reference bundle.[[vs_cdc_core]]</p>
<p>For catheters, the LOCK IT-100 trial randomized 795 patients to a taurolidine-heparin lock or heparin alone. Catheter-related bloodstream infection occurred at 0.13 versus 0.46 per 1,000 catheter-days (hazard ratio 0.29), with similar safety; 9 versus 32 patients had an infection.[[vs_agarwal2023]] Whether the product is registered and available in the Philippines needs checking before it enters a local protocol. Check product compatibility before applying any agent to a catheter.</p>
{{key:The surest prevention is fewer catheter-days. Every catheter needs an exit date (Module 8).}}
"""),
    ],
    "debrief": [
        "<p><strong>The first hour.</strong> This is septic shock, not a wound-clinic problem. Start the sepsis pathway now: resuscitation, blood and wound cultures without delay, empiric antibiotics covering <em>Staphylococcus aureus</em> including resistant strains per the local antibiogram, dosed for dialysis. Call the nephrologist about dialysis and the surgeon about source control.</p>",
        "<p><strong>The graft.</strong> Once she is stabilized, an infected synthetic graft with pus and sepsis generally needs the infected material removed; extent determines whether partial excision is possible or the whole graft must go. Plan a temporary dialysis catheter that protects her future sites, ideally a right internal jugular line placed when blood cultures are clearing, as the team judges.</p>",
        "<p><strong>The handoff.</strong> Name who reviews cultures and sets the antibiotic course, how antibiotics will be given at dialysis, when she is reviewed, and what her new access plan is. Report the missed prescription as a system failure so the unit can fix how outpatient antibiotics are started.</p>",
    ],
    "skills": {"title": "Sepsis recognition and source-control handoff",
               "intro": "Emergency station simulation or supervised emergency case.",
               "items": [("Recognizes instability and activates sepsis care before discussing the access", True),
                         ("Ensures cultures are taken without delaying antibiotics", False),
                         ("Arranges urgent source-control review", True),
                         ("Plans a bridge dialysis route that protects future sites", False),
                         ("Names the owner of culture review, antibiotic duration and follow-up", True)],
               "placement": "Emergency station or on-call"},
    "quiz": [
        ("A patient with a draining graft is hypotensive. What is the best response?",
         ["A routine wound appointment", "Delay treatment until final cultures return",
          "Emergency sepsis care, prompt antibiotics, and surgical source-control review", "Oral antibiotics and discharge"],
         2, "Systemic instability needs urgent coordinated care."),
        ("What should happen when microbiology results become available?",
         ["A named clinician reviews and adjusts therapy as appropriate", "No review if antibiotics were already started",
          "Automatic continuation indefinitely", "The patient decides"],
         0, "Stewardship includes reassessment, dialysis dosing and effective transitions."),
        ("Why is an infected synthetic graft often removed rather than treated with antibiotics alone?",
         ["Antibiotics cannot be given at dialysis", "Biofilm on synthetic material shields bacteria from antibiotics and host defenses",
          "Grafts never become infected", "Removal is always easier"],
         1, "Synthetic material cannot clear infection as living tissue can."),
        ("In LOCK IT-100, what were the catheter-related bloodstream infection (CRBSI) rates with taurolidine-heparin versus heparin?",
         ["0.13 versus 0.46 per 1,000 catheter-days", "1.3 versus 4.6 per 100 patient-days", "No difference", "0.46 versus 0.13, favoring heparin"],
         0, "Hazard ratio 0.29; local availability must be checked."),
        ("UKKA 2025 suggests favoring catheter replacement for bacteremia with which features?",
         ["Any coagulase-negative staphylococcus", "Recurrent, severe, or due to Staphylococcus aureus", "Exit-site redness alone", "Fever without cultures"],
         1, "Statement 6.6, grade 2C."),
    ],
    "terms": [("Antibiogram", "A local summary of which antibiotics work against which organisms."),
              ("Partial excision", "Removing only the infected segment of a graft and bypassing it.")],
    "readings": [("dialysis-access-infection.html", "When the access gets infected, for patients and clinicians."),
                 ("tropical-infection-aki.html", "Infection and the kidney in the Philippine setting.")],
    "calcs": ["calc-qsofa-sofa.html", "calc-sirs-sepsis.html", "calc-access-infection-rate.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
