# LLM API Conventions

- Models: Default to `gpt-4o-2024-05-13` or `o1-preview-2024-09-12` depending on complexity.
- API keys MUST be loaded from Environment variables (OPENAI_API_KEY, S2_API_KEY).
- Keep a close eye on `token_tracker.json` when generating large files to remain within token budgets.
