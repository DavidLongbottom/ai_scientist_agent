---
name: llm-review
description: "获取针对生成的 PDF 论文的 LLM 审稿意见。该意见更关注逻辑、贡献和描述。"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read, mcp__codex__codex
---

# LLM Review Skill

Runs an extensive review simulation on the compiled PDF.

1. Ensure the PDF is available in the `<experiment-dir>`.
2. Run:
   ```bash
   python scripts/run_review.py --type llm --experiment-dir "$ARGUMENTS" --output-json
   ```
3. A `review_text.txt` will be output. 
4. Read this file and provide the user a breakdown of the Strengths, Weaknesses, and overall Score (which according to quality gates must be >=5 to proceed).
