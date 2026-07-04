# Dobra — Ideas Parking Lot
> Anti-scatter valve. Mid-task ideas land here as one-liners, NEVER in code. Triage: promote to ROADMAP Backlog, send to paper inbox, or delete. Review at each milestone exit.

- opencode adapter: dobra as opencode "agent" backend so its TUI becomes our chat UI — revisit after D2.4 REPL exists
- weft (github.com/WeaveMindAI/weft): revisit after their Aug 2026 mvp release — typed ports + collapsible groups + durable resume map to our tree; maybe compile flows/*.yaml → weft
- mechanism-design task allocation: roles bid for nodes given budget (Lucas's field — could be paper #2)
- workspace handoff-at-N%-context hook = folding applied to Claude Code sessions (INBOX idea 2026-06) — dobra tree could BE the handoff format
- RIG-style deterministic repo graph (arXiv 2601.10112) as a role's attachment for code tasks (D3+)
- model swap scheduling: order tree execution to minimize ollama model loads on 6GB (one resident model)
- FOLD.md quality self-play: folder writes, verifier scores, keep best-of-k — trace gold for D4 LoRA
- U-Fold / AgentFold / FoldAct / ACON policy variants as pluggable FoldPolicy implementations for E2-style comparison
