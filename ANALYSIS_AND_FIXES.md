# AI-Scientist-v2 Claude Code Agent 项目分析与修复报告

## 一、发现的 BUG 与错误

### 🔴 严重错误 (Critical Bugs)

#### 1. `_check_substage_completion` 死代码 (Dead Code)
**文件:** `ai_scientist/treesearch/agent_manager.py:397-408`
**问题:** 在 `_check_substage_completion()` 方法中，第 362 行的 `return` 语句（无论是 True/False 分支）都会在 try/except 块中返回，导致第 397-408 行的 `max_iterations` 检查**永远不会执行**。这是一个逻辑短路错误。
```python
# Line 363-395: try/except block always returns
# Line 397-408: DEAD CODE - never reached
if len(journal.nodes) >= current_substage.max_iterations:
    ...
    return True, "Reached max iterations"
```
**影响:** 子阶段的 max_iterations 限制完全失效，可能导致无限循环。

#### 2. `_check_substage_completion` 返回值不一致
**文件:** `ai_scientist/treesearch/agent_manager.py:408`
**问题:** 函数在某些路径返回 `(bool, str)` 元组，但最后一行 `return False` 只返回单值 `bool`，调用方使用 `substage_complete, substage_feedback = ...` 解包将崩溃。

#### 3. `make_llm_call` 不支持 Gemini 和 Claude 模型
**文件:** `ai_scientist/llm.py:215-255`
**问题:** `make_llm_call()` 函数只支持 `ollama/`, `gpt`, `o1/o3` 模型，不支持 `gemini` 和 `claude` 模型，但 `get_response_from_llm()` 中的 `gpt` 分支调用了它。Bedrock Claude 模型在 config 中是默认的 code 模型，但如果错误地通过 `make_llm_call` 路由将直接报错。

#### 4. `get_batch_responses_from_llm` 缺少 `@track_token_usage` 兼容性
**文件:** `ai_scientist/llm.py:86-96`
**问题:** `@track_token_usage` 装饰器假设被装饰函数返回一个 LLM response 对象（具有 `.model`, `.usage` 等属性），但 `get_batch_responses_from_llm` 返回的是 `(content, new_msg_history)` 元组。装饰器会尝试访问 `result.model` 导致 `AttributeError`。

#### 5. `token_tracker.py` 中 `logging.info` 参数错误
**文件:** `ai_scientist/utils/token_tracker.py:153-154, 195-196`
**问题:** `logging.info("args: ", args)` 是错误用法。`logging.info()` 不像 `print()` 那样接受多参数，正确写法应为 `logging.info("args: %s", args)`。

### 🟡 中等错误 (Medium Severity Issues)

#### 6. 5个 Skills 目录为空，无 SKILL.md
**目录:**
- `.claude/skills/analyze-results/` (空)
- `.claude/skills/monitor-experiment/` (空)
- `.claude/skills/run-experiment/` (空)
- `.claude/skills/research-lit/` (空)
- `.claude/skills/paper-compile/` (空)

**问题:** CLAUDE.md 中列出了 `/paper-compile` 等命令，但对应的 skill 目录为空。Claude Code 调用这些 skill 时会失败。

#### 7. `pre-compact.py` 状态保存不完整
**文件:** `.claude/hooks/pre-compact.py`
**问题:** 仅保存了 `sys_time` 和 `compression_trigger`，没有保存实际的实验进度、当前阶段、journal 状态等关键信息。Compact 恢复后无法知道实验进行到哪个步骤。

#### 8. Safety Hook 不阻止危险操作
**文件:** `.claude/hooks/experiment-safety-check.sh`
**问题:** Hook 只打印警告信息并 `exit 0`，即使发现没有 API key 或 GPU 内存不足，也不会阻止命令执行。应该在关键条件不满足时 `exit 1` 以阻断操作。

#### 9. `run_tree_search.py` 缺少 GPU 可用性检查
**文件:** `scripts/run_tree_search.py:14-17`
**问题:** 定义了 `get_available_gpus()` 函数但从未调用，也没有根据 GPU 数量自动调整 `num_workers`。

#### 10. `bfts_config.yaml` 中 `num_workers: 4` 与 `num_seeds: 3` 不匹配
**文件:** `bfts_config.yaml:38,49`
**问题:** 根据 README，`num_seeds` 应 ≤ `num_workers`（当 num_workers < 3 时），或设为 3（当 num_workers ≥ 3 时）。当前配置 `num_workers=4, num_seeds=3` 虽然合法但没有在启动时验证。

## 二、架构不足与改进方向

### 🔧 设计不足

#### 11. Agent 定义过于简单
**文件:** `.claude/agents/*.md`
**问题:** 每个 agent 描述仅 5-7 行，缺少：
- 具体的输入/输出格式规范
- 错误处理流程
- 与其他 agent 的协作协议
- 质量评估标准

#### 12. 研究管道缺少错误恢复机制
**文件:** `.claude/skills/research-pipeline/SKILL.md`
**问题:** 流水线是线性的，没有：
- 任何步骤失败后的重试逻辑
- 中间状态保存与恢复
- 超时处理
- 部分成功的回退策略

#### 13. MEMORY.md 过于简单
**文件:** `MEMORY.md`
**问题:** 仅有 3 条 `[LEARN]` 记录，缺少：
- 结构化的知识分类
- 成功/失败的实验记录
- 最佳实践模式库
- API 调用参数优化记录

#### 14. `auto-review-loop` 引用了不存在的 `/verify` skill
**文件:** `.claude/skills/auto-review-loop/SKILL.md:14`
**问题:** 步骤 4 提到 "执行 `/verify` 或 recompile context"，但没有 verify skill。

#### 15. Token 成本追踪不包含 Claude/Bedrock 模型
**文件:** `ai_scientist/utils/token_tracker.py:25-60`
**问题:** `MODEL_PRICES` 字典只包含 OpenAI 模型的价格，但项目的默认编码模型是 `anthropic.claude-3-5-sonnet-20241022-v2:0`（Bedrock）。无法追踪主要的实验成本。

---

## 三、具体修复执行计划 (Execution Plan)

我们将按照以下四个阶段逐步对项目进行重构和修复，以确保 Claude Code 在该项目上能高效稳定地运行科学发现流水线。

### 阶段 1：核心逻辑 Bug 修复 (Critical)
* **1.1 修复 `agent_manager.py` 死代码与逻辑短路**
  * 修改 `_check_substage_completion` 方法：统一并重新组织逻辑，确保在返回前对 max_iterations 进行正确判断，并且所有分支统一返回 `(bool, str)`。
* **1.2 修复 `llm.py` 中的适配问题**
  * 在 `get_batch_responses_from_llm` 以及 `@track_token_usage` 中修复对批处理返回元组的兼容性，使其正确计算 token 或直接忽略对于不支持格式情况的强行记录。
  * 扩展 `make_llm_call` 方法：添加针对 `claude-` 系列模型和 `gemini` 系列模型的分支。

### 阶段 2：日志与成本追踪改进 (Medium)
* **2.1 修复 `logging.info` 语法问题**
  * 在 `token_tracker.py` 中将 `logging.info("args: ", args)` 替换为标准的格式化语法 `logging.info("args: %s", args)`。
* **2.2 扩展 `token_tracker.py` 计费字典**
  * 在 `MODEL_PRICES` 中补充 Bedrock Claude 模型 (`anthropic.claude-3-5-sonnet-20241022-v2:0` 等) 的官方 token 定价信息。

### 阶段 3：健全 Claude Hooks 与 Skills (Medium)
* **3.1 补充缺失的 Skills (.claude/skills/)**
  * 为 `.claude/skills/` 目录下为空的文件夹编写并补齐 `SKILL.md` 文件。
* **3.2 改进 Safety Hook (`experiment-safety-check.sh`)**
  * 如果没有查找到环境变量要求的 API Key，则进行 `exit 1` 阻断执行，防止产生无效调用费用并死转。
* **3.3 补全 `pre-compact.py` 状态记录**
  * 在将来的交互中，改进 hook 的状态序列化。

### 阶段 4：架构强化与鲁棒性提升 (Important)
* **4.1 细化 Agent 模型指示 (`.claude/agents/*.md`)**
  * 对于专门子角色的指令进行内容扩充和健壮性设计。
* **4.2 完善整体 Research Pipeline**
  * 在 `research-pipeline/SKILL.md` 中增加容错和自动重试的说明。
