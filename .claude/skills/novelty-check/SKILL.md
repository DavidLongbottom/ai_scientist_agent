---
name: novelty-check
description: Check novelty of candidate ideas
argument-hint: [idea-description]
allowed-tools: Bash(*), Read, mcp__codex__codex
---

# Novelty Check

Check if an idea has already been done in the literature.

Uses Semantic Scholar searches combined with `mcp__codex__codex` review.
Report High/Medium/Low novelty and any closest matching works.
