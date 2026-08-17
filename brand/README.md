# Renal Care Matters — Brand Assets

Vectorized from the approved Canva logo. Colors: Navy `#1F3864`, Gold `#B4894C`
(soft gold `#C9A66B` on dark), Cream `#FBF8F2`. Type: Lora (wordmark),
Poppins (tagline).

## Files
Lockups (SVG = scalable master, PNG = ready-to-use @2x):
- logo-horizontal-light — icon + divider + wordmark, for light/cream backgrounds
- logo-horizontal-dark — same, on navy background
- logo-stacked-light / -dark — icon centered above wordmark
- *-transparent.png — light lockups with no background fill

Icon:
- icon.svg — full-color mark (navy kidney + gold nephron/leaf), transparent
- icon-dark.svg — cream kidney + gold, for dark backgrounds
- icon-mono-navy.svg — single-color navy
- icon-512.png / icon-1024.png — raster exports, transparent

Favicons / app icons:
- favicon.ico (16–256), favicon-16/32/48.png, favicon.svg
- apple-touch-icon-180.png, icon-512-tile.png (navy rounded tile)

## Web usage
Place this `brand/` folder at the site root. The landing page already links:
  <link rel="icon" href="brand/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="brand/icon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="brand/apple-touch-icon-180.png">

The header/footer logo is an inline SVG sprite (`#rcm-icon`) recolored per context
via CSS custom properties `--k` (kidney) and `--l` (leaf).

## Clear space & minimum size
Keep clear space ≥ the width of the kidney around the lockup.
Minimum icon size on screen: 24px. Below ~20px use the navy tile favicon.

## Social / OG share image
- og-image.png (1200×630) — light, for og:image / twitter:image
- og-image-dark.png (1200×630) — navy alternative
- The landing page <head> now references brand/og-image.png.
