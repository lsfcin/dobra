# References
> Tier-1 capture: one line per ref. Promote to `<slug>.yaml` when a ref earns real study.

## Context folding + agents
- [CL4R1T4S — Fable-5 system-prompt leak](https://github.com/elder-plinius/CL4R1T4S) — mine for context-folding insights
- [Fable-5 leak coverage](https://memeburn.com/claude-fable-5-system-prompt-leak-shakes-ai-industry/) · [analysis](https://www.ayautomate.com/blog/claude-fable-5-system-prompt-leak)
- [arxiv 2601.10112](https://arxiv.org/pdf/2601.10112) — graphs + context folding for agents
- [arxiv 2602.11988](https://arxiv.org/pdf/2602.11988) — graphs + context folding for agents
- [openreview 91jL62CQF1](https://openreview.net/pdf?id=91jL62CQF1) — graphs + context folding for agents
- [openreview JaLXQnA2wi](https://openreview.net/pdf?id=JaLXQnA2wi) — graphs + context folding for agents

- [vinisousabr — four free Claude Code plugins](https://www.instagram.com/p/DbiVrYngBiV/) — [src: web:instagram.com]
  **Headroom** (compresses the input), **Graphify** (codebase → knowledge graph), **CodeBurn** (shows where tokens
  burn), **Ponytail** (claims +50% output efficiency without losing precision), pitched as four angles on one problem:
  compression, memory, visibility, efficiency. Lucas: *"headroom parece ressoar com a ideia que dei de mipmaps e 3d
  model lod pra contextos de llm"* (INBOX 2026-08-21) — idea logged in [IDEAS.md](../IDEAS.md). DM-gated post, so each
  plugin has to be found by name; Graphify also touches the workspace's own knowledge-graph question.

## SLM runtimes / serving
- colibri — GPU runtime for running LLMs locally, to investigate as an SLM-leaf backend (INBOX 2026-07-25). Assessment task: dobra ROADMAP Backlog
- [Stride Josh — 2.78T params on one CPU](https://www.instagram.com/reel/DcHhBlHBRmU/) — [src: web:instagram.com] a 2.78T-parameter MoE run on a single CPU in **8.24 GB resident**, byte-identical output, with a 176 KB C engine and no PyTorch. The mechanism is the point: ~93% of the model is experts that never load, staying on SSD and read only when a token routes to them (5.5 TB at full precision → 8.24 GB). Costs are brutal and stated — **33 seconds per token**, a 1.56 TB SSD, Linux only — and the post calls it a proof rather than a product: *"the memory wall was never about model size, it's about which bytes you keep."* Captured 2026-08-17. Directly adjacent to dobra's thesis that orchestration, not model size, is the lever — assessment task in `ROADMAP.md` Backlog. Unverified: one YouTuber reportedly never generated a token for lack of disk, so treat the byte-identical claim as unconfirmed until the engine is found and named.
- "Soup" — [reel](https://www.instagram.com/reel/Db-5SSwJHls/) by 100xEngineers, [src: web:instagram.com]. Claims to collapse LLM fine-tuning into one YAML config plus one command, replacing rented cloud GPUs and custom training scripts. Lucas (INBOX 2026-08-16): *"pode ser especialmente interessante pra gente em todos os casos em que pensamos em slms e dsls, texpace, spacemantics, dobra..."* — so it is cross-project: dobra's SLM leaves, and the spacemantics/texpace DSL work. **The GitHub link is DM-gated** (*"Comment 'Soup' and I'll send you the GitHub link"*), so the repo has to be found independently before any assessment. Config-file-shaped fine-tuning is the claim to verify, not the branding.
