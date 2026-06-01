#!/usr/bin/env bash
# Run this from your LOCAL repo root:
# cd /Users/williamgregoryriveromd/Documents/williamriveromd.github.io
# bash convert-slowing-ckd-images.sh

set -e
IMGDIR="images"
FILES=(
  slowing-ckd-progression-og
  slowing-ckd-progression-hero
  slowing-ckd-mechanisms-poster
  slowing-ckd-egfr-dip-explainer
  slowing-ckd-four-pillars
  slowing-ckd-uacr-categories
  slowing-ckd-bp-target-monitoring
  slowing-ckd-sick-day-rules
  slowing-ckd-red-flags
  slowing-ckd-action-plan
)

# Require cwebp (brew install webp)
if ! command -v cwebp &>/dev/null; then
  echo "cwebp not found. Install with: brew install webp"
  exit 1
fi

for NAME in "${FILES[@]}"; do
  SRC="$IMGDIR/${NAME}.png"
  DST="$IMGDIR/${NAME}.webp"
  if [ ! -f "$SRC" ]; then
    echo "MISSING: $SRC — skipping"
    continue
  fi
  cwebp -q 85 "$SRC" -o "$DST"
  echo "✓  $DST"
done

echo ""
echo "All done. Now stage and push:"
echo "  git add images/slowing-ckd-*.png images/slowing-ckd-*.webp"
echo "  git pull origin claude/blissful-rubin-h1tBf"
echo "  git push -u origin claude/blissful-rubin-h1tBf"
