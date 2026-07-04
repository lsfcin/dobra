# Dobra
> Context folding + small local models: match frontier LLMs on long-horizon tasks with a 6GB-VRAM laptop, trading time for capability.

## What it does

- Runs tasks as a **task tree on the filesystem** — each node a folder with a goal,
  a folded summary (`FOLD.md`), and a full trace.
- **Folds context**: workers see only ancestor summaries + their own inputs, never the
  whole history. Active context stays small no matter how long the task runs.
- **Small models only** (≤6GB VRAM by default): orchestration lives in Python, models do
  bounded leaf work — the inversion that makes SLMs viable ([NVIDIA position, arXiv 2506.02153](https://arxiv.org/abs/2506.02153)).
- **Verified folds**: every summary passes a verifier gate before entering parent context.
- **Adapts to your hardware**: declare models in `models.yaml`; the router does the rest.
- Twin research project: methodology, prereg, and literature in `academy/papers/2026-WIP-dobra`.

## Architecture

See [SPECS.md](SPECS.md) — the folding invariant is the design center.

## Quickstart

```bash
# prerequisites: python3.11+, ollama serving on :11434
python3 -m venv .venv && .venv/bin/pip install -e .
ollama pull <model-tag-from-models.yaml>
.venv/bin/dobra run summarize path/to/long-document.pdf   # available after D1.6
```

## Status

Milestone D0 (infrastructure) — see [ROADMAP.md](ROADMAP.md).

## License

TBD.

---
[CONTEXT.md](CONTEXT.md) · [SPECS.md](SPECS.md) · [ROADMAP.md](ROADMAP.md) · [SETUP.md](SETUP.md) · [EVAL.md](EVAL.md) · [DECISIONS.md](DECISIONS.md) · [BRIDGE.md](BRIDGE.md)
