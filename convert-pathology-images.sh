#!/usr/bin/env bash
# convert-pathology-images.sh
# Run this locally on your Mac to convert the 11 pathology PNG images to WebP
# and copy both formats into the repo's images/ directory.
#
# Requirements: cwebp (brew install webp)
# Usage: bash convert-pathology-images.sh /path/to/source/images/

set -euo pipefail

SOURCE_DIR="${1:-/Users/williamgregoryriveromd/Documents/williamriveromd.github.io/images}"
DEST_DIR="$(cd "$(dirname "$0")" && pwd)/images"

IMAGES=(
  "gn-spectrum-immunofluorescence-panel.png"
  "nephrotic-vs-nephritic-comparison.png"
  "aki-three-compartment-diagram.png"
  "atn-ischemic-vs-nephrotoxic-pathology.png"
  "ckd-progression-map-kdigo-heatmap.png"
  "ckd-mbd-renal-osteodystrophy-cascade.png"
  "diabetic-nephropathy-progression-interventions.png"
  "cardiorenal-syndrome-five-types-diagram.png"
  "hyperkalemia-management-algorithm.png"
  "acid-base-disorders-four-quadrant-map.png"
  "hyponatremia-management-algorithm.png"
)

if ! command -v cwebp &>/dev/null; then
  echo "ERROR: cwebp not found. Install with: brew install webp"
  exit 1
fi

echo "Converting and copying ${#IMAGES[@]} images..."
echo "  Source: $SOURCE_DIR"
echo "  Dest:   $DEST_DIR"
echo ""

for img in "${IMAGES[@]}"; do
  src="$SOURCE_DIR/$img"
  webp="${img%.png}.webp"
  if [ ! -f "$src" ]; then
    echo "  MISSING: $src"
    continue
  fi
  cp "$src" "$DEST_DIR/$img"
  cwebp -q 88 -m 6 "$src" -o "$DEST_DIR/$webp"
  echo "  OK: $img + $webp"
done

echo ""
echo "Done. Now commit and push:"
echo "  cd $(dirname "$DEST_DIR")"
echo "  git add images/*.png images/*.webp"
echo "  git commit -m 'Add 11 pathology reference images (PNG + WebP)'"
echo "  git push -u origin claude/cool-hamilton-57RNP"
