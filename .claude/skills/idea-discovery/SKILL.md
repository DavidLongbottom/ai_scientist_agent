---
name: idea-discovery
description: Workflow 1 pipeline exploring a direction and generating a ranked list of viable research ideas.
argument-hint: [research-direction]
allowed-tools: Bash(*), Read, Skill, mcp__codex__codex
---

# Idea Discovery Workflow

1. Use `/ideation` to generate a batch of ideas.
2. Perform `/novelty-check` on top few.
3. Present ideas to the human in a Human Checkpoint. Get approval.
