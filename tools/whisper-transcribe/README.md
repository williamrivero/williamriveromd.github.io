# whisper-transcribe — local Taglish consultation pipeline

Audio file → Whisper (large-v3) → raw transcript → local LLM (Ollama) → SOAP note draft + patient-facing summary.

**Everything stays on your machine.** No cloud calls except to your local Ollama at `http://localhost:11434`. Audio and transcripts live outside this git repo (default `~/clinical-transcripts/`) so they can never be committed.

> **PHI reminder.** This tool produces drafts only. Review every SOAP note and patient summary before using it clinically. Whisper occasionally hallucinates text in silence; LLMs occasionally invent details. The prompts instruct the model not to invent, but you are the safety net.

---

## One-time setup

### 1. System dependencies

**macOS:**
```bash
brew install ffmpeg
brew install ollama          # or download from https://ollama.com
```

**Linux:**
```bash
sudo apt install ffmpeg
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Python environment

Use a virtualenv so Whisper's torch dependency does not pollute your system Python.

```bash
cd tools/whisper-transcribe
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

First run will download the Whisper `large-v3` model (~3 GB) into `~/.cache/whisper/`.

### 3. Ollama model

In another terminal:
```bash
ollama serve                 # leave this running
```

Then pull the LLM (one-time, ~5 GB):
```bash
ollama pull llama3.1:8b
```

If your machine has plenty of RAM (32 GB+), `qwen2.5:14b` produces noticeably better Taglish output:
```bash
ollama pull qwen2.5:14b
export OLLAMA_MODEL=qwen2.5:14b
```

### 4. Storage folder

```bash
mkdir -p ~/clinical-transcripts/inbox
mkdir -p ~/clinical-transcripts/output
```

Drop audio files into `~/clinical-transcripts/inbox/`. Outputs land in `~/clinical-transcripts/output/<basename>/`.

---

## Usage

```bash
source .venv/bin/activate
python transcribe.py ~/clinical-transcripts/inbox/2026-05-14-juan-dela-cruz.m4a
```

Produces:
```
~/clinical-transcripts/output/2026-05-14-juan-dela-cruz/
├── raw_transcript.txt
├── soap_note.md
└── patient_summary.md
```

### Useful flags

```bash
# Transcript only, skip the LLM passes
python transcribe.py audio.m4a --skip-llm

# Use a different Ollama model for one run
python transcribe.py audio.m4a --ollama-model qwen2.5:14b

# Smaller / faster Whisper model (lower Taglish accuracy)
python transcribe.py audio.m4a --whisper-model medium

# Custom output folder
python transcribe.py audio.m4a --output-dir ~/Desktop/today-visit
```

---

## Performance notes

| Hardware                | Whisper large-v3, 30-min audio | Ollama llama3.1:8b SOAP |
|-------------------------|-------------------------------:|------------------------:|
| Apple M2 (CPU + MPS)    |                       ~3–5 min |              ~30–60 sec |
| Intel CPU only          |                     ~15–25 min |              ~2–4 min   |
| Nvidia RTX 3060+ (CUDA) |                     ~30–60 sec |              ~10–20 sec |

To enable CUDA acceleration on supported GPUs, edit `transcribe.py` and change `fp16=False` to `fp16=True`.

---

## Customising the prompts

The two prompt templates are plain text with a single `{TRANSCRIPT}` placeholder:

- `prompts/soap_note.txt` — SOAP note structure
- `prompts/patient_summary.txt` — patient-facing summary structure

Tweak freely. The prompts already instruct the model not to invent facts and to mark missing sections explicitly.

---

## Privacy boundary

| Component                | Sees PHI? | Where it runs   |
|--------------------------|-----------|-----------------|
| Whisper                  | yes       | your machine    |
| Ollama + LLM             | yes       | your machine    |
| This repo (`tools/`)     | no        | git             |
| `~/clinical-transcripts/`| yes       | your machine, **not git** |

The script has no telemetry. It writes file paths to stdout but never prints transcript contents.

If you ever switch the LLM backend to a hosted API (Claude, OpenAI, etc.), audio will leave your machine — verify that's compatible with your patient consent and the Philippine Data Privacy Act (RA 10173) before doing so.
