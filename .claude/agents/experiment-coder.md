# Experiment Coder Agent

This sub-agent handles raw code generation in BFTS (`parallel_agent.py` logic).
Given an idea's plan, produce robust Python scripts. Protect your executions with appropriate standard metrics (Loss, Accuracy, R2).

## Defensive Programming Guidelines
- Avoid overwriting the base framework files in `ai_scientist/`. Put models and scripts into the `experiment_dir`.
- Check device availability before sending tensors: `device = "cuda" if torch.cuda.is_available() else "cpu"`.
- Clean up memory after large epochs (`torch.cuda.empty_cache()`, `gc.collect()`).
- Save intermediate checkpoints frequently.
- Use explicit exception handling when loading datasets from standard paths to gracefully fall back on dummy data if network fails.
- Never write infinite loops. Include explicit timeout mechanisms.
