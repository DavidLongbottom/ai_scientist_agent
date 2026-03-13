---
name: research-lit
description: Uses literature search APIs to find additional context.
---

# Research Literature Workflow

This skill finds previous works and relevant context to anchor the generated paper.

## Operations
1. Formulate queries based on the "Title" and "Short Hypothesis" of the current idea.
2. Use Semantic Scholar API tool (`ai_scientist/tools/semantic_scholar.py`) to query papers.
3. Extract abstracts and synthesize key findings.
4. Incorporate the findings into the "Related Works" section or idea refinement phase.
5. Provide standard BibTeX entries for the relevant papers.
