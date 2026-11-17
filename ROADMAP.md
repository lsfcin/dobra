# Dobra — Roadmap
> Pending work only. Completed milestones are deleted (git is the history). Task IDs are permanent (D<milestone>.<n>).

## Status

Milestone D0 active — nothing started. Next task: D0.1.

## Inbox from paper

<!-- Paper sessions file experiment/code requests here as P→D lines. Coding sessions
     triage into milestones at session start. Format:
     - [ ] (from P<id>) one-line request — why the paper needs it -->

- [ ] (from P1/letta2026) hands-on letta-code session: `npm i -g @letta-ai/letta-code`,
  inspect MemFS layout + sleep-time subagent behavior — architecture recon before D1.3
  assembler design; write findings to eval/results/letta-recon.md
- [ ] (from P2) when E3 prereg is refined at D3.1: consider a Letta baseline arm
  (letta-code + same SLM) — related-work map says it's our closest neighbor; decide and
  record in EVAL.md E3 before any E3 run

## Backlog

- [ ] [advisor] Compare executor-plus-advisor with current model routing on matched tasks, measuring quality, retries, total tokens and quota consumption. Ref: refs/REFS.md [advisor] (Instagram lead).

- [ ] [respan-gateway] Assess Respan against existing provider integration: format/tool fidelity, streaming, fallback, observability and total cost; hedging can duplicate billed requests. Model-request routing is distinct from CLI session management. Ref: refs/REFS.md [Respan].

- [ ] [colibri-streaming] High priority: assess JustVugg/colibri disk-streaming inference; pin version/model, RAM/storage, first-response latency and tokens/s before any download. Compare a usable local configuration with the current baseline; retain the old unidentified GPU-runtime lead separately. Ref: refs/REFS.md [Colibri].

- [ ] [glm52-comparison] Compare GLM-5.2 on matched coding tasks with the same harness and budget; distinguish model quality, tool orchestration, hosted cost, local hardware and persistent memory. Share local-feasibility work with [colibri-streaming]. Ref: refs/REFS.md [GLM-5.2].

- [ ] [infinity-runtime] Assess Infinity yielding/hibernation and tool events against existing orchestration: persisted state, interruption recovery, session continuity, memory and bounded concurrency; waiting states are not simultaneous model inference. Ref: refs/REFS.md [Infinity].

- [ ] [taiga-s1] Assess the planner/tiny-executor split as a specialized baseline: training cost, state representation, completion checks and generalization limits; no evidence yet for general context-folding performance. Ref: refs/REFS.md [Taiga-S1].

- [ ] [qwen-modified] Assess whether the reported modified Qwen variant serves a concrete local task; verify provenance, licence, hardware fit and task quality against the original model. Ref: refs/REFS.md [Qwen modified].

- [ ] [omega-loop] Compare the reported planner/worker/check loop with existing routing and file-based orchestration; measure total cost, retries and accepted output quality. Ref: refs/REFS.md [Omega planner/worker loop].

- [ ] [openviking-context] Avaliar arquitetura do OpenViking em relação aos mecanismos de context-folding e memória do Dobra. Ref: refs/REFS.md [openviking-context].

- [ ] [context-evidence] Compare focused context, planning and meaningful verification with existing practice using measured local outcomes, not the creator's invented 100k quality cutoff. Ref: refs/REFS.md [context-evidence].

- [ ] [gpu-unlock] Assess whether any supported compute-bound workload transfers to our actual GPU and pipeline, keeping hardware, precision, power and whole-task results distinct. Ref: refs/REFS.md [gpu-unlock].

- [ ] [scaledown] Compare narrow classification/extraction/summarization baselines for correctness and cost, distinguishing schema validity, semantic accuracy, generation and hosted availability. Ref: refs/REFS.md [scaledown].

- [ ] [pstack] Assess completion criteria, invariants, behavior evidence and bounded parallel work against our existing workflow; separate portability and throughput claims from demonstrated facts. Ref: refs/REFS.md [pstack].

- [ ] [code-mode] Compare code-owned tool composition and filtered results with the current workflow, retaining direct calls where useful and requiring no Model Context Protocol adoption. Ref: refs/REFS.md [code-mode].

- [ ] [r-cli] Compare one matched coding task for quality, total tokens/cost, memory-service behavior and portability before changing a harness or provider. Ref: refs/REFS.md [r-cli].

- [ ] [model-continuity] Assess proportionate source/version continuity for models we actually use, checking licence, integrity and storage; do not infer a platform-wide ban or download this oversized derivative. Ref: refs/REFS.md [model-continuity].

- [ ] [unlimited-ocr] Compare one representative long document with our current extraction path for fidelity, reading order, runtime and supported memory; distinguish original and v2 results. Ref: refs/REFS.md [unlimited-ocr]. Include additional capture DfTb1XOGW_2; 100 pages is a source claim, not a guarantee.

- [ ] [airllm] Assess layer/expert streaming as a capacity-versus-latency baseline, retaining measured hardware, terabyte storage and time-per-token limits before any download decision. Ref: refs/REFS.md [airllm]. Include Kimi-in-C capture DcjlgleALHo; verify implementation and measured seconds/token before any download.

- [ ] [harness2] Compare controlled harness-improvement loops with existing orchestration, including model-call budget, held-out evaluation, judge bias and retained sandbox restrictions. Ref: refs/REFS.md [harness2].

- [ ] [deepinfer] Track the likely DeepInfer release as datacenter engineering and assess research relevance without presenting it as a consumer-laptop or independently benchmarked option. Ref: refs/REFS.md [deepinfer].

- [ ] [dependency-provenance] Assess how dependency-source verification and locked inventories cover the documented hallucinated-package risk; use the original benign case and reviewed study in teaching. Ref: refs/REFS.md [dependency-provenance].

- [ ] [unsloth-browser] Assess a bounded browser task with documented permission/network limits and memory headroom before selecting a local browser-agent setup. Ref: refs/REFS.md [unsloth-browser].

- [ ] [firecrawl] Compare Firecrawl with our existing fetch/search on representative difficult sources, recording coverage, deployment duties, access failures and total cost. Ref: refs/REFS.md [firecrawl]. Include Alexandria: compare source coverage, citation support, freshness, access failures and total cost; retrieval does not guarantee factual answers.

- [ ] [mesh-llm] Assess trusted-node availability, network cost and model compatibility; distinguish client routing from fitting a large model on this laptop. Ref: refs/REFS.md [mesh-llm].

- [ ] [strata-local] Record the supported memory/storage/context/quality tradeoffs and compare them with our laptop before selecting any local-inference trial. Ref: refs/REFS.md [strata-local].

- [ ] [qwenputer] Assess what Qwenputer demonstrates beyond external deterministic tools, retaining the merged-model limitation, selected-test scope and absent accepted-paper finding. Ref: refs/REFS.md [qwenputer].

- [ ] [mcptoon-context] Assess mcptoon discovery, on-demand schema retrieval and measured context cost against Dobra's folding invariant without changing configuration before comparison; refs/REFS.md, shared assessment in ../../core/ROADMAP.md.

- [ ] Assess OpenHarness (refs/REFS.md) and whether Dobra can bound the desktop hyperagent's cross-session context while preserving user decisions; application assessment in ../../core/ROADMAP.md (high priority, week).

- Chat REPL (`dobra chat`) — after D2
- opencode adapter — parked in IDEAS.md until kernel stable
- GAIA subset eval — D3 planning decides scope
- **SLM survey** (INBOX 2026-07-25) — serious, deep survey: which SLMs exist, for which contexts, benchmarks; and how to connect them efficiently (multi-SLM orchestration). Feeds D0.2 model inventory + the "how to connect" question is dobra's fold-kernel thesis. Ref: [local-ai](../../brain/goals/local-ai.md).
- **colibri assessment** (INBOX 2026-07-25, ref in refs/REFS.md) — investigate colibri (GPU LLM runtime) as a leaf backend candidate vs ollama; note tokens/s + VRAM fit on RTX 3050.
- **mipmaps as the fold model: fixed resolution levels instead of one folded summary** (INBOX 2026-08-20, Lucas: *"uma forma de pensar context folding é 'mipmaps' ou '3D model lod'. como texturas e modelos, arquivos de texto poderiam ter versões de resolução máxima + 2 níveis, médio, mínimo, e 1-parágrafo"*). Worth taking seriously because the analogy carries real machinery, not just a picture: mipmaps are **precomputed** (the fold is paid once per file, not per read), **selected by distance** (the caller picks a level from how relevant the file is to the current node), and **memory-bounded by construction** (the whole chain costs ~1.33× the finest level). Against it: mipmap levels are lossy in a *uniform* way, and prose is not — halving a texture is well-defined, halving a document is a judgement, so level *k* is a different artifact per file rather than a derivation. The question to answer first is whether fixed levels beat dobra's current on-demand fold on the fold invariant in SPECS.md, or only feel tidier. Second half of the capture is a factual question and it has an answer: **a session can read its own context size but not edit it** — `core/hooks/session/context-meter.py` reads the size the API reports and `core/tools/wos/session/context` attributes growth per file from transcripts, so measurement is available and zero-token, while manipulation is limited to what gets fed in and to compaction. Design against reading, not rewriting.
- **SSD-paged experts: does it change the leaf story?** (INBOX 2026-08-17, ref in refs/REFS.md) — a 2.78T MoE claimed to run in 8.24 GB by leaving ~93% of experts on SSD until a token routes to them. Find and name the actual engine first; the reel names none. Then answer one question for dobra: at 33 s/token the technique is useless for interactive leaves, but dobra's own premise is *time is not constrained* — so does expert paging widen which models can be a leaf on a 6 GB machine, or is the SSD requirement (1.56 TB) a worse constraint than the VRAM one it removes?

---

## Milestone D0 — Infrastructure ⬜ PENDING

### Problem
Nothing runs yet. Need venv, test gate, local models pulled and measured on the
reference GPU (RTX 3050 6GB), and the model inventory format the whole system reads.

### Checklist
- [ ] **D0.1 venv + verify gate.** Create `.venv` (python3.11+), `pip install pytest pyyaml
  requests`, write `pyproject.toml`, add a `Makefile` with a `verify-fast:` target running
  `.venv/bin/python -m pytest -q tests` (the pre-commit gate now discovers Makefile targets
  too, not just package.json — see code/VERIFY.md G1; no need for a fake package.json).
  Keep `tests/test_smoke.py` green.
  *Acceptance:* `make verify-fast` exits 0. Workspace pre-commit gate now enforces it.
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
