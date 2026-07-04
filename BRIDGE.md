# Dobra ↔ Paper Bridge (code side)
> Cross-duties binding this repo to `academy/papers/2027-ICLR-dobra`. The paper's mirror copy of these duties lives there as BRIDGE.md. Task IDs: D* = code, P* = paper.

## Why this file

Two sessions types work on dobra: coding sessions (here) and paper sessions (paper repo).
Each is REQUIRED to feed the other. This is what keeps the project simultaneously an
engineering artifact and a sound academic contribution.

## Duties of a CODING session (read at session start, act at session end)

1. **Results flow to paper.** Produced any measured number (microbench, eval, ablation)?
   → Append to paper `ROADMAP.md § Inbox from code`:
   `- [ ] (from D<task>) <one-line result> — runs/<id>, eval/results/<file>`.
2. **Decisions check literature.** Before writing a DECISIONS.md entry, check the paper's
   `reviews/` folder: does a reviewed paper already answer this? Cite the review key in the
   decision's Basis line.
3. **New SOTA sighting.** Found a relevant paper while coding (searching APIs, error hunting)?
   → Add a stub `reviews/<key>.yaml` in the paper repo with url + one-line relevance. Paper
   session completes it.
4. **Claims need evidence.** About to claim something works in README/HISTORY? The claim must
   name a run id or test. Unproven claims are written as "TODO: measure (→ E<n>)".

## Duties of a PAPER session (mirror — enforced by the paper-side BRIDGE.md)

1. Scan code `HISTORY.md` + `DECISIONS.md` since last paper session; file experiment gaps
   as D-tasks in code `ROADMAP.md § Inbox from paper`.
2. Audit DECISIONS.md `invalidated-if` triggers against newly reviewed literature; if fired,
   file a D-task quoting the trigger.
3. Keep `reviews/` current (complete stubs left by coding sessions; monthly `/research watch` sweep).
4. Never write a number the code repo can't trace to `runs/` — EVAL.md rules bind the paper too.

## Shared invariants

- EVAL.md (code repo) is the single prereg registry. The paper cites it; it cites the paper's reviews.
- A P-task or D-task filed via bridge always names its origin task id.
- Bridge inboxes are triaged at the START of the receiving side's next session — never left >2 sessions.
