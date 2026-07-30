# Dobra — Dev Setup
> Zero to running on a clean machine. Reference platform: RTX 3050 Laptop 6GB VRAM, 14GB RAM, Linux.

## Prerequisites

- Python 3.11+
- [ollama](https://ollama.com) ≥0.9 serving on `localhost:11434` (`ollama serve`)
- Node ≥18 (only for `npm run verify:fast` — the workspace commit gate)
- ~8GB disk for model weights

## Install

```bash
cd code/dobra
python3 -m venv .venv
.venv/bin/pip install pytest pyyaml requests   # pyproject.toml arrives with D0.1
ollama pull <tags in models.yaml>              # real tags fixed by D0.2 microbench
```

## Environment Variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `DOBRA_OLLAMA_URL` | no | `http://localhost:11434` | override backend endpoint |
| `DOBRA_RUNS_DIR` | no | `./runs` | where task trees are written |

No API keys: cloud backends stay disabled unless `models.yaml § cloud.enabled: true`.

## Run

```bash
.venv/bin/dobra run summarize <file>    # after D1.6
.venv/bin/dobra tree runs/<run-id>      # inspect any run
```

## Test

```bash
.venv/bin/python -m pytest -q tests
```

## Verification Contract

```bash
npm run verify:fast   # = pytest -q tests; wired into workspace pre-commit gate at D0.1
```

Regression specs for BUGS fixes: `tests/b<N>-*.py` (workspace known-bugs-gate).
