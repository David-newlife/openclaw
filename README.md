# OpenClaw Swarm Repo (Zoe Orchestrator + Claude Code Executors)

这个仓库用于复现并落地 Elvis 的高效开发模式：

- **OpenClaw = 编排层（Zoe）**：负责业务上下文、任务拆分、模型选择、进度监控、PR 汇总与通知。
- **Claude Code = 执行层**：只聚焦代码库上下文，按微任务小步提交（commit/PR），跑测试与修复 CI。

## 目标

- 把需求拆成 10~30 分钟的 **微任务**，并行执行。
- 默认 **1 微任务 = 1 commit**（或 1 小 PR），实现高频稳定交付。

## 目录结构

- `orchestrator/`：Zoe 编排层规范与提示词
  - `SWARM_POLICY.md`：任务拆分与编排策略
  - `TASK_TEMPLATE.md`：微任务模板（DoD/风险/回滚）
  - `PR_TEMPLATE.md`：PR 输出规范
  - `prompts/`：给执行层（Claude Code）的提示词
- `docs/`：操作手册与排障

## 使用方式（MVP）

1. 在 Issues（或需求文档）中写下需求
2. Zoe（OpenClaw）将需求拆分为若干微任务（每个 10~30 分钟）
3. Claude Code 执行每个微任务：实现 → 测试 → commit
4. Zoe 汇总多个 commit 为 PR，并通知你审核合并

## 权限（后续你配置）

- 推荐：GitHub PAT（repo 权限）或 SSH key
- 配好后可实现：自动 push 分支、自动开 PR。
