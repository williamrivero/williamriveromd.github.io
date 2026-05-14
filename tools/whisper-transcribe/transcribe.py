#!/usr/bin/env python3
"""
Local Taglish consultation transcription pipeline.

Audio file -> Whisper (large-v3) -> raw transcript
                                 -> Ollama (SOAP note draft)
                                 -> Ollama (patient-facing summary)

Everything stays on this machine. No network calls except to local Ollama.
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path


DEFAULT_OUTPUT_ROOT = Path.home() / "clinical-transcripts" / "output"
DEFAULT_WHISPER_MODEL = "large-v3"
DEFAULT_OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.1:8b")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
PROMPTS_DIR = Path(__file__).parent / "prompts"


def transcribe_audio(audio_path: Path, model_name: str) -> str:
    import whisper  # imported lazily so --help works without whisper installed

    print(f"[whisper] loading model '{model_name}' (first run downloads ~3 GB)...")
    model = whisper.load_model(model_name)

    print(f"[whisper] transcribing {audio_path.name} (Taglish auto-detect)...")
    t0 = time.time()
    # language=None lets Whisper detect per-segment; verbose=False keeps output clean
    result = model.transcribe(
        str(audio_path),
        language=None,
        task="transcribe",
        verbose=False,
        fp16=False,  # safer default; flip to True if you have CUDA
    )
    print(f"[whisper] done in {time.time() - t0:.1f}s")
    return result["text"].strip()


def call_ollama(prompt: str, model: str) -> str:
    payload = json.dumps(
        {"model": model, "prompt": prompt, "stream": False}
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        sys.exit(
            f"[ollama] failed to reach {OLLAMA_URL}: {e}\n"
            "Is Ollama running? Try `ollama serve` in another terminal."
        )
    return body.get("response", "").strip()


def render_prompt(template_path: Path, transcript: str) -> str:
    template = template_path.read_text(encoding="utf-8")
    return template.replace("{TRANSCRIPT}", transcript)


def write_output(out_dir: Path, name: str, content: str) -> Path:
    path = out_dir / name
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe Taglish consultation audio and draft SOAP + patient summary."
    )
    parser.add_argument("audio", type=Path, help="Path to audio file (m4a/mp3/wav/etc.)")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=f"Output folder (default: {DEFAULT_OUTPUT_ROOT}/<audio-basename>/)",
    )
    parser.add_argument(
        "--whisper-model",
        default=DEFAULT_WHISPER_MODEL,
        help=f"Whisper model size (default: {DEFAULT_WHISPER_MODEL})",
    )
    parser.add_argument(
        "--ollama-model",
        default=DEFAULT_OLLAMA_MODEL,
        help=f"Ollama model tag (default: {DEFAULT_OLLAMA_MODEL})",
    )
    parser.add_argument(
        "--skip-llm",
        action="store_true",
        help="Only produce raw transcript; skip SOAP note and patient summary.",
    )
    args = parser.parse_args()

    if not args.audio.exists():
        sys.exit(f"Audio file not found: {args.audio}")

    out_dir = args.output_dir or (DEFAULT_OUTPUT_ROOT / args.audio.stem)
    out_dir.mkdir(parents=True, exist_ok=True)

    transcript = transcribe_audio(args.audio, args.whisper_model)
    transcript_path = write_output(out_dir, "raw_transcript.txt", transcript)
    print(f"[out] {transcript_path}")

    if args.skip_llm:
        return 0

    print(f"[ollama] generating SOAP note with {args.ollama_model}...")
    soap_prompt = render_prompt(PROMPTS_DIR / "soap_note.txt", transcript)
    soap = call_ollama(soap_prompt, args.ollama_model)
    soap_path = write_output(out_dir, "soap_note.md", soap)
    print(f"[out] {soap_path}")

    print(f"[ollama] generating patient summary...")
    summary_prompt = render_prompt(PROMPTS_DIR / "patient_summary.txt", transcript)
    summary = call_ollama(summary_prompt, args.ollama_model)
    summary_path = write_output(out_dir, "patient_summary.md", summary)
    print(f"[out] {summary_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
