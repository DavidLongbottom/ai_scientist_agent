---
name: plot-aggregation
description: "图表聚合，生成最终的可视化结果。需要指定 experiment directory。"
argument-hint: [experiment-dir]
allowed-tools: Bash(*), Read, Write
---

# Plot Aggregation Skill

Creates and aggregates plots from the BFTS experiment runs.

1. Run the plotting script:
   ```bash
   python scripts/run_plotting.py --experiment-dir "$ARGUMENTS" --output-json
   ```
2. Report the generated plot paths.
