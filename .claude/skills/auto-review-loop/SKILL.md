---
name: auto-review-loop
description: "自动执行数轮：review -> fix -> re-review"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read, Write, Skill, mcp__codex__codex, mcp__codex__codex-reply
---

# Auto Review Loop

Given an experiment directory with preliminary writeup or results:
1. Trigger `/llm-review` and wait for scores.
2. If score < 5, parse the weaknesses.
3. Automatically decide to modify the code or the paper.
4. Execute `/paper-compile` (if paper was modified) or `/run-experiment` (if code was modified).
5. Do this for MAX_ROUNDS = 4. Stop when score >= 5.
6. Persist status to `experiments/plans/RESEARCH_STATE.json` after every round.
