# WGM Rivero Image Prompts

A Claude Code plugin bundling the image-generation prompt-authoring skills used to produce
every visual asset on [renalcarematters.com](https://renalcarematters.com) — a nephrology
patient-education site. Each skill outputs a single copy-paste prompt engineered for the
ChatGPT Image Generator GPT, in a consistent house style (Inter / Nunito Sans / IBM Plex Sans /
Manrope typography only, light backgrounds, `© renalcarematters.com` attribution, no journal or
guideline brand names).

## Skills included

| Skill | Produces |
|---|---|
| `williamriveromd-hero-vignette` | The circular-vignette hero graphic beside a guide's title (2048×2048, 85–90% diameter disc, title-safe zone) |
| `williamriveromd-infographic-skill` | Editorial hero images, pathophysiology posters, clinical algorithms, multi-panel infographics, clinician reference cards, food matrices, case snapshots, circular workflows, 3D medical renderings |
| `williamriveromd-simple-figure` | One focused figure — a single flowchart, comparison panel, mechanism diagram, step sequence, or reference table |
| `williamriveromd-biomedical-mechanism-figure` | Review-article biomedical mechanism schematics — organ-level panel → magnified functional-unit inset → injury → intervention → benefit flow |
| `williamriveromd-organ-crosstalk-sigil-graphic` | Minimal line-art "organ sigil" diagrams showing organ crosstalk / physiology feedback loops |
| `williamriveromd-algorithm-generator-skill` | Clinical algorithm flowcharts in AHA-resuscitation or journal-treatment-algorithm style |
| `williamriveromd-local-image-generator` | Stage 2 of the pipeline — validates prompts from any of the above, builds the local folder structure, manifests, and wires finished images into a guide |

## Pipeline

1. **Stage 1** — invoke one of the prompt-authoring skills (`infographic-skill`, `simple-figure`,
   `biomedical-mechanism-figure`, `hero-vignette`, `algorithm-generator-skill`, or
   `organ-crosstalk-sigil-graphic`) to produce a copy-paste prompt for the
   [ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).
2. **Stage 2** — invoke `williamriveromd-local-image-generator` to validate the prompt(s),
   build the local `image-prompts/` / `generated-images/` folder structure and manifest, and
   (once you've generated and saved the images) wire them into the guide's HTML.

## Installation

```
/plugin marketplace add williamrivero/williamriveromd.github.io
/plugin install wgmr-image-prompts@williamriveromd-graphics
```

Or test locally without installing:

```
claude --plugin-dir ./wgmr-image-prompts
```

## License

MIT
