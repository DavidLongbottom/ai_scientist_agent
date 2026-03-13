# Code Execution Sandbox

- Prevent random web access during code runs unless absolutely required to download data.
- The `interpreter.py` is the designated way to safely invoke code. Do not bypass it by throwing raw subprocess requests everywhere.
- Do not let the agent arbitrarily modify core `ai_scientist/` logic without explicit user review.
