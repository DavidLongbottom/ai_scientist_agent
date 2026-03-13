---
name: research-pipeline
description: "端到端自动化科研全流程。从研究方向直达论文投稿 PDF。"
argument-hint: [research-direction]
allowed-tools: Bash(*), Read, Skill, mcp__codex__codex
---

# Research Pipeline

Orchestrates everything:

1. `/idea-discovery` for the user's string direction.
2. The agent pauses to ask the user which idea (1, 2, or 3) they prefer.
3. Call `/tree-search` on the chosen idea.
4. Call `/plot-aggregation` safely checking memory beforehand.
5. Apply `/auto-review-loop` (LLM-review max 4 rounds).
6. Perform `/paper-writing`.
7. Summarize final outcome inside `experiments/plans/FINAL_REPORT.md`.

## Error Recovery & Fallbacks
- **Step Failure:** If any script (`tree-search`, `paper-writing`, etc.) crashes completely, DO NOT abort the pipeline immediately. Review the trace, propose a fix, and attempt a retry up to 2 times.
- **Resource OOM (Out of Memory):** If the experiment fails with CUDA OOM or RAM limits, adjust `bfts_config.yaml` to halve batch sizes or worker counts, and retry at least once.
- **API Errors:** Exponentially back off locally or try switching a model in `settings.json` or `bfts_config.yaml` if an API failure is persistent.
