<div align="center">
  <h1>
    <b>The AI Scientist-v2: Claude Code Agent Edition</b><br>
    <b>Workshop-Level Automated Scientific Discovery</b>
  </h1>
</div>

> **About This Repository:**
> This project is a specialized **Claude Code Agent Edition** adapted from the original [SakanaAI AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-ICLR2025-Workshop-Experiment). It restructures the execution model to leverage the `claude` CLI and Anthropic's interactive agent workflows.

Fully autonomous scientific research systems are becoming increasingly capable, with AI playing a pivotal role in transforming how scientific discoveries are made. This system autonomously generates hypotheses, runs experiments, analyzes data, and writes scientific manuscripts. 

While the original v2 relied on static python scripts for orchestration, **this edition uses Claude Code's native `.claude/skills/` and hooks** to orchestrate the Best-First Tree Search (BFTS) experiment manager in an interactive, dynamic, and fault-tolerant way.

> **Caution!**
> This codebase executes Large Language Model (LLM)-written code. Ensure that you run this within a controlled sandbox environment (e.g., a Docker container).

## Table of Contents

1.  [Requirements](#requirements)
2.  [Claude Code Agent Quickstart](#claude-code-agent-quickstart)
3.  [Pipeline Details](#pipeline-details)
4.  [Manual Execution (Legacy)](#manual-execution-legacy)
5.  [Citing The AI Scientist-v2](#citing-the-ai-scientist-v2)

## Requirements

This code is designed to run on Linux with NVIDIA GPUs using CUDA and PyTorch.

### Installation

```bash
# Create a new conda environment
conda create -n ai_scientist python=3.11
conda activate ai_scientist

# Install PyTorch with CUDA support (adjust pytorch-cuda version for your setup)
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

# Install PDF and LaTeX tools
conda install anaconda::poppler
conda install conda-forge::chktex

# Install Python package requirements
pip install -r requirements.txt

# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code
```

### Supported Models and API Keys

By default, the system requires API keys for the foundation models performing the research:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_KEY_HERE"
export S2_API_KEY="YOUR_SEMENTIC_SCHOLAR_KEY"  # Optional, for literature
```

**AWS Bedrock (Claude Models)**  
The system can use Claude directly via Bedrock. If doing so, ensure:
```bash
pip install anthropic[bedrock]
export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_KEY"
export AWS_REGION_NAME="your-aws-region"
```

## Claude Code Agent Quickstart

You can now run end-to-end scientific research by interacting dynamically with the `claude` CLI. Be sure you are in the project root containing the `.claude/` directory.

1. **Setup Codex:** (Optional for adversarial cross-model review) `claude mcp add codex -s user -- codex mcp-server`
2. **Launch Interactive Pipeline:**
   ```bash
   claude
   > /research-pipeline "Your research topic/direction"
   ```

Or you can invoke individual workflows to perform partial steps:
- `> /idea-discovery "your topic"`
- `> /tree-search "path/to/idea.json"`
- `> /auto-review-loop`
- `> /paper-writing`

This dynamic pipeline includes built-in retry mechanisms, memory monitors (`/monitor-experiment`), and automatic compilation fallbacks (`/paper-compile`).

## Pipeline Details

When you execute `/research-pipeline`, the Claude Code Agent follows these automated steps:
1. **Ideation:** Generates a set of ideas and checks their novelty using Semantic Scholar.
2. **Selection:** Pauses to ask the user which drafted idea to pursue.
3. **Execution:** Triggers the BFTS (Best-First Tree Search) coding agent. It writes, runs, and evaluates models against datasets.
4. **Analysis & Plotting:** Runs the aggregation step to create LaTeX-ready figures.
5. **Auto-Review:** Repeatedly evaluates the manuscript using LLMs, performing automated code/text fixes until a minimum score gate is passed.
6. **Publication:** Compiles the PDF.

## Manual Execution (Legacy)

If you prefer to bypass the Claude Code agent orchestration and use the raw Python backend scripts:

**1. Ideation:**
```bash
python scripts/run_ideation.py --topic-file "ai_scientist/ideas/my_research_topic.md"
```

**2. BFTS Search:**
```bash
python scripts/run_tree_search.py --load_ideas "ai_scientist/ideas/my_research_topic.json" --load_code --add_dataset_ref
```

**3. Writeup:**
```bash
python scripts/run_writeup.py --folder "experiments/your_experiment_timestamp"
```

## Citing The AI Scientist-v2

If you use the underlying methodology in your research, please cite the original SakanaAI work:

```bibtex
@article{aiscientist_v2,
  title={The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search},
  author={Yamada, Yutaro and Lange, Robert Tjarko and Lu, Cong and Hu, Shengran and Lu, Chris and Foerster, Jakob and Clune, Jeff and Ha, David},
  journal={arXiv preprint arXiv:2504.08066},
  year={2025}
}
```

## ⚖️ License & Responsible Use

This project is licensed under **The AI Scientist Source Code License** (a derivative of the Responsible AI License). By using this code, you are legally bound to clearly and prominently disclose the use of AI in any resulting scientific manuscripts or papers. 

We recommend the following attribution:
> "This manuscript was autonomously generated using [The AI Scientist](https://github.com/SakanaAI/AI-Scientist)."
