# Dobra — Eval Preregistration
> Benchmarks, metrics, and baselines are FIXED here before the code that runs them exists. Changing a prereg after results exist requires a DECISIONS.md entry explaining why.

## Rules

1. Each experiment (E<n>) is preregistered: dataset, metric, baselines, config — before implementation.
2. Every reported number carries provenance: run id under `runs/`, config hash, model tag, quant.
3. Judge-model bias: any LLM-judged metric uses a judge from a DIFFERENT family than the
   system under test, judge version pinned, and 20% of judgments human-audited (Lucas).
4. No cherry-picking: report all preregistered cells, including losses.

## E1 — Folding vs baselines on long-document summarization (D1.7)

- **Dataset:** 5 documents, 50k–300k chars each, mixed type (2 papers, 1 book chapter,
  1 technical doc, 1 transcript). Fixed list committed to `eval/e1-docs.md` before first run.
- **System:** dobra tiered fold, reference SLM (models.yaml `default`), 6GB VRAM laptop.
- **Baselines:** (a) same SLM single-shot with naive truncation to its context;
  (b) same SLM with plain map-reduce summarization (no verify, no tree); (c) Claude Sonnet
  single-shot (cloud reference, cost logged).
- **Metrics:** faithfulness (judge + human audit per rule 3), coverage of key claims
  (recall vs human-built claim list per doc), tokens total, wall time.
- **Hypothesis H1:** dobra ≥ baseline (b) on faithfulness+coverage; within 15% of (c) on coverage.

## E2 — Role ablation (D2.3)

- **Cells:** {verifier on/off} × {critic pair on/off} × {decomposer vs size-only branching}.
- **Dataset:** E1 docs + 5 new (no tuning on E1's five).
- **Metrics:** as E1 + role compliance rate (schema-valid outputs / calls).
- **Hypothesis H2:** verifier-on beats verifier-off on faithfulness by more than its token overhead ratio.

## E3 — External benchmarks (D3)

- **LongBench v2 subset** (exact task list frozen at D3.1 start, before any run) +
  comparison to published RLM-Qwen3-8B numbers where tasks overlap.
- **GAIA dev subset** for agentic; leaderboard-format logs kept from first run.
- **Curves:** quality vs wall-time vs VRAM ("compute inversion") — the paper's central figure.
- **Hypothesis H3:** ≤6GB local system closes ≥50% of the gap between its base SLM
  single-shot and frontier single-shot on the frozen subset.

## E4 — Per-role LoRA delta (D4)

- Prereg written at D4.1 once trace volume is known. Placeholder: same cells as E3,
  adapters on/off, no new tuning docs.
