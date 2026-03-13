---
name: monitor-experiment
description: Tracks running process and checks memory/CPU usage.
---

# Monitor Experiment Workflow

This skill checks the running state of currently active experiments.

## Operations
1. Use `nvidia-smi` or `top` (via bash) to inspect resource consumption.
2. Read the tail of output logs (e.g. `tail -n 100 log.txt`).
3. Report any out-of-memory errors, crashes, or stalls.

## Resolution Strategies
- If OOM occurs: Reduce batch size in `bfts_config.yaml` or code, and recommend killing the process.
- If stalled for > 15 minutes without log activity: Recommend restarting the session.
