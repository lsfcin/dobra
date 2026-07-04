# Dobra — Specs
> Architecture constitution: folding invariant, domain model, interfaces. Decision log lives in DECISIONS.md.

## Core Principles

1. **Orchestration in code, cognition in models.** Python decides structure (branch, fold,
   retry, route); models only transform bounded text. A 4B model must never be asked to
   follow a long protocol.
2. **Filesystem is the runtime.** The task tree is a folder tree on disk. Every run is
   inspectable with `ls` and `cat`, resumable after crash, diffable, human-editable mid-run.
3. **The folding invariant** (below) is never violated, by any role, in any flow.
4. **Trace everything.** Every model call logs to `trace.jsonl`. Traces are future LoRA
   training data — losing them loses phase D4.
5. **Verified folds only.** A fold is accepted only after a verifier pass. Errors compound
   across steps; gates are the countermeasure.
6. **Adapt to declared models.** `models.yaml` is the only source of model availability.
   No hardcoded model names outside it.
7. **Small files, small functions.** Workspace R1-R6 + 200-line hard limit apply.

## The Folding Invariant

Context assembled for any model call at node N contains, at most:

```
system      = role card of N's role
lineage     = FOLD.md of each ancestor, root → parent (already-folded summaries only)
goal        = N's node.yaml goal + acceptance
attachments = files explicitly listed in N's node.yaml inputs
```

NEVER: sibling internals, ancestor raw transcripts, unrelated tree branches, whole
documents when a fold of them exists. If assembled context exceeds N's token budget,
the assembler folds the largest attachment first (recursive folding), never truncates silently.

## Architecture Overview

```
flows/*.yaml          declarative flow defs (which roles, which fold policy, budgets)
      │
   runner ──► tree (runs/<id>/… node.yaml, FOLD.md, trace.jsonl per node)
      │            │
      │        context assembler (folding invariant enforced here, single choke point)
      │            │
   roles (cards) ──► backend router ──► backends (ollama | openai-compat)
      │
   verifier loop (accept / retry-with-feedback / escalate)
```

## Domain Model

| Concept | Is | Lives at |
|---------|-----|----------|
| Node | one task: goal, status, role, budget, inputs | `runs/<run>/…/node.yaml` |
| Fold | summary that survives a node's completion | `FOLD.md` next to node.yaml |
| Role | prompt card + output contract + model needs | `dobra/roles/cards/<role>.md` + `.yaml` |
| Flow | declarative recipe: steps, roles, policies | `flows/<name>.yaml` |
| Fold policy | branch/fold strategy (tiered, windowed, chunked) | `dobra/fold/` |
| Backend | `generate()` provider | `dobra/backends/` |
| Trace event | one model call record | `trace.jsonl` (JSONL, append-only) |

**node.yaml** required keys: `id`, `goal`, `role`, `status` (pending|running|done|failed),
`budget_tokens`, `inputs` (list of paths), `acceptance` (how verifier judges output).

**trace.jsonl** event keys: `ts`, `node`, `role`, `model`, `backend`, `prompt_tokens`,
`output_tokens`, `ms`, `config_hash`, `verdict` (verifier outcome, when applicable).

## Module Interfaces (implement exactly; extend via DECISIONS.md)

```python
# dobra/backends/base.py
class Backend(Protocol):
    def generate(self, messages: list[Message], schema: dict | None = None,
                 max_tokens: int = 1024) -> GenResult: ...

# dobra/router/router.py
def resolve(role: RoleSpec, inventory: Inventory) -> ModelChoice: ...

# dobra/context/assembler.py
def assemble(node: Node, tree: Tree, budget: int) -> list[Message]: ...
    # sole implementation of the folding invariant

# dobra/fold/base.py
class FoldPolicy(Protocol):
    def should_branch(self, node: Node, content_chars: int) -> BranchPlan | None: ...
    def fold(self, node: Node, output: str) -> str: ...   # returns FOLD.md content

# dobra/verify/loop.py
def verified(node: Node, output: str, max_retries: int = 2) -> VerifyResult: ...
```

Initial roles (cards in `dobra/roles/cards/`): `decomposer`, `worker`, `folder`,
`verifier`, `critic`. Cards are ≤40 lines each — SLMs get short, concrete instructions
with one output contract, never multi-step protocols.

## Relationship to Neighbors

- `code/flows/` — conceptual donor (slots-as-requirements, typed payloads, trace).
  Dobra stays standalone; see DECISIONS.md AD-1 for the merge-back condition.
- `core/flows/summarize.md` — prose spec of the tiered fold policy; port it as code
  (D1.4), do not interpret it with a model.
- Paper twin `academy/papers/2026-WIP-dobra` — every measured number there must trace to
  a `runs/` artifact here. Cross-duties: [BRIDGE.md](BRIDGE.md).

## Conventions

- Python 3.11+, typed, `.venv` local to project. R1-R6 style (workspace SPECS).
- Runs are immutable after completion; re-runs get new run ids (timestamped slug).
- No network calls except through `Backend` implementations.
- Every module folder has `__init__.py` facade; cross-module imports only via facades
  (workspace hook enforces).
- Benchmark configs and results: `eval/` (prereg in EVAL.md), raw outputs under `runs/`.
