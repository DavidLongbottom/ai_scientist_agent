---
name: ideation
description: "生成研究想法。调用 scripts/run_ideation.py 生成一组带有 JSON 格式的研究想法。"
argument-hint: [workshop-file-path]
allowed-tools: Bash(*), Read, Write, Grep, Glob, WebSearch, mcp__codex__codex
---

# Ideation Skill

This skill generates initial research ideas based on a workshop description template.

1. Locate the markdown template the user specified, e.g. `ideas/my_topic.md`.
2. Run the `scripts/run_ideation.py` script:
   ```bash
   python scripts/run_ideation.py --workshop-file "$ARGUMENTS" --output-json
   ```
3. Read the output. The script generates a corresponding `.json` file containing the generated ideas.
4. Report back the top ideas that were generated, so the user can select one to proceed with.
