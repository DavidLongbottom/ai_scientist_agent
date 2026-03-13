---
name: paper-writing
description: "Workflow 3 pipeline: Citation gathering -> Paper Writeup -> PDF compilation"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read, Skill
---

# Paper Writing Workflow

1. `/gather-citations` over the `[experiment-dir]`
2. `/paper-writeup` over the `[experiment-dir]` to generate the `.tex` files.
3. Automatically check that a `.pdf` file was correctly built and matches quality gates.
