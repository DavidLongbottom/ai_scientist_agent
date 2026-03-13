---
name: analyze-results
description: Parses output logs/json to evaluate metric success.
---

# Analyze Results Workflow

This skill parses output logs, evaluation metrics, and json result files from experiment runs.

## Operations
1. Find standard output files, typical in `experiments/**/*.json` or `.txt`.
2. Extract the best performance numbers for comparison.
3. Compare the current results with baselines.
4. Output a summary report indicating whether the experiment succeeded based on predefined improvement bounds.

## Rules
- Highlight anomalies or suspicious spikes in loss curves if visible in the raw logs.
- Provide a summary table in markdown format.
