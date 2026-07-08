# Dobra — Ideas Parking Lot
> Anti-scatter valve. Mid-task ideas land here as one-liners, NEVER in code. Triage: promote to ROADMAP Backlog, send to paper inbox, or delete. Review at each milestone exit.

- opencode adapter: dobra as opencode "agent" backend so its TUI becomes our chat UI — revisit after D2.4 REPL exists
- weft (github.com/WeaveMindAI/weft): revisit after their Aug 2026 mvp release — typed ports + collapsible groups + durable resume map to our tree; maybe compile flows/*.yaml → weft
- mechanism-design task allocation: roles bid for nodes given budget (Lucas's field — could be paper #2)
- workspace handoff-at-N%-context hook = folding applied to Claude Code sessions (INBOX idea 2026-06) — dobra tree could BE the handoff format
- RIG-style deterministic repo graph (arXiv 2601.10112) as a role's attachment for code tasks (D3+)
- model swap scheduling: order tree execution to minimize ollama model loads on 6GB (one resident model)
- FOLD.md quality self-play: folder writes, verifier scores, keep best-of-k — trace gold for D4 LoRA
- sleep-time defrag (letta/sleeptime2025 idea, our axis): idle-time role that re-folds stale FOLD.md chains, merges duplicates across sibling folds — AFTER kernel stable, measure before adopting
- git-versioned runs/ (letta MemFS convergence): commit per fold → free undo/diff of agent memory; check fs overhead first
- kimi report's inverse tiering (big manager + small worker) as an E2/E3 comparison arm — dobra's stance is code-manager; the LLM-manager arm would quantify what code replaces
- U-Fold / AgentFold / FoldAct / ACON policy variants as pluggable FoldPolicy implementations for E2-style comparison
- visualize context trees folding/unfolding — a dobra viz of the fold structure animating (INBOX 2026-07)
- mine the Fable-5 system-prompt leak for context-folding insights → apply to dobra (INBOX 2026-07); links in refs/REFS.md
- model-cost router: score cost × quality per subtask, pick best model per leaf; keep a live benchmark via OpenRouter API (INBOX 2026-07)
