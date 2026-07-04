# Dobra
> Context folding + small local models: task-tree runner where SLMs do leaf work under folded context. Paper twin: `academy/papers/2027-ICLR-dobra`.

## Overview

Dobra ("fold", PT) tests one claim: consumer-grade small models (≤6GB VRAM), orchestrated
by explicit context folding, can match frontier LLMs on long-horizon tasks when time is
not constrained. Orchestration lives in Python code, not in model prompts — models only
do leaf-level cognition. See [SPECS.md](SPECS.md) for the constitution.

## Session Protocol — mandatory for every agent session

**Start:**
1. Read [SPECS.md](SPECS.md) — architecture constitution. Never edit code that contradicts it.
2. Read [ROADMAP.md](ROADMAP.md) — Status line + active milestone only. Ignore later milestones.
3. Session touches a design decision or produces a measurable result? Read [BRIDGE.md](BRIDGE.md) and do its duties.

**Work:**
- One ROADMAP task per session (trivial fixes exempt). Task is done only when its
  acceptance command passes — run it, paste output, then check the box.
- New idea mid-task → one line in [IDEAS.md](IDEAS.md), then back to task. Never implement it now.
- Architecture change → new entry in [DECISIONS.md](DECISIONS.md) FIRST (check `invalidated-if`
  of existing decisions), then code.
- Phase gate: milestone N+1 tasks are LOCKED while milestone N has unchecked acceptance boxes.

**End:**
- Update ROADMAP checkboxes; move finished milestones to HISTORY.md.
- If a result is paper-relevant (any measured number, any decision with literature basis) →
  BRIDGE.md duty: file a P-task in the paper ROADMAP inbox.
- `/handoff` with next task id.

<!-- routing:start -->
## Routing

| File | Interface | API | Description |
|------|-----------|-----|-------------|
| [`dobra/__init__.py`](dobra/__init__.py) | [`dobra/__init__.pyi`](dobra/__init__.pyi) | — | **facade** — Dobra package facade — public API grows here as kernel modules land (SPECS.md interfaces). |
| [`BRIDGE.md`](BRIDGE.md) | — | — | Dobra ↔ Paper Bridge (code side) |
| [`DECISIONS.md`](DECISIONS.md) | — | — | Dobra — Decisions |
| [`EVAL.md`](EVAL.md) | — | — | Dobra — Eval Preregistration |
| [`HISTORY.md`](HISTORY.md) | — | — | Dobra — History |
| [`IDEAS.md`](IDEAS.md) | — | — | Dobra — Ideas Parking Lot |
| [`KNOWN-BUGS.md`](KNOWN-BUGS.md) | — | — | Dobra — Known Bugs |
| [`README.md`](README.md) | — | — | Dobra |
| [`ROADMAP.md`](ROADMAP.md) | — | — | Dobra — Roadmap |
| [`SETUP.md`](SETUP.md) | — | — | Dobra — Dev Setup |
| [`SPECS.md`](SPECS.md) | — | — | Dobra — Specs |
| [`models.yaml`](models.yaml) | — | — | Model inventory — the ONLY source of model availability (SPECS principle 6). Edit per machine; router adapts. |
| [`tests/test_smoke.py`](tests/test_smoke.py) | [`tests/test_smoke.pyi`](tests/test_smoke.pyi) | `test_package_imports` | Smoke test — proves the verify:fast gate wiring; real suites arrive with each D-task. |
<!-- routing:end -->
