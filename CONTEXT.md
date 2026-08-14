# Dobra
> Context folding + small local models: task-tree runner where SLMs do leaf work under folded context. Paper twin: `academy/papers/2027-ICLR-dobra`.
> goal: [local-ai](../../brain/goals/local-ai.md)

## Overview

Dobra ("fold", PT) tests one claim: consumer-grade small models (≤6GB VRAM), orchestrated
by explicit context folding, can match frontier LLMs on long-horizon tasks when time is
not constrained. Orchestration lives in Python code, not in model prompts — models only
do leaf-level cognition. See [SPECS.md](SPECS.md) for the constitution.

**Kinship with `/loops`** (`core/flows/craft/craft.md`): dobra's task-tree runner
is the *parallel-fan-out* primitive that /loops lacks (cross-repo loops parallelize, same-
repo loops fight, per the loops `## Field Practice` notes). /loops uses one Carry block per
sequential chain; dobra uses folded task-tree context — Voyager's "lifelong learning"
vision (Wang et al. 2023, <https://arxiv.org/abs/2305.16291>) made durable via files.
LATM's two-tier cost-spreading (Cai et al. 2023,
<https://arxiv.org/abs/2305.17126>) applies to both: frontier-tier orchestrators,
SLM-tier leaves. The two projects share a thesis — **the artifact is the memory** — and
should converge on a shared Carry-block / folded-context convention. See
`core/flows/craft/prior-art.md` for the citation chain shared by both.


## Session Protocol — mandatory for every agent session

**Start:**
1. Read [SPECS.md](SPECS.md) — architecture constitution. Never edit code that contradicts it.
2. Read [ROADMAP.md](ROADMAP.md) — Status line + active milestone only. Ignore later milestones.
3. Session touches a design decision or produces a measurable result? Read [SPECS.md](SPECS.md) § Twin and do its duties.

**Work:**
- One ROADMAP task per session (trivial fixes exempt). Task is done only when its
  acceptance command passes — run it, paste output, then check the box.
- New idea mid-task → one line in [IDEAS.md](IDEAS.md), then back to task. Never implement it now.
- Architecture change → new entry in [DECISIONS.md](DECISIONS.md) FIRST (check `invalidated-if`
  of existing decisions), then code.
- Phase gate: milestone N+1 tasks are LOCKED while milestone N has unchecked acceptance boxes.

**End:**
- Update ROADMAP checkboxes; delete finished milestones (git is the history).
- If a result is paper-relevant (any measured number, any decision with literature basis) →
  SPECS.md § Twin duty: file a P-task in the paper ROADMAP inbox.
- `/handoff` with next task id.

<!-- routing:start -->
## Routing

| Subdirectory | Description |
|--------------|-------------|
| [`refs/`](refs/CONTEXT.md) | Captured references for dobra — tier-1 links in [REFS.md](refs/REFS.md); promote |

| File | Interface | Description |
|------|-----------|-------------|
| [`dobra/__init__.py`](dobra/__init__.py) | [`dobra/__init__.pyi`](dobra/__init__.pyi) | **facade** — Dobra package facade — public API grows here as kernel modules land (SPECS.md interfaces). |
| [`BUGS.md`](BUGS.md) | — | Dobra — Known Bugs |
| [`DECISIONS.md`](DECISIONS.md) | — | Dobra — Decisions |
| [`EVAL.md`](EVAL.md) | — | Dobra — Eval Preregistration |
| [`IDEAS.md`](IDEAS.md) | — | Dobra — Ideas Parking Lot |
| [`README.md`](README.md) | — | Dobra |
| [`ROADMAP.md`](ROADMAP.md) | — | Dobra — Roadmap |
| [`SETUP.md`](SETUP.md) | — | Dobra — Dev Setup |
| [`SPECS.md`](SPECS.md) | — | Dobra — Specs |
| [`models.yaml`](models.yaml) | — | Model inventory — the ONLY source of model availability (SPECS principle 6). Edit per machine; router adapts. |
| [`tests/test_smoke.py`](tests/test_smoke.py) | [`tests/test_smoke.pyi`](tests/test_smoke.pyi) | Smoke test — proves the verify:fast gate wiring; real suites arrive with each D-task. |
<!-- routing:end -->
