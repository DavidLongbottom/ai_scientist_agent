---
name: gather-citations
description: "收集该想法所需的文献引用"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read
---

# Gather Citations Skill

Collect correct academic references using Semantic Scholar.

1. Run:
   ```bash
   python scripts/run_writeup.py --experiment-dir "$ARGUMENTS" --citations-only --output-json
   ```
2. The citations will be prepared inside the experiment directory.
