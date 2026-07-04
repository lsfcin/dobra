# Dobra — Decisions
> Append-only decision log. Every entry has literature basis + invalidated-if trigger. Paper sessions audit these against new literature (BRIDGE duty).

Format: `AD-N — title · date · decision · basis · invalidated-if`.
Never delete; supersede with a new entry referencing the old.

---

## AD-1 — Standalone project, not a code/flows extension · 2026-07-03

**Decision:** Dobra is its own repo/kernel. `code/flows` remains conceptual donor
(slots-as-requirements, typed payload kinds, trace discipline).

**Basis:** flows is a generic orchestration engine (V1 mid-flight, UI/voice scope);
dobra needs an opinionated folding kernel where the folding invariant is THE design
center. Generality now = drift risk (user: "the road it took is maybe not so good").

**Invalidated-if:** dobra's kernel stabilizes (D2 done) AND flows V1 lands a stable
component API — then evaluate exposing dobra as a flows component instead of a parallel
engine. Revisit at D3 planning.

## AD-2 — Task tree lives on the filesystem · 2026-07-03

**Decision:** Nodes = folders; state = node.yaml + FOLD.md + trace.jsonl. No DB.

**Basis:** Van Clief (arXiv 2603.16021) folder-structure-as-architecture; workspace
CONTEXT.md idiom proven in daily use; explainability + crash-resume + human mid-run
edits for free. HI research angle (human repairs the tree) needs human-readable state.

**Invalidated-if:** measured tree-walk overhead >5% of run wall time, or concurrent
node execution needs locking the fs can't give cleanly. Then: keep fs as the VIEW,
add sqlite as index — never replace the readable artifacts.

## AD-3 — Ollama first backend; everything else via OpenAI-compat · 2026-07-03

**Decision:** `OllamaBackend` is the reference implementation; second backend speaks
OpenAI-compatible HTTP (covers llama.cpp server, vLLM, LM Studio, cloud proxies).

**Basis:** ollama already installed on reference machine; simplest pull/swap UX for
"users declare what they have"; OpenAI-compat covers the rest of the local ecosystem.

**Invalidated-if:** microbench (D0.2) shows ollama overhead vs llama-server >20%
tokens/s on the 3050 — then llama-server becomes reference, ollama stays as pull/UX layer.

## AD-4 — Prompted folding first, trained folding later · 2026-07-03

**Decision:** Phases D0–D3 use off-the-shelf SLMs with coded orchestration + prompted
role cards. LoRA per role only in D4, on our own traces. No RL (FoldGRPO-style) planned.

**Basis:** RLM (arXiv 2512.24601) shows prompted recursion already lifts Qwen3-8B ~28%;
ByteDance Context-Folding (2510.11967) needed RL but folded INSIDE the model — we fold
in code, so the model's job stays small. Cheapest path to falsifiable results first.

**Invalidated-if:** D1.7/D3.1 show role compliance (schema-valid, on-task outputs) below
~85% for the 4B class — then move LoRA forward to D2.5, before external benchmarks.

## AD-5 — Verifier gate on every fold · 2026-07-03

**Decision:** No fold enters an ancestor's context without passing the verifier role
(retry ×2 with feedback, then fail the node).

**Basis:** error compounding is the #1 failure mode of step-decomposed pipelines
(10 steps × 95% = 60%). Workspace verify culture (VERIFY.md) applies the same lesson.

**Invalidated-if:** measured verifier overhead >40% of tokens with <5% quality delta
on E1 (EVAL.md) — then verifier becomes sampling-based (verify p% of folds) instead of always-on.
