# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Two identifiers every time, why the weight decides the fluid goal and therefore must be true, wheelchair tare done right, blood pressure errors that move a reading by 20 mm Hg or more, why the oximeter can miss low oxygen, and why a symptom outranks a normal-looking number.",
    "desc": "Dialysis Nurse Assistant / PCA Module 5: patient identification, accurate pre- and post-dialysis weights with tare, interdialytic weight gain evidence, blood pressure measurement error, pulse oximetry limits, timed counts, and reporting without calculating treatment.",
    "keywords": "dialysis weight wheelchair tare, interdialytic weight gain percent, blood pressure measurement errors nursing aide, pulse oximetry skin color bias, two patient identifiers, dialysis vital signs assistant",
    "image_alt": "A dialysis nurse assistant reading a wheelchair scale while the patient sits calmly, a clipboard showing the weight, units and wheelchair tare.",
    "objectives": [
        "Identify every patient with two approved identifiers before any measurement.",
        "Explain why the pre-dialysis weight drives the fluid goal, and obtain a weight with units, clothing and tare recorded.",
        "Calculate a net weight and the weight gain since the last session, and report them without proposing a treatment change.",
        "Name the main sources of blood pressure and oximetry error and how to avoid them.",
        "Report a symptom or an unexpected reading at once, even when other numbers look normal.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "The scale is a witness",
         "html": """
<p>Think of each measurement as a witness statement. The RN and the physician were not at the scale. They will make a decision based on what your witness says. If the witness is honest and careful, the decision can be right. If the witness guesses, or speaks about the wrong person, the decision will be wrong, however skilled the decision makers are.</p>
<p>The picture has a limit. A witness can explain what they saw. A number cannot. So you add the context: the units, the scale, what the patient was wearing, the wheelchair, and anything that made the reading hard. And you report what the patient said and looked like, because a symptom can matter more than any number.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Right patient, right scale, right units, tare written down, reading written exactly. Symptoms first, numbers second. You measure and report; the RN decides.</div>
"""},
        {"id": "identity", "nav": "Identification", "tag": "Practice", "h2": "Two identifiers, every time",
         "html": """
<p>Use the unit&rsquo;s two approved identifiers, usually full name and date of birth, checked against the record or wristband, at every encounter where you measure or record. A chair number is not an identifier: patients move. A familiar face is not an identifier: two patients can share a surname, a barangay and a schedule. Ask the patient to state their name rather than asking &ldquo;Are you Mr. Reyes?&rdquo;, which invites a yes.</p>
<p>Before routine intake, ask how the patient feels. Chest pain, breathlessness, fainting, bleeding or a sudden change in alertness go to the RN <em>before</em> you continue. Routine forms never delay an urgent call.</p>
"""},
        {"id": "weight", "nav": "Weights and tare", "tag": "Physiology and evidence", "h2": "Why the weight must be true",
         "html": """
<p>Between sessions, almost all the weight a patient gains is water, because a person cannot gain two kilograms of fat in two days. The difference between today&rsquo;s weight before dialysis and the target weight after dialysis is the main input for the fluid the prescription will remove. An error of one kilogram on the scale can become a liter of fluid removed in error. Removing too much can drop the blood pressure (Module 2); removing too little leaves fluid in the lungs.</p>
<p>Weight gain between sessions is itself associated with outcomes. In 34,107 patients in the United States, after adjustment for nutrition and other factors, an average gain of 4.0 kilograms or more was associated with higher cardiovascular death than a gain of 1.5 to 2.0 kilograms (hazard ratio 1.25; 95% confidence interval 1.12 to 1.39). A gain under 1.0 kilogram was associated with lower risk (0.67).[[kalantar2009]] Excessive gain was also associated with higher mortality in DOPPS.[[saran2003]] These are associations, not targets you set: the unit&rsquo;s written threshold tells you when a gain must be reported at once.</p>
<div class="tc-formula"><strong>Worked example: the wheelchair weight.</strong> Mang Rolando, wheelchair scale.<br>Scale reading with chair: 78.6 kg. The empty chair, weighed on the same scale today: 15.2 kg. Clothing allowance the unit uses: 0 kg (he is wearing the usual light clothes).<br>Net weight = 78.6 &minus; 15.2 &minus; 0 = <strong>63.4 kg</strong>.<br>Last post-dialysis weight: 58.0 kg. Gain = 63.4 &minus; 58.0 = <strong>5.4 kg</strong>, which is 5.4 &divide; 58.0 &times; 100 = <strong>9.3%</strong> of his last post-dialysis weight.<br>Report: &ldquo;Ma&rsquo;am Jessa, Mang Rolando: 63.4 kilograms net on the wheelchair scale, chair weighed today at 15.2. Up 5.4 from his last post-weight. He is breathless when he talks.&rdquo; You do not suggest a fluid goal.</div>
<div class="table-wrap"><table>
<caption>Common weight errors</caption>
<thead><tr><th scope="col">Error</th><th scope="col">What it does to the number</th><th scope="col">Prevention</th></tr></thead>
<tbody>
<tr><td>Tare guessed, or taken from another chair</td><td>Off by several kilograms</td><td>Weigh the chair empty on the same scale, or use the unit&rsquo;s labeled tare</td></tr>
<tr><td>Wrong units (pounds read as kilograms)</td><td>Off by more than double</td><td>Check the display unit; convert with the toolkit</td></tr>
<tr><td>Shoes, jacket, bag or blanket on</td><td>Heavier than true</td><td>Same clothing as usual, or record the item</td></tr>
<tr><td>Scale not zeroed, or on an uneven floor</td><td>Drift up or down</td><td>Zero before use; report a scale that will not zero</td></tr>
<tr><td>Copied last weight</td><td>A fabricated value</td><td>Never; record &ldquo;not obtained&rdquo; and the reason</td></tr>
</tbody></table></div>
<p>Use the <a href="calc-dialysis-nurse-assistant-toolkit.html">Patient Care Assistant Toolkit</a> to check the arithmetic, including pounds to kilograms. A negative gain, or a gain far above the patient&rsquo;s usual, is a reason to re-check the tare and the units, and to tell the RN.</p>
"""},
        {"id": "vitals", "nav": "Blood pressure and oxygen", "tag": "Evidence", "h2": "Readings that lie, and how to stop them",
         "html": """
<p>Blood pressure readings are easy to get wrong. A systematic review of 328 studies found 29 sources of inaccuracy related to the patient, the device, the procedure and the person measuring. Single sources changed systolic readings by as much as 23.6 mm Hg too low or 33 mm Hg too high. The authors advised that one unexpected value should be repeated, not acted on alone.[[kallioinen2017]]</p>
<div class="table-wrap"><table>
<caption>Blood pressure: common sources of error</caption>
<thead><tr><th scope="col">Source</th><th scope="col">Effect</th><th scope="col">What you do</th></tr></thead>
<tbody>
<tr><td>Cuff too small for the arm</td><td>Reads too high</td><td>Choose the cuff size by the arm, using the cuff&rsquo;s markings</td></tr>
<tr><td>Talking, moving, legs crossed, arm unsupported</td><td>Usually reads higher</td><td>Seated quietly, back and arm supported, feet flat, no talking during the reading</td></tr>
<tr><td>Cuff over clothing</td><td>Unreliable</td><td>Cuff on bare skin</td></tr>
<tr><td>Wrong arm</td><td>Harm to the fistula or graft</td><td>Never on the access arm: use the arm the RN&rsquo;s plan names</td></tr>
</tbody></table></div>
<p>Pulse oximeters are useful but imperfect. In paired readings from hospital patients, among those whose oximeter showed 92% to 96%, the true arterial saturation was below 88% in 11.7% of readings in Black patients and 3.6% in White patients.[[sjoding2020]] Cold fingers, poor circulation, movement and nail polish also cause errors. The lesson for you: a reassuring oxygen number never cancels a patient who looks breathless, blue or drowsy.</p>
<div class="tc-formula"><strong>Worked example: a timed count.</strong> You count 19 beats in 15 seconds: 19 &times; 4 = 76 per minute. But the beats were irregular, so you count again for a full 60 seconds and get 84. Record 84, irregular, and tell the RN that the pulse was irregular. The toolkit converts 15-, 30- and 60-second counts and reminds you when to count for a full minute.</div>
<div class="tc-keyp"><strong>Symptoms outrank numbers.</strong> Report breathlessness, chest pain, confusion or a patient who &ldquo;looks different&rdquo; at once, whatever the readings show.</div>
"""},
        {"id": "report", "nav": "Reporting", "tag": "Practice", "h2": "Report the finding, not a prescription",
         "html": """
<p>Record what you measured, the units, the time, the device and any limitation (&ldquo;patient moving,&rdquo; &ldquo;cuff size large adult&rdquo;). If a reading surprises you and it is safe to do so, repeat it once as the RN directs, but never let repeating delay a call about a symptom.</p>
<p>Tell the RN about: a change from the patient&rsquo;s usual pattern; a gain above the unit&rsquo;s threshold; a fall since the last session; a missed session; fever symptoms; any concern about the access. Use a short structure:</p>
<div class="tc-plain"><span class="tc-lab">A short report</span><strong>Who:</strong> name and station. <strong>What:</strong> the reading or symptom, exactly. <strong>Context:</strong> usual pattern, tare, device, limits. <strong>Ask:</strong> &ldquo;Will you come and see him?&rdquo;</div>
<p>Pre- and post-dialysis weights support the clinical team&rsquo;s review. They do not authorize you to set a dry weight, a fluid goal or a treatment time.</p>
"""},
    ],
    "case": {
        "title": "63.4 kilograms and breathless",
        "html": """
<p><strong>Monday, 6:20 a.m.</strong> Mang Rolando Aquino, 68, comes after the long weekend. Bea weighs him on the wheelchair scale: 78.6 kg with the chair. Nobody knows this borrowed wheelchair&rsquo;s weight. His son says, &ldquo;The other chair was 14 kilos, just use that.&rdquo; Mang Rolando is sitting forward with his hands on his knees, breathing fast. He stops between words. His record shows a post-dialysis weight of 58.0 kg on Friday.</p>
""",
        "acte": {
            "Notice": "Breathlessness with stopping between words is urgent and outranks the weight. A guessed tare would produce an untrustworthy weight.",
            "Communicate": "Call the RN at once: &ldquo;Ma&rsquo;am Jessa, Mang Rolando at the scale is breathless, stopping between words. I am weighing the empty chair now.&rdquo; Then: &ldquo;Net 63.4, chair weighed at 15.2, up 5.4 from Friday.&rdquo;",
            "Do": "Keep him sitting upright, stay with him, and weigh the empty chair (or ask a colleague to) only once the RN is on the way.",
            "Escalate": "If he becomes drowsy, blue, or cannot speak, call the emergency route (Module 8).",
        },
        "task": "Write the record entry for the weight, including units, tare and how the tare was obtained.",
        "outcome": """
<p>The RN arrived within a minute and assessed him; the physician was called. The borrowed chair weighed 15.2 kg, not 14. With the guessed tare, the net weight would have been recorded 1.2 kg too high. The unit now labels every wheelchair with its weighed tare and the date.</p>
""",
    },
    "second_round": ("The standing scale reads 41.2 for a patient whose last post-weight was 58.0 kg.",
                     "What you check first, and what you tell the RN."),
    "evidence_out": "Two identifiers; equipment check; weight with units and tare; assigned observations by the approved technique; escalation of a symptom with closed-loop confirmation.",
    "critical": "Using the wrong patient record, guessing a tare or fabricating a measurement, putting a cuff on the access arm, or delaying an urgent symptom report.",
    "reflect": "Which measurement in your unit is most often guessed or copied? What would make the honest measurement easier?",
    "practice": {"intro": "Practice on colleagues and simulated patients first; then measure patients only after sign-off and under supervision.", "items": [
        "Verify two identifiers by asking the patient to state them.",
        "Check scale readiness (zero, units, level floor) and the transfer plan.",
        "Measure and record a weight with units, clothing and tare, and calculate the net weight and gain.",
        "Obtain assigned observations with correct cuff size, position and arm.",
        "Escalate a symptom or an unexpected reading with closed-loop confirmation.",
    ]},
    "readings": [("dry-weight-determination.html", "How the team decides a patient&rsquo;s dry weight."),
                 ("fluid-management-dialysis.html", "Weight gain between sessions and why it matters.")],
    "calcs": ["calc-dialysis-nurse-assistant-toolkit.html"],
    "terms": [("Tare", "The weight of a wheelchair or other item, subtracted from the scale reading to get the patient&rsquo;s weight."),
              ("Net weight", "The patient&rsquo;s weight alone, after the tare and any clothing allowance are subtracted."),
              ("Interdialytic weight gain (IDWG)", "Weight gained between the end of one session and the start of the next; almost all is water."),
              ("Occult hypoxemia", "Low oxygen in the blood that the pulse oximeter fails to show.")],
    "quiz": [
        {"stem": "Why is almost all weight gained between sessions treated as water?", "options": [
            ("A person cannot gain kilograms of body tissue in two days; the gain is retained fluid.", True, "So the weight drives the fluid goal."),
            ("Because food weighs nothing.", False, "Food has weight, but most of what stays between sessions is the water it contains."),
            ("Because the scale measures only water.", False, "A scale measures total weight; the reasoning is about what changes in two days."),
            ("It is not; it is mostly fat.", False, "Not over two days.")], "sources": []},
        {"stem": "Net weight with a wheelchair reading of 81.0 kg and a weighed tare of 16.5 kg is:", "options": [
            ("64.5 kg.", True, "81.0 minus 16.5."),
            ("97.5 kg.", False, "That adds the tare."),
            ("81.0 kg.", False, "Tare not subtracted."),
            ("16.5 kg.", False, "That is the chair.")], "sources": []},
        {"stem": "Post-weight last session 60.0 kg; today net 63.0 kg. The gain as a percent of the post-weight is:", "options": [
            ("5.0%.", True, "3.0 divided by 60.0, times 100."),
            ("3.0%.", False, "That is the kilograms, not the percent."),
            ("4.8%.", False, "That divides by 63.0."),
            ("50%.", False, "Arithmetic error.")], "sources": []},
        {"stem": "In 34,107 patients, a gain of 4.0 kg or more versus 1.5 to 2.0 kg was associated with:", "options": [
            ("Higher cardiovascular death (hazard ratio 1.25).", True, "An adjusted association, not a target you set."),
            ("Lower death.", False, "The opposite after adjustment."),
            ("No difference.", False, "A difference was found."),
            ("Better nutrition and no risk.", False, "Risk rose after adjustment.")], "sources": ["kalantar2009"]},
        {"stem": "The son says to use another chair&rsquo;s tare. You:", "critical": True, "options": [
            ("Weigh this chair empty or use its labeled tare; never guess.", True, "A guessed tare gives a false weight."),
            ("Use the other chair&rsquo;s tare.", False, "Chairs differ."),
            ("Subtract 15 kg as usual.", False, "Guessing."),
            ("Skip the weight.", False, "Measure properly instead.")], "sources": []},
        {"stem": "A cuff that is too small for the arm usually makes blood pressure read:", "options": [
            ("Too high.", True, "Choose the cuff by arm size."),
            ("Too low.", False, "Usually too high."),
            ("Exactly right.", False, "A wrong cuff size biases the reading."),
            ("Zero.", False, "A small cuff still gives a number, just a falsely high one.")], "sources": ["kallioinen2017"]},
        {"stem": "Where must you never place a blood pressure cuff?", "critical": True, "options": [
            ("On the arm with the fistula or graft.", True, "Constriction can damage the access."),
            ("On the arm the RN named.", False, "That is correct practice."),
            ("On bare skin.", False, "Bare skin is where the cuff belongs."),
            ("On a supported arm.", False, "A supported arm improves accuracy.")], "sources": ["lok2020"]},
        {"stem": "The oximeter shows 95% but the patient is breathless and gray. What is true?", "options": [
            ("Oximeters can miss low oxygen; report the patient&rsquo;s appearance at once.", True, "Symptoms outrank numbers."),
            ("95% means he is fine.", False, "Not if he looks unwell."),
            ("Change fingers until it reads 100%.", False, "No."),
            ("Record 95% and move on.", False, "Unsafe.")], "sources": ["sjoding2020"]},
        {"stem": "You count 21 beats in 15 seconds and the rhythm is irregular. Next?", "options": [
            ("Count for a full 60 seconds and report the rhythm as irregular.", True, "Short counts mislead in irregular rhythms."),
            ("Record 84 and move on.", False, "Recount for a full minute."),
            ("Record 21.", False, "Not per minute."),
            ("Ignore the irregularity.", False, "Report it.")], "sources": []},
        {"stem": "Which identification is acceptable?", "critical": True, "options": [
            ("The patient states full name and date of birth, checked against the record.", True, "Two approved identifiers."),
            ("Chair number.", False, "Patients move."),
            ("&ldquo;Are you Mr. Reyes?&rdquo; and a nod.", False, "Invites a yes."),
            ("Recognizing the face.", False, "Not reliable.")], "sources": []},
    ],
    "exam": [
        {"half": "a", "critical": True, "stem": "A familiar patient needs identification:", "options": [
            ("With two approved identifiers at each relevant encounter.", True, "Familiarity and location are not identity checks."),
            ("Only on the first visit.", False, "Identity is checked at every encounter, not once."),
            ("By chair number.", False, "No."),
            ("Only if a new nurse is on duty.", False, "Staffing changes nothing; two identifiers every time.")], "sources": []},
        {"half": "a", "critical": True, "stem": "Breathlessness during intake requires:", "options": [
            ("RN review immediately.", True, "Urgent symptoms take priority over routine intake."),
            ("Completion of the whole form first.", False, "Delay."),
            ("Independent adjustment of the dialysis prescription.", False, "Not your role."),
            ("A second weight before calling.", False, "Call first.")], "sources": []},
        {"half": "b", "stem": "An unknown wheelchair tare should be:", "options": [
            ("Resolved by weighing the chair or using the approved labeled tare.", True, "Guessing produces a misleading weight."),
            ("Estimated silently.", False, "No."),
            ("Copied from another chair.", False, "Chairs differ."),
            ("Ignored.", False, "The weight would be wrong.")], "sources": []},
        {"half": "b", "critical": True, "stem": "Who sets the fluid-removal target?", "options": [
            ("The authorized clinical team.", True, "Measuring weight does not confer prescribing authority."),
            ("The assistant, from the weight difference.", False, "The weight difference informs the RN and physician; it is not a prescription."),
            ("The transport driver.", False, "The driver has no role in the prescription."),
            ("The patient&rsquo;s relative.", False, "Relatives may share information, but the clinical team sets the goal.")], "sources": []},
    ],
}
