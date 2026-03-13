---
name: run-experiment
description: Executes a specific Python script or BFTS agent stage.
---

# Run Experiment Workflow

This skill is responsible for running Python scripts or specific steps of the experiment execution.

## Allowed Tools
- `Bash`: execution of `python <script>.py`
- `Read/Write`: To read or modify configuration files required for the execution.

## Instructions
1. First, check `.claude/rules/experiment-safety.md` and `.claude/rules/code-execution-sandbox.md`.
2. Do not use this skill to run arbitrary downloaded code.
3. Before running an experiment, ensure that `bfts_config.yaml` is properly configured.
4. Execute the command within a sandboxed interpreter setup if you are coding new features.
5. If running a system-wide script, wrap it with proper stdout redirection to a log file.
6. Report the execution completion and any errors encountered.
