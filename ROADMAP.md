# Dobra — Roadmap
> Pending work only. Completed milestones move to HISTORY.md. Task IDs are permanent (D<milestone>.<n>).

## Status

Milestone D0 active — nothing started. Next task: D0.1.

## Inbox from paper

<!-- Paper sessions file experiment/code requests here as P→D lines. Coding sessions
     triage into milestones at session start. Format:
     - [ ] (from P<id>) one-line request — why the paper needs it -->

## Backlog

- Chat REPL (`dobra chat`) — after D2
- opencode adapter — parked in IDEAS.md until kernel stable
- GAIA subset eval — D3 planning decides scope

---

## Milestone D0 — Infrastructure ⬜ PENDING

### Problem
Nothing runs yet. Need venv, test gate, local models pulled and measured on the
reference GPU (RTX 3050 6GB), and the model inventory format the whole system reads.

### Checklist
- [ ] **D0.1 venv + verify gate.** Create `.venv` (python3.11+), `pip install pytest pyyaml
  requests`, write `pyproject.toml`, add `package.json` with `"verify:fast": ".venv/bin/python -m pytest -q tests"`.
  Keep `tests/test_smoke.py` green.
  *Acceptance:* `npm run verify:fast` exits 0. Workspace pre-commit gate now enforces it.
- [ ] **D0.2 pull + microbench models.** `ollama pull` the 2 inventory models (check current
  best ≤4GB tags at https://ollama.com/library — expected: qwen3.5:4b class + phi-4-mini class;
  update `models.yaml` with real tags). Write `eval/microbench.py`: measure tokens/s,
  time-to-first-token, and JSON-schema compliance rate over 20 structured-output calls each.
  *Acceptance:* `.venv/bin/python eval/microbench.py` writes `eval/results/microbench.md` with a
  filled table for ≥2 models. File a P-task with the table (BRIDGE duty).
- [ ] **D0.3 inventory + router.** Implement `dobra/router/` reading `models.yaml`:
  `resolve(role_spec, inventory)` per SPECS interface. Role asks capabilities + max VRAM;
  router returns concrete model or raises `NoModelFits`.
  *Acceptance:* `pytest tests/test_router.py` — cases: match by capability, VRAM overflow,
  cloud disabled by default.

### Key Files
`models.yaml` (schema seeded), `dobra/router/`, `eval/microbench.py`, `tests/`.

---

## Milestone D1 — Fold Kernel MVP ⬜ PENDING

### Problem
The core loop doesn't exist: task tree on disk, folding-invariant context assembly,
tiered fold policy, verified folds, one end-to-end flow (summarize) running fully local.

### Solution
Port `core/flows/summarize.md` tiers from prose to `dobra/fold/tiered.py`. Tree nodes
per SPECS Domain Model. Assembler is the single choke point for the folding invariant.
Verifier role gates each fold. CLI drives it.

### Checklist
- [ ] **D1.1 backends.** `dobra/backends/base.py` (Protocol per SPECS) + `ollama.py`
  (HTTP :11434, retry ×2, timeout, schema-constrained output via `format`). Unit tests mock HTTP.
  *Acceptance:* `pytest tests/test_backends.py` green + 1 live smoke vs local ollama.
- [ ] **D1.2 tree.** `dobra/tree/`: create/load/walk `runs/<id>/` trees, node.yaml
  read/write, status transitions, `dobra tree <run>` ASCII rendering.
  *Acceptance:* `pytest tests/test_tree.py`; render matches fixture.
- [ ] **D1.3 assembler.** `dobra/context/assembler.py` per SPECS. Property test: assembled
  context NEVER contains sibling content; budget overflow triggers recursive fold call.
  *Acceptance:* `pytest tests/test_assembler.py` including the two invariant properties.
- [ ] **D1.4 tiered fold policy.** `dobra/fold/tiered.py`: direct (<8k chars) /
  windowed (8k–60k, window+overlap) / chunked (>60k, N child nodes). Thresholds in flow yaml.
  *Acceptance:* `pytest tests/test_fold_tiered.py` — tier selection + window math from
  core/flows/summarize.md examples.
- [ ] **D1.5 role cards + verifier loop.** Cards: worker, folder, verifier (≤40 lines each).
  `verified()` per SPECS: verifier judges output vs node acceptance; fail → retry with
  feedback appended; 2 fails → node status failed, parent notified.
  *Acceptance:* `pytest tests/test_verify.py` with scripted fake backend.
- [ ] **D1.6 E2E summarize.** `flows/summarize.yaml` + `dobra run summarize <file>` on the
  reference laptop, fully local, on a 100+ page PDF text. Trace complete, FOLD.md chain readable.
  *Acceptance:* run completes; `dobra tree` shows all nodes done; trace.jsonl valid JSONL;
  manual read of final FOLD.md is faithful (spot-check 3 claims against source).
- [ ] **D1.7 first measurement.** Run E2E on 5 long docs × {folding on, single-shot same
  model, naive-truncate}. Record per EVAL.md prereg. File P-task with results (BRIDGE duty).
  *Acceptance:* `eval/results/d1-summarize.md` table filled; provenance = run ids.

### Key Files
`dobra/backends/`, `dobra/tree/`, `dobra/context/assembler.py`, `dobra/fold/tiered.py`,
`dobra/roles/cards/*.md`, `dobra/verify/loop.py`, `dobra/cli.py`, `flows/summarize.yaml`.

### References
`core/flows/summarize.md` (tier spec), RLM paper repo github.com/alexzhang13/rlm
(REPL-as-environment tricks), SPECS.md interfaces.

---

## Milestone D2 — Roles & Decomposition ⬜ PENDING (coarse — refine at D1 exit)

- D2.1 decomposer role + `should_branch` for open tasks (not just size-triggered).
- D2.2 critic pair (pro/con) as optional verify stage; measure quality delta.
- D2.3 role ablation harness: same model, roles on/off (EVAL.md E2).
- D2.4 `dobra chat` terminal REPL (thin: each turn = new node under session root).

## Milestone D3 — External Benchmarks ⬜ PENDING (coarse)

- D3.1 LongBench v2 subset harness + baselines per EVAL.md E3; compare to published RLM numbers.
- D3.2 GAIA dev subset; leaderboard-format logs from day one.
- D3.3 quality-vs-time-vs-VRAM tradeoff curves (the "compute inversion" plot for the paper).

## Milestone D4 — Per-Role LoRA ⬜ PENDING (coarse)

- D4.1 trace→dataset exporter (traces are already the format — validate coverage).
- D4.2 LoRA per role (worker, folder) via unsloth; train cloud or local, infer local.
- D4.3 re-run D3 evals with adapters; delta table.
