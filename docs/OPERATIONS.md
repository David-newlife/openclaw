# Operations

## Day-to-day (Elvis style)

1. Capture requirement (Issue / message)
2. Zoe writes a task breakdown (micro-tasks, each 10~30min)
3. Zoe spawns executors (Claude Code) in parallel
4. Executors implement + test + commit
5. Zoe aggregates into a PR and notifies reviewer

## Commit convention

Use Conventional Commits:
- feat: add new functionality
- fix: bug fix
- refactor: refactor without behavior change
- test: add/update tests
- docs: documentation
- chore: tooling / deps

## Micro-task sizing

- Target 10-30 minutes each
- Too big => split
- Too coupled => add a reconnaissance task first

## Failure handling

- Reduce scope
- Add recon/testing
- Avoid stuffing more context into executor
