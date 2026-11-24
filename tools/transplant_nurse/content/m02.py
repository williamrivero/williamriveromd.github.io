# -*- coding: utf-8 -*-
MODULE = {
    "sub": "What the evaluation is looking for and why, how blood groups, HLA antibodies and crossmatches decide which kidney a body will accept, why a single transfusion can change a candidate's chances, and how to run a readiness tracker that keeps a candidate truly ready.",
    "desc": "Transplant Nurse Module 2: recipient evaluation domains (cardiac, cancer, infection, frailty, psychosocial), ABO and HLA compatibility, cPRA, donor-specific antibodies and crossmatch, sensitizing events, vaccines before transplant, and readiness tracking for Philippine registered nurses.",
    "keywords": "kidney transplant evaluation nursing, HLA antibodies cPRA explained, crossmatch nurse, sensitization transfusion transplant, frailty transplant candidate, waiting list readiness",
    "image_alt": "A transplant coordinator nurse reviewing a color-coded readiness checklist on a tablet with an older Filipino candidate and his daughter.",
    "objectives": [
        "Explain the purpose of each evaluation domain in terms of what could make surgery or immunosuppression unsafe.",
        "Explain ABO compatibility, HLA typing, cPRA, donor-specific antibodies and the crossmatch in plain language.",
        "Recognize sensitizing events and report them so that antibody testing stays current.",
        "Maintain a readiness tracker with dated results, dispositions and named owners.",
        "Respond to missed tests and loss of contact as barriers to solve rather than as nonadherence to punish.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "Two questions every evaluation asks",
         "html": """
<p>Every test in a transplant evaluation answers one of two questions. <em>Will this person survive the operation and the first year of immunosuppression?</em> And <em>will this person's immune system accept this particular kidney?</em> The first question is answered by the medical work-up: heart, cancer, infection, frailty, mind and means. The second is answered by the immunology laboratory: blood group, tissue type and antibodies.</p>
<p>Think of the immune system as a security guard holding a list of faces it has been taught to attack. Most people's list is short. Every pregnancy, every blood transfusion and every previous transplant shows the guard new faces, and the list grows. A candidate whose list matches most of the population is "highly sensitized" and will wait far longer for a kidney that matches none of the faces. The analogy breaks in one place: the list is written in antibodies circulating in the blood, so it can be read with a blood test, and it can change silently after a single transfusion.</p>
"""},
        {"id": "workup", "nav": "Evaluation", "tag": "Physiology", "h2": "What the medical evaluation is looking for",
         "html": """
<p>The KDIGO candidate guideline organizes evaluation around risks that surgery or lifelong immunosuppression would make dangerous.[[txcand2020]] Knowing the reason behind each item helps you explain it to patients and spot what is overdue.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>The physiologic worry</th><th>Nursing focus</th></tr></thead>
<tbody>
<tr><td>Cardiovascular</td><td>Coronary disease is common and often silent in kidney failure; surgery and fluid shifts unmask it.</td><td>Track stress test or echocardiogram dates; report new chest pain or dyspnea.</td></tr>
<tr><td>Cancer</td><td>Immunosuppression weakens immune surveillance, so an untreated cancer can grow faster.</td><td>Age- and sex-appropriate screening dates; report new weight loss or bleeding.</td></tr>
<tr><td>Infection</td><td>Latent infections (hepatitis B and C, HIV, tuberculosis, Strongyloides in endemic areas) can reactivate under immunosuppression.</td><td>Serology dates; latent tuberculosis results and treatment start; dental clearance.</td></tr>
<tr><td>Vascular and surgical</td><td>The kidney is joined to the iliac vessels and bladder; heavy calcification or bladder problems complicate surgery.</td><td>Imaging dates; prior abdominal surgery; urologic history.</td></tr>
<tr><td>Frailty and function</td><td>Low physiologic reserve predicts complications and death.</td><td>Mobility, falls, weight; refer for prehabilitation.</td></tr>
<tr><td>Psychosocial and means</td><td>Lifelong medicines, labs and visits require support, understanding and money.</td><td>Social work review; coverage; who will help after discharge.</td></tr>
</tbody></table></div>
<p><strong>Tuberculosis deserves particular attention in the Philippines.</strong> The burden of latent infection is high, and reactivation under immunosuppression can be severe and atypical. Guidance from the American Society of Transplantation recommends screening every candidate for latent tuberculosis and treating latent infection, ideally starting before transplant.[[subramanian2019]] Track the result, the decision and the start date.</p>
<p><strong>Frailty predicts outcomes independently of age.</strong> In a prospective cohort of 537 recipients, five-year survival was 91.5 percent in nonfrail, 86.0 percent in intermediately frail and 77.5 percent in frail recipients, and frailty was independently associated with about twice the risk of death.[[mcadams2015]] This is observational evidence, so it identifies risk rather than proving that improving frailty improves survival. It is still a reason to measure frailty and to refer for prehabilitation while the candidate waits.</p>
<p><strong>Vaccinate before, not after.</strong> Vaccines work better before immunosuppression, and live vaccines are generally avoided after transplant. Guidance recommends completing inactivated vaccines at least two weeks and live vaccines at least four weeks before transplant whenever possible.[[danziger2019]] A candidate on the active list should have an up-to-date vaccine record.</p>
"""},
        {"id": "immunology", "nav": "Compatibility", "tag": "Physiology", "h2": "Blood groups, HLA, antibodies and the crossmatch",
         "html": """
<p><strong>ABO blood group.</strong> The same A and B sugar antigens that decide transfusion compatibility also coat the inner lining of the kidney's blood vessels. A recipient's natural anti-A or anti-B antibodies would attack an incompatible kidney within minutes, so ABO compatibility follows transfusion rules. Some centers perform ABO-incompatible transplants after removing antibodies, a specialized protocol.</p>
<p><strong>HLA typing.</strong> Human leukocyte antigens (HLA) are the proteins every cell uses to display fragments of itself to T lymphocytes. They are inherited, highly variable, and are the main targets of rejection. Typing tells the laboratory which HLA a candidate and a donor carry.</p>
<p><strong>Antibodies and cPRA.</strong> Sensitizing events (pregnancy, transfusion, a prior transplant) can create antibodies against HLA the candidate does not have. The laboratory lists antigens against which the candidate has clinically significant antibodies. The calculated panel-reactive antibody (cPRA) translates that list into a percentage: the share of donors in a reference population who carry at least one of those antigens. A cPRA of 95 percent means roughly 95 of every 100 donors would be unsuitable on antibody grounds.</p>
<p><strong>Donor-specific antibody (DSA).</strong> cPRA describes breadth of sensitization against a population. A DSA is an antibody directed against an HLA carried by <em>a particular donor</em>. A candidate with a cPRA of 20 percent can still have a strong DSA against her husband's kidney; a candidate with 90 percent may have none against a specific offer.</p>
<p><strong>Crossmatch.</strong> The crossmatch tests the recipient's serum against the donor's cells (or, virtually, the antibody list against the donor's typing). A strongly positive crossmatch from preformed DSA can cause hyperacute or early antibody-mediated rejection, which is why the test must use the candidate's <em>current</em> serum.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>cPRA tells you how hard it will be to find a kidney. DSA and crossmatch tell you whether <em>this</em> kidney is safe. The laboratory and transplant team interpret both; the nurse makes sure the sample is the right patient, the right date, and that new sensitizing events are reported.</div>
"""},
        {"id": "sensitizing", "nav": "Sensitizing events", "tag": "Practice", "h2": "One transfusion can change everything",
         "html": """
<p>A wait-listed candidate who receives a blood transfusion during an unrelated admission may develop new HLA antibodies within weeks. If the laboratory's stored serum predates the transfusion, a future crossmatch could miss a dangerous antibody. Programs therefore ask to be notified of transfusions, pregnancies, miscarriages and infections, and they keep serum samples current on a regular schedule.</p>
<ul>
<li>Ask every listed candidate at every contact: any admission, transfusion, pregnancy or surgery since we last spoke?</li>
<li>Record the date, the facility and the number of units if known, and request the records.</li>
<li>Notify the coordinator and, per local procedure, the histocompatibility laboratory, and document who will arrange the repeat sample.</li>
<li>Avoid unnecessary transfusion in candidates where you have influence: flag the patient's status to the treating team, who weigh anemia treatment options.</li>
</ul>
<div class="tc-stop"><span class="tc-lab">Stop and report</span>Any discrepancy in a sample label, a result that seems to belong to another patient, or a crossmatch request with a mismatched identifier must stop the workflow until it is verified through the laboratory's procedure.</div>
"""},
        {"id": "tracker", "nav": "Readiness tracker", "tag": "Workflow", "h2": "Keeping a candidate truly ready",
         "html": """
<p>A candidate is "ready" only if every required item is current on the day a kidney becomes available. Results expire: a cardiac test from three years ago, an outdated serum sample, a lapsed cancer screen. A good tracker lists, for each item, the date done, the result disposition (reviewed and acceptable, needs action, pending), the expiry or repeat date, and the owner of the next step.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Date</th><th>Disposition</th><th>Repeat due</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Serum sample for antibody screening</td><td>12 Jan</td><td>Reviewed</td><td>Per laboratory schedule, or after any sensitizing event</td><td>Coordinator</td></tr>
<tr><td>Cardiac assessment</td><td>3 Feb</td><td>Cardiology cleared</td><td>Per program policy</td><td>Nephrologist</td></tr>
<tr><td>Latent tuberculosis test</td><td>20 Feb</td><td>Positive, treatment started 1 Mar</td><td>Completion date</td><td>Infectious disease</td></tr>
<tr><td>Cervical cancer screen</td><td>pending</td><td>Overdue</td><td>Book this month</td><td>Clinic RN</td></tr>
</tbody></table></div>
<p><strong>Missed tests are a signal.</strong> A candidate who misses two appointments may have run out of money for transport, lost a job, become ill, or misunderstood. Contact them through the approved route, ask what happened, document the barrier, and offer a path back: bundled visits, local testing, social work, or a benefits review. Labeling a candidate "nonadherent" without exploring the reason closes the door on people who most need help.</p>
<p><strong>Report changes that affect safety.</strong> New infection, hospitalization, a new cancer concern, major weight change, or loss of contact for weeks may require the team to place a candidate on hold. You report; the program decides the status and communicates it.</p>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Certainty", "h2": "What is established, and what is not",
         "html": """
<ul>
<li><strong>Established physiology:</strong> preformed antibodies against ABO or donor HLA can cause immediate or early antibody-mediated graft injury; this is why compatibility testing exists.</li>
<li><strong>Guideline-based:</strong> structured evaluation across cardiac, cancer, infection, frailty and psychosocial domains is KDIGO practice.[[txcand2020]] Pre-transplant latent tuberculosis screening and vaccination are recommended by transplant infectious-disease guidance.[[subramanian2019]][[danziger2019]]</li>
<li><strong>Association, not proven causation:</strong> frailty predicts mortality after transplant.[[mcadams2015]] Whether prehabilitation reverses that risk is still being studied.</li>
</ul>
"""},
    ],
    "case": {
        "title": "The transfusion nobody mentioned",
        "html": """
<p>Aling Merly, 58, has been on the deceased-donor waiting list for two years. Her cPRA was 35 percent at listing. At her quarterly call she mentions, almost in passing, that she was admitted to a provincial hospital last month for heavy uterine bleeding and "received two bags of blood." The program's last serum sample on file is from four months ago. She also says she missed her mammogram because her son's motorcycle broke down.</p>
""",
        "acte": {
            "Assess": "Date and place of admission, number of units, current symptoms, ongoing bleeding, hemoglobin if known, and whether the bleeding cause has been evaluated (also a cancer-screening issue).",
            "Communicate": "Notify the coordinator and, per procedure, the histocompatibility laboratory that a sensitizing event occurred after the last stored sample. Request the provincial records. Document who will arrange the repeat sample and by when.",
            "Teach": "Explain why a transfusion can create new antibodies and why the laboratory needs a fresh sample to keep her safe when a kidney is offered. Ask her to report any future admission or transfusion promptly.",
            "Escalate": "The new uterine bleeding and the missed mammogram are both cancer-screening concerns; route them to the nephrologist for work-up and possible temporary hold. Offer social work help with transport.",
        },
        "task": "Write the contact note: event, dates, notifications made, owner of the repeat sample, owner of the gynecologic and breast follow-up, and who will tell her about any change in list status.",
    },
    "second_round": ("One laboratory result in her file has a different middle name, and her cervical screening is also overdue.", "A tracker with the suspect result flagged as invalid until verified, the verification route, and separate owners for each follow-up item."),
    "evidence_out": "Readiness tracker with dated results, dispositions and named owners.",
    "critical": "Independently clearing compatibility or changing listing status.",
    "reflect": "Which items on your unit's candidate checklist expire, and does anyone track their expiry dates?",
    "practice": {
        "intro": "Use synthetic or de-identified examples only.",
        "items": [
            "Build a readiness tracker for a synthetic candidate with at least eight dated items and owners.",
            "Explain cPRA, DSA and crossmatch to a peer in plain language without using the acronyms.",
            "Walk through your laboratory's sample-labeling and verification procedure with the histocompatibility staff.",
            "Practice a scripted check-in call that asks about admissions, transfusions and pregnancies.",
            "Review one candidate's vaccine record against the program's pre-transplant schedule.",
        ],
    },
    "readings": [
        ("highly-sensitized-kidney-transplant-candidates-clinician.html", "Deeper dive on sensitization and access for highly sensitized candidates."),
        ("transplant-prehabilitation.html", "Prehabilitation for frail candidates."),
        ("viral-infections-vaccinations-ckd.html", "Vaccines and viral screening in kidney disease."),
    ],
    "calcs": ["calc-frailty-assessment.html", "calc-epts.html"],
    "terms": [
        ("Sensitization", "Development of antibodies against foreign HLA after pregnancy, transfusion or a previous transplant."),
        ("Crossmatch", "A test of the recipient's serum against a specific donor's cells or HLA type to detect donor-specific antibodies."),
        ("Hyperacute rejection", "Immediate graft destruction caused by preformed antibodies against donor antigens."),
        ("Prehabilitation", "Structured exercise and nutrition before surgery to build physiologic reserve."),
    ],
    "quiz": [
        {"stem": "Which statement best distinguishes cPRA from a donor-specific antibody (DSA)?",
         "options": [("cPRA estimates the share of donors a candidate is sensitized against; DSA is an antibody against a particular donor's HLA.", True, "cPRA describes breadth; DSA and crossmatch address a specific donor."),
                     ("They are two names for the same test.", False, "They answer different questions."),
                     ("cPRA identifies the antibody that will reject a particular kidney.", False, "Only donor-specific testing does that."),
                     ("DSA measures blood group compatibility.", False, "ABO is a separate system.")],
         "sources": ["txcand2020"]},
        {"stem": "A listed candidate received two units of blood at another hospital last month. What is the priority nursing action?",
         "options": [("Report the sensitizing event to the coordinator and laboratory pathway and document who will arrange a repeat serum sample.", True, "New antibodies may form; the stored sample may no longer be current."),
                     ("No action; transfusions do not affect transplant.", False, "Transfusion is a recognized sensitizing event."),
                     ("Remove her from the list yourself.", False, "Listing status is a program decision."),
                     ("Advise her to refuse all future transfusions.", False, "Transfusion decisions belong to the treating team weighing her safety.")],
         "sources": ["txcand2020"]},
        {"stem": "Why must the crossmatch use the candidate's current serum?",
         "options": [("Antibodies can appear after recent sensitizing events, and an old sample could miss them.", True, "Current serum reflects current antibodies."),
                     ("Old serum samples spoil within a day.", False, "Serum is stored frozen for antibody testing."),
                     ("PhilHealth requires it.", False, "The reason is immunologic safety."),
                     ("It makes the test cheaper.", False, "Not the reason.")],
         "sources": ["txcand2020"]},
        {"stem": "Why does a candidate's cancer screening matter before transplant?",
         "options": [("Immunosuppression weakens immune surveillance and may allow an undetected cancer to progress.", True, "This is the physiologic rationale for cancer screening."),
                     ("Cancer screening is needed only for living donors.", False, "Recipients need it too."),
                     ("It is an administrative formality.", False, "It addresses real risk."),
                     ("Cancer cells reject the kidney.", False, "Not the mechanism.")],
         "sources": ["txcand2020", "engels2011"]},
        {"stem": "What do transplant infectious-disease guidelines recommend about latent tuberculosis in candidates?",
         "options": [("Screen all candidates and treat latent infection, ideally starting before transplant.", True, "Reactivation under immunosuppression can be severe."),
                     ("Screen only candidates with cough.", False, "Latent infection is asymptomatic by definition."),
                     ("Defer all screening until after transplant.", False, "Pre-transplant screening allows treatment before immunosuppression."),
                     ("Tuberculosis is not relevant in transplant.", False, "It is a major concern, especially in high-burden countries.")],
         "sources": ["subramanian2019"]},
        {"stem": "In a prospective cohort, how was frailty at transplant related to survival?",
         "options": [("Frail recipients had lower five-year survival and about twice the adjusted risk of death.", True, "Five-year survival was 77.5 percent in frail versus 91.5 percent in nonfrail recipients."),
                     ("Frailty had no relationship with survival.", False, "The association was independent of age."),
                     ("Frailty only mattered in recipients older than 80.", False, "It was associated with risk regardless of age."),
                     ("Frail recipients lived longer.", False, "The opposite was found.")],
         "sources": ["mcadams2015"]},
        {"stem": "What timing is recommended for vaccines before transplant when possible?",
         "options": [("Inactivated vaccines at least 2 weeks and live vaccines at least 4 weeks before transplant.", True, "Vaccines work better before immunosuppression; live vaccines are generally avoided afterward."),
                     ("All vaccines should wait until one year after transplant.", False, "Pre-transplant vaccination is preferred."),
                     ("Live vaccines are preferred immediately after transplant.", False, "Live vaccines are generally avoided after transplant."),
                     ("Vaccines are not needed for transplant candidates.", False, "Up-to-date vaccination is part of readiness.")],
         "sources": ["danziger2019"]},
        {"stem": "A candidate has missed two scheduled tests. What is the most appropriate first action?",
         "options": [("Contact her through the approved route, explore barriers, document, and coordinate completion.", True, "Missed tests often signal solvable barriers."),
                     ("Document her as nonadherent and notify the committee to decline her.", False, "Premature and outside nursing scope."),
                     ("Wait for her next quarterly call.", False, "Delays readiness and leaves the barrier unsolved."),
                     ("Cancel her remaining tests.", False, "Unhelpful and unauthorized.")],
         "sources": []},
        {"stem": "A laboratory result in a candidate's file shows a different middle name. What should happen?",
         "options": [("Flag it as unverified, exclude it from decisions, and verify identity through the laboratory's procedure.", True, "Identity discrepancies stop the workflow until resolved."),
                     ("Correct the name by hand.", False, "Altering a result record is unsafe and improper."),
                     ("Use it anyway; middle names are often wrong.", False, "A wrong-patient result could cause serious harm."),
                     ("Delete it from the chart.", False, "Records are corrected through procedure, not deleted.")],
         "sources": []},
        {"stem": "Why are ABO-incompatible kidneys normally avoided?",
         "options": [("Natural anti-A or anti-B antibodies can attack antigens on the graft's blood vessels.", True, "A and B antigens are expressed on vascular endothelium."),
                     ("Blood type determines kidney size.", False, "Not related."),
                     ("ABO incompatibility only matters for transfusions.", False, "It matters for kidneys too."),
                     ("They are never possible under any protocol.", False, "Specialized antibody-removal protocols exist at some centers.")],
         "sources": []},
        {"stem": "Which event is NOT typically a sensitizing event for HLA antibodies?",
         "options": [("A routine eye examination.", True, "No exposure to foreign HLA occurs."),
                     ("Pregnancy.", False, "Exposure to paternal HLA can sensitize."),
                     ("Blood transfusion.", False, "Transfusion is a classic sensitizing event."),
                     ("A previous transplant.", False, "Prior grafts commonly sensitize.")],
         "sources": []},
        {"stem": "Which best describes a readiness tracker entry?",
         "options": [("Item, date done, disposition, repeat or expiry date, and owner of the next step.", True, "These fields keep a candidate ready on the day of an offer."),
                     ("Item name only.", False, "Without dates and owners, readiness cannot be judged."),
                     ("Free-text comments about the family.", False, "Not a tracker."),
                     ("The results of a single day's labs.", False, "Readiness spans many dated items.")],
         "sources": []},
        {"stem": "A wait-listed candidate is hospitalized with pneumonia. Who decides whether her list status changes?",
         "options": [("The transplant program, after the nurse reports the admission.", True, "The nurse reports; the program decides and communicates status."),
                     ("The ward nurse caring for her.", False, "Not within nursing authority."),
                     ("The patient herself.", False, "She participates, but listing status is a program decision."),
                     ("PhilHealth.", False, "Coverage does not determine clinical status.")],
         "sources": ["txcand2020"]},
        {"stem": "What does a cPRA of 95 percent mean in practice?",
         "options": [("Roughly 95 of 100 donors would be unsuitable on antibody grounds, so waiting is likely to be longer.", True, "High cPRA narrows the pool of compatible donors."),
                     ("The transplant will be 95 percent successful.", False, "cPRA is not a success rate."),
                     ("The candidate has a 95 percent match with her sibling.", False, "Not what cPRA measures."),
                     ("The candidate has no antibodies.", False, "High cPRA means broad sensitization.")],
         "sources": ["txcand2020"]},
        {"stem": "Why is psychosocial and financial review part of evaluation?",
         "options": [("Lifelong medicines, monitoring and visits require support, understanding and resources.", True, "Barriers identified early can be addressed before transplant."),
                     ("To exclude poor patients.", False, "The purpose is to identify and solve barriers, not exclude."),
                     ("To decide who will donate.", False, "Donor decisions are separate and voluntary."),
                     ("It is optional for recipients.", False, "It is a standard evaluation domain.")],
         "sources": ["txcand2020"]},
    ],
    "exam": [
        {"stem": "A listed candidate with an old serum sample on file reports a recent transfusion elsewhere. What is the correct sequence?",
         "options": [("Capture the date and records, notify the team and laboratory pathway, confirm the repeat-sampling owner, and document who will communicate any status change.", True, "Covers reporting, ownership and communication."),
                     ("Reassure her and record it at the next annual review.", False, "Delays an immunologic safety step."),
                     ("Order a crossmatch yourself.", False, "Outside nursing scope."),
                     ("Tell her she has been removed from the list.", False, "Status decisions and communication belong to the program.")],
         "sources": ["txcand2020"]},
        {"stem": "Does a high cPRA identify the antibody that would reject a particular donor's kidney?",
         "options": [("No. Donor-specific antibody testing and the crossmatch address a particular donor.", True, "cPRA summarizes breadth of sensitization."),
                     ("Yes. cPRA is donor-specific.", False, "It is population-based."),
                     ("Yes, if it is above 50 percent.", False, "No cutoff makes it donor-specific."),
                     ("Only for living donors.", False, "It is never donor-specific.")],
         "sources": ["txcand2020"]},
        {"stem": "A candidate missed two evaluation tests. What is the best first action?",
         "options": [("Contact through the approved route, assess barriers, document, and coordinate completion.", True, "Barrier-focused follow-up."),
                     ("Report nonadherence to the committee.", False, "Premature without exploring barriers."),
                     ("Discharge her from the program.", False, "Outside scope."),
                     ("Wait for her to reschedule.", False, "Passive; risks losing her.")],
         "sources": []},
    ],
}
