---
name: tree-search
description: "运行 Best-First Tree Search 实验。这是 AI-Scientist-v2 的核心实验引擎。"
argument-hint: [idea-json-path]
allowed-tools: Bash(*), Read, Write, Grep, Glob
---

# Tree Search Skill

Execute the BFTS tree search over a chosen idea.

1. Ensure you have the `.json` file containing the selected idea.
2. Run the search algorithm:
   ```bash
   python scripts/run_tree_search.py --idea "$ARGUMENTS" --output-json
   ```
3. Monitor the output from the script.
4. The script will create an `experiments/YYYY-MM-DD_NAME` folder. Wait for it to complete.
5. Report back the output directory and the results of the experiment.
