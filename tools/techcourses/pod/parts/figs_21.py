# -*- coding: utf-8 -*-
"""New illustrated figures for Physician on Duty, Module 21. key: (file in images/, alt text, default caption).
The image files do not exist yet; the page leaves the slot empty until the art is produced."""

FIGS = {
    "pod21_kidney_to_red_cell": ("physician-on-duty-21-kidney-to-red-cell.webp",
                                 "A flow from left to right. An oxygen sensor in the kidney sends erythropoietin, the hormone that orders red cell "
                                 "production, to the bone marrow, which releases red cells into the blood. Four breaks are marked in red: too little "
                                 "erythropoietin from the failed kidney; hepcidin, a liver hormone, locking iron away; blood lost in the dialysis "
                                 "circuit, in blood tests, and from the gut; and red cells that die sooner than normal.",
                                 "From kidney to red cell. The failed kidney sends too few orders, inflammation locks the iron away, blood is lost "
                                 "at every step, and red cells die early. Each break lowers the hemoglobin by a different route."),
    "pod21_iron_warehouse": ("physician-on-duty-21-iron-warehouse-trucks.webp",
                             "Three panels. Each shows a warehouse labeled ferritin (stored iron) and delivery trucks labeled transferrin "
                             "saturation (TSAT, iron in transit) driving to a factory labeled bone marrow. Panel one, absolute iron deficiency: "
                             "an empty warehouse and empty trucks. Panel two, functional iron deficiency: a full warehouse with its door locked "
                             "by hepcidin and empty trucks. Panel three, iron replete: a stocked warehouse and loaded trucks.",
                             "Ferritin is the stock in the warehouse. Transferrin saturation is the iron on the trucks. A full warehouse with "
                             "empty trucks means the door is locked, usually by inflammation."),
    "pod21_phosphate_in_out": ("physician-on-duty-21-phosphate-in-out.webp",
                               "A weekly balance drawing. A large stream of phosphate enters from meals across seven days. Three smaller buckets, "
                               "one for each dialysis session, bail phosphate out, and a sieve labeled binders catches part of it at meals. A "
                               "shaded gap between intake and removal stays in the body.",
                               "Phosphate comes in every day with food and leaves only during sessions. Binders and diet narrow the gap; "
                               "standard thrice-weekly dialysis cannot close it alone."),
    "pod21_overworked_parathyroid": ("physician-on-duty-21-overworked-parathyroid.webp",
                                     "A mechanism figure. Low calcitriol (active vitamin D), high phosphate, and high fibroblast growth factor 23 "
                                     "(FGF23) all push on the parathyroid glands, which enlarge from four small glands into nodular glands. Two "
                                     "outputs come from the enlarged glands: calcium pulled out of bone, and calcium and phosphate deposited in "
                                     "the wall of an artery.",
                                     "Secondary hyperparathyroidism. Low active vitamin D, high phosphate, and high FGF23 drive the glands to "
                                     "grow. The bone is drained and the vessels calcify."),
    "pod21_bone_and_vessel": ("physician-on-duty-21-bone-and-vessel.webp",
                              "Side-by-side panels. On the left, healthy bone with a dense structure and a supple artery with a clear wall. On "
                              "the right, thinned bone with calcium leaving it, and an artery wall stiffened by white calcium deposits.",
                              "The calcification paradox. Calcium leaves the skeleton and settles in the arteries, so the patient can have weak "
                              "bones and stiff vessels at the same time."),
    "pod21_calciphylaxis": ("physician-on-duty-21-calciphylaxis.webp",
                            "An illustrated thigh, not a patient photograph, showing a net-like purple mottling (livedo), a firm purple "
                            "plaque, and a black crust (eschar) over a central ulcer. A label reads report the same day. An inset shows a "
                            "small skin artery narrowed by calcium and clot.",
                            "Calciphylaxis. Very painful purple mottling or plaques that turn into black, crusted ulcers, often on fatty "
                            "areas such as the thighs, abdomen, and buttocks. Report any such lesion to the attending nephrologist the same day."),
}
