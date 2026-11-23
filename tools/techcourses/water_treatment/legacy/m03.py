# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A reverse osmosis unit with pressure gauges and flow meters.",
    "objectives": [
        "Explain in plain words how a reverse osmosis membrane separates product water from reject water.",
        "Calculate percent rejection and percent recovery, and say what a change in each suggests.",
        "Describe how the distribution loop is designed to discourage bacterial growth.",
        "Identify dead legs and other places where water can stand still.",
    ],
    "big": """
{{plain:Think of a fine cloth stretched over a pot when you strain coconut milk. You press down, the liquid runs through, and the grated coconut stays behind on the cloth. Reverse osmosis works the same way, with a pump doing the pressing and a membrane far finer than any cloth. Water molecules pass. Most dissolved salts, metals, bacteria, and endotoxin do not.}}
<p>The picture has a limit. A cloth is squeezed once and thrown away with the pulp. A reverse osmosis membrane works all day, and the material it holds back must be carried off continuously, or it builds up on the surface. So the unit makes two streams: product water, which passed through, and reject water, which washes away what was held back. From there a loop of pipe carries the product water past every station and back again, always moving.</p>
{{cards:Key terms for this module|Membrane::A thin sheet, rolled into a cartridge, with pores too small for most dissolved substances.|Product water::The clean water that passes through the membrane. Also called permeate.|Reject water::The stream that carries away what the membrane held back. Also called concentrate.|Percent rejection::How much of the dissolved salt the membrane stopped.|Percent recovery::How much of the feed water became product water.|Dead leg::A branch of pipe where water sits still.|Biofilm::A slimy layer of bacteria stuck to a surface. Once it forms it is hard to kill.}}
""",
    "case": {
        "title": "The numbers that drifted",
        "html": """
<p>It is the last Saturday of the month, after the second shift. Ms. Grace Tolentino, 35, the water treatment technician, sits down with the reverse osmosis log to prepare the monthly summary for the chief technician, Mr. Arnel Bautista.</p>
<p>She notices that product water conductivity has crept up from 8 to 19 microsiemens per centimeter over the month, while the feed water has stayed near 400. No alarm has sounded, because the alarm is set at 30. Product flow has also fallen a little over the same weeks.</p>
""",
        "questions": ["What was the percent rejection at the start of the month, and what is it now?",
                      "No alarm has sounded. Is there anything to report?",
                      "What might be happening to the membrane?"],
    },
    "sections": [
        ("ro", "How it works", "How reverse osmosis works", """
<p>Separate salty water from pure water with a fine membrane, and water moves on its own toward the salty side. This is osmosis. Reverse osmosis uses a pump to push the other way: pressure forces water out of the salty side, through the membrane, and leaves the salts behind.</p>
{{flow:Inside the reverse osmosis unit|Feed::Pretreated water enters.|Pump::Raises the pressure against the membrane.|Membrane::Water passes; most salts, bacteria, and endotoxin do not.|Product::Clean water goes on to the loop.|Reject::Concentrated water goes to drain, or part of it is recycled.}}
{{fig:wts_dualpass|Some systems pass the product water through a second set of membranes (dual pass) for higher purity. The principle at each pass is the same.}}
<p>A membrane is damaged by chlorine, plugged by scale and dirt, and fouled by bacteria. That is why the pretreatment stages matter so much. Temperature matters as well, because water moves through the membrane more slowly when it is cold: output falls by roughly 3 percent for each degree Celsius the feed water cools. The practical point is that a unit that keeps up in summer may fall short on a cold morning.</p>
"""),
        ("numbers", "Rejection and recovery", "Two calculations every technician should know", """
{{formula:<strong>Percent rejection</strong> = (feed conductivity &minus; product conductivity) &divide; feed conductivity &times; 100<br>Example: feed 400, product 8. (400 &minus; 8) &divide; 400 &times; 100 = 98%.}}
{{formula:<strong>Percent recovery</strong> = product flow &divide; feed flow &times; 100<br>Example: product 6 liters per minute from a feed of 10 liters per minute = 60%.}}
<p>Conductivity measures how easily water carries electricity, and that depends on the salts dissolved in it. So conductivity is a convenient stand-in for the amount of dissolved material. Rejection tells you how well the membrane is separating. A healthy membrane usually rejects well over 90 percent; your system&rsquo;s manual gives the expected figure and the alarm point. Recovery tells you how hard the membrane is being worked. Push recovery too high and the salts concentrate on the reject side until they form scale.</p>
{{cards:Reading the changes|Rejection falling::Membrane damage (often from chlorine), a leaking seal, or scaling. Report it even if no alarm has sounded.|Product flow falling::Fouling or scaling, colder feed water, or low pump pressure.|Feed-side pressure drop rising::The membrane or its prefilter is plugging.|Sudden change after service::Something was put back together incorrectly.}}
{{key:Conductivity does not detect chlorine, chloramine, bacteria, or endotoxin. A perfect rejection figure never replaces the chlorine test or the monthly cultures.}}
"""),
        ("loop", "The loop", "The distribution loop", """
{{fig:wts_layout}}
<p>Product water travels to the stations through a loop of smooth pipe that returns to where it started. Bacteria settle and multiply where water stands still. So the loop is built to keep the water moving at all times, including at night and on days off.</p>
{{cards:Features of a well-designed loop|Continuous flow::Water returns to the start instead of stopping at the last station.|Smooth, suitable materials::Pipes and joints that do not shed chemicals or give bacteria crevices to hide in.|No dead legs::Branches to the machines are kept as short as possible.|Direct feed where possible::Many modern systems have no storage tank; where a tank exists it has a tight lid, a filtered vent, and a sloped base that drains completely.|Sample ports::Clean, easy-to-reach points for taking samples at the start and at the end of the loop.}}
{{fig:wts_isolation}}
<p>Some systems add an ultraviolet lamp to kill bacteria in a loop fed from a storage tank, followed by an ultrafilter to remove the dead cells and the endotoxin they release. A lamp that has lost its output, or a filter that is overdue, gives little protection while looking normal. So both have their own checks and their own replacement dates.</p>
{{fig:wts_pou}}
"""),
    ],
    "debrief": ["""
<p><strong>The rejection, then and now.</strong> At the start of the month rejection was (400 &minus; 8) &divide; 400 = 98 percent. Now it is (400 &minus; 19) &divide; 400 = about 95 percent. The membrane is letting through more than twice as much salt as it did four weeks ago.</p>
<p><strong>Is there anything to report?</strong> Yes. The alarm has not sounded, but the trend is clear, and a clear trend is reportable. Tell Mr. Bautista, or whoever is responsible for the system, with the figures in front of you, and record that you told him. An alarm marks the point where the problem is already large; a trend lets the unit act while it is still small.</p>
<p><strong>What might be happening to the membrane.</strong> Falling rejection together with falling flow suggests the membrane is scaling or fouling. Falling rejection on its own, especially after a chlorine breakthrough, suggests the membrane has been damaged. Finding the cause is for the responsible person and the service provider. Your part was to notice it three weeks before the alarm would have.</p>
"""],
    "skills": {
        "title": "Reverse osmosis readings and loop inspection",
        "intro": "Materials: the reverse osmosis unit&rsquo;s display and gauges, the log, a calculator, and the loop drawing.",
        "items": [("Reads and records feed and product conductivity, flows, and pressures with units.", False),
                  ("Calculates percent rejection and percent recovery correctly.", True),
                  ("Compares today&rsquo;s figures with the last two weeks and describes any trend.", False),
                  ("States the alarm settings for the unit and what happens when each is reached.", False),
                  ("Traces the loop from supply to return and points out every sample port.", False),
                  ("Identifies any dead leg or unused branch and reports it.", True),
                  ("Explains why conductivity does not replace chlorine testing or cultures.", True)],
        "placement": "Plot one month of product conductivity and product flow from your unit&rsquo;s log on graph paper or a spreadsheet and discuss the shape with your preceptor.",
    },
    "quiz": [
        ("What passes through a reverse osmosis membrane most easily?",
         ["Dissolved salts", "Bacteria", "Water", "Endotoxin"], 2, "Pressure forces water through; most dissolved and suspended material is held back."),
        ("Feed conductivity is 500 and product conductivity is 25. What is the percent rejection?",
         ["5%", "75%", "95%", "99.5%"], 2, "(500 &minus; 25) &divide; 500 &times; 100 = 95%."),
        ("Feed flow is 20 liters per minute and product flow is 12. What is the percent recovery?",
         ["8%", "40%", "60%", "167%"], 2, "12 &divide; 20 &times; 100 = 60%."),
        ("Rejection has fallen steadily for three weeks but no alarm has sounded. What should you do?",
         ["Wait for the alarm", "Report the trend and record that you reported it", "Raise the alarm setting", "Stop recording conductivity"], 1,
         "A trend is information. Reporting it early prevents a failure."),
        ("Which of these does conductivity NOT detect?",
         ["A rise in dissolved salts", "A leaking membrane seal", "Chloramine", "A fall in membrane rejection"], 2,
         "Chlorine and chloramine at harmful levels barely change conductivity. Only the chlorine test detects them."),
        ("Why does the loop return water to its starting point?",
         ["To save pipe", "To keep water moving so bacteria have less chance to settle", "To warm the water", "To add chlorine"], 1,
         "Stagnant water allows biofilm to form."),
        ("What is a dead leg?",
         ["A broken pump", "A branch of pipe where water does not circulate", "A used membrane", "A drain line"], 1,
         "Dead legs let bacteria grow and seed the rest of the loop."),
        ("Product flow drops on an unusually cold morning with no other change. What is the most likely reason?",
         ["Chlorine damage", "Cold water passes through the membrane more slowly", "The softener is regenerating", "Endotoxin in the loop"], 1,
         "Membrane output falls as feed water temperature falls."),
    ],
    "terms": [("Osmosis", "The natural movement of water through a membrane toward the side with more dissolved material."),
              ("Microsiemens per centimeter", "The unit of conductivity for very pure water."),
              ("Fouling", "A build-up of dirt, organic matter, or bacteria on a membrane."),
              ("Scaling", "A crust of minerals on a membrane or pipe."),
              ("Ultrafilter", "A filter fine enough to hold back bacteria and endotoxin.")],
    "readings": [("dialysis-water-treatment-systems.html", "Loop layouts, dual-pass design, and capacity sizing.")],
    "calcs": ["calc-ro-recovery-dualpass.html", "calc-dialysis-water-reuse.html"],
}
