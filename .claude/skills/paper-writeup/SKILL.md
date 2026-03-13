---
name: paper-writeup
description: "撰写最终论文模板和内容。默认调用 icbinb 类型（4页版）。"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read
---

# Paper Writeup Skill

Writes the actual LaTeX code for the final paper.

1. Run:
   ```bash
   python scripts/run_writeup.py --experiment-dir "$ARGUMENTS" --type icbinb --output-json
   ```
2. Check that the `.tex` and `.pdf` files are produced in the experiment directory.
