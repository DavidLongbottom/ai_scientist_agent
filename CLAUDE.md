# CLAUDE.MD -- AI Scientist v2 (Claude Code Agent Edition)

**Project:** AI-Scientist-v2
**Purpose:** Autonomous end-to-end scientific research via agentic tree search
**Branch:** main

## Core Principles
- **Plan first** — 实验前必须有明确假设和实验设计
- **Safety first** — 所有 LLM 生成代码在沙箱中执行
- **Cross-model review** — Claude 执行 + GPT 审稿，避免自我盲点
- **Document everything** — 每个实验节点、审稿轮次必须有完整记录
- **[LEARN] tags** — 实验教训记录到 MEMORY.md

## Folder Structure
```
AI-Scientist-v2/
├── CLAUDE.md                          # Project configurations
├── MEMORY.md                          # Persistent knowledge
├── .claude/
│   ├── settings.json                  # Hooks and permissions
│   ├── rules/                         # Governance
│   ├── skills/                        # Composable operations
│   ├── agents/                        # Specialized sub-agents
│   └── hooks/                         # Lifecycle scripts
├── ai_scientist/                      # Core search algorithms
├── scripts/                           # CLI entry points
├── templates/                         # Templates
└── experiments/                       # Saved states & runs
```

## Commands
```bash
# LaTeX compilation
cd [latex_dir] && latexmk -pdf -interaction=nonstopmode

# General execution
python scripts/run_ideation.py --workshop-file [file]
python scripts/run_tree_search.py --idea [file]
```

## Skills Quick Reference
| Command | Description |
|---|---|
| `/idea-discovery` | Workflow 1: From direction to idea (ideation + novelty) |
| `/auto-research-loop` | Workflow 2: Tree search + results aggregation + review |
| `/paper-writing` | Workflow 3: Citation gathering + compile + PDF gen |
| `/research-pipeline` | Full end-to-end pipeline |
| `/ideation` | Generate research ideas via LLM |
| `/tree-search` | Run BFTS tree search over an idea |
| `/plot-aggregation` | Generate summary plots |
| `/gather-citations` | Collect citations for the writeup |
| `/paper-writeup` | Generate LaTeX paper |
| `/paper-compile` | Compile LaTeX to PDF |
| `/llm-review` | Get standard paper review |
| `/vlm-review` | Get visual review of plots |
| `/novelty-check` | Verify technical novelty of ideas |

## Environment
- Python 3.11 + PyTorch + CUDA
- API Keys: OPENAI_API_KEY, S2_API_KEY, AWS_* (for Bedrock)
- LaTeX: poppler, chktex
