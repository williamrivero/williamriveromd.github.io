#!/usr/bin/env bash
# convert-landmark-images.sh
# Converts 11 landmark-trial PNG images to WebP and copies both to images/
# Requirements: cwebp  (brew install webp)
# Usage: bash convert-landmark-images.sh [source-dir]
set -euo pipefail

SOURCE_DIR="${1:-/Users/williamgregoryriveromd/Documents/williamriveromd.github.io/images}"
DEST_DIR="$(cd "$(dirname "$0")" && pwd)/images"

IMAGES=(
  "landmark-ckd-progression-mdrd-aask-sprint.png"
  "landmark-acei-arb-revolution-rein-renaal-idnt.png"
  "landmark-diabetes-era-dcct-ukpds-advance.png"
  "landmark-sglt2-revolution-empa-canvas-credence-dapa-empakidney.png"
  "landmark-four-pillars-ckm-rasi-sglt2i-nsmra-glp1.png"
  "landmark-finerenone-fidelio-figaro-fidelity.png"
  "landmark-glp1-kidney-flow-trial.png"
  "landmark-anemia-trials-choir-create-treat.png"
  "landmark-dialysis-trials-hemo-mpo-evolve.png"
  "landmark-transplant-milestones-symphony-benefit.png"
  "landmark-hdf-trials-contrast-eshol-turkish-convince.png"
)

if ! command -v cwebp &>/dev/null; then
  echo "ERROR: cwebp not found. Install with: brew install webp"
  exit 1
fi

echo "Converting ${#IMAGES[@]} landmark images..."
for img in "${IMAGES[@]}"; do
  src="$SOURCE_DIR/$img"
  webp="${img%.png}.webp"
  [ -f "$src" ] || { echo "  MISSING: $src"; continue; }
  cp "$src" "$DEST_DIR/$img"
  cwebp -q 88 -m 6 "$src" -o "$DEST_DIR/$webp"
  echo "  OK: $img → $webp"
done

echo ""
echo "Done. Now commit and push:"
echo "  git add images/landmark-*.png images/landmark-*.webp"
echo "  git commit -m 'Add 11 landmark trial images (PNG + WebP)'"
echo "  git push"
