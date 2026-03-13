# Experiment Safety

**沙箱执行、超时 3600s、GPU 内存检查**

1. Ensure the Python process timeouts are strictly respected (max 3600s).
2. Check GPU `memory.used < 500 MiB` before starting a heavy `tree-search` or assigning `num_workers`.
3. If hitting memory limits, gracefully drop parallel workers instead of crashing everything.
