---
name: vlm-review
description: "针对生成的图表、图片部分运行 VLM 审稿意见。"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read
---

# VLM Review Skill

Runs visual review of the sub-plots and PDF captions.

1. Ensure the PDF is available.
2. Run:
   ```bash
   python scripts/run_review.py --type vlm --experiment-dir "$ARGUMENTS" --output-json
   ```
3. A `review_img_cap_ref.json` file will be generated containing the VLM reviews.
