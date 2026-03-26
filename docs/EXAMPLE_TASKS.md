# Example micro-tasks

下面给出一个“最小可验证需求”的拆分示例，展示 Elvis 风格的 10~30min 微任务如何写。

## Trial requirement (MVP)

**需求**：为本仓库增加一个 `swarmctl` 脚本，用于把一段需求文本写入 `docs/requests/` 并生成标准化的微任务清单（Markdown）。

**验收标准（DoD）**：
- 运行 `./scripts/swarmctl new "<requirement>"` 后：
  - `docs/requests/<timestamp>-request.md` 被创建
  - `docs/tasks/<timestamp>-tasks.md` 被创建（包含 3~7 个微任务，套用 TASK_TEMPLATE 的字段）
- 脚本带 `--help`
- 提供一个最小测试：`python -m scripts.swarmctl ...` 或 bash smoke test（二选一）

> 说明：此需求不涉及真实业务代码，但能验证“需求进入→拆分→产出工单”的流水线入口。

## Suggested micro-tasks

1) **docs: add request/task folder conventions**
- 更新 `docs/OPERATIONS.md`，写清楚 requests/tasks 的文件命名规范

2) **feat: implement swarmctl new**
- 新增 `scripts/swarmctl.py`
- 支持 `new` 子命令 + `--help`

3) **test: add smoke test**
- 新增 `scripts/test_swarmctl.sh`（或 python unittest）

4) **docs: add usage examples**
- README 增加 3 条使用示例

每个微任务都能独立 commit，最后可汇总为一个 PR。
