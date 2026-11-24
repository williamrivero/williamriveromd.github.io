#!/bin/bash
# Finish and publish the Transplant Nurse subtrack from this Mac (git and the Calculo build need locally downloaded files).
# Run from the repo root:  bash ship-transplant-nurse.sh
set -e
cd "$(dirname "$0")"
exec > >(tee ship-transplant-nurse.log) 2>&1
python3 build_calc_app.py || echo "build_calc_app skipped (the sitemap workflow runs it on push)"
python3 generate_latest_calculators.py || true
python3 generate_sitemap.py || true
git add academy/transplant-nurse*.html academy/nephrology-nursing.html \
        academy/nephrology-nursing-11-transplantation-special-populations.html academy/index.html \
        guides/calc-tacrolimus-level-check.html guides/calculators.html guides/calc-offline-manifest.json \
        guides/calc-app.webmanifest guides/calc-sw.js latest_calculators.json sitemap.xml \
        assets/nursing-course.js generate_transplant_nurse.py generate_nursing_course.py generate_tech_courses.py \
        tools/academy/publish_academy.py tools/transplant_nurse data/transplant-nurse docs/transplant-nurse \
        images/transplant-nurse-* images/resp/transplant-nurse-* images/og/transplant-nurse-* \
        ship-transplant-nurse.sh ship-transplant-nurse.command
git commit -m "Add Transplant Nurse subtrack to the Renal Care Academy

Hub, 12 modules, end-of-course knowledge check (one question per module, pass 10/12),
Tacrolimus Level Check calculator, entry links from Nephrology Nursing Module 11,
the Nephrology Nursing hub and the Academy landing page, and the image prompt pack, with 13 heroes and 12 teaching figures."
git pull --rebase --autostash origin main
git push origin main
echo SHIP-DONE
