#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

req='Smoke test requirement'

python3 "$ROOT_DIR/scripts/swarmctl.py" new "$req" >/dev/null

# Find most recent generated files (exclude README.md)
latest_req=$(ls -1 "$ROOT_DIR/docs/requests" | grep -E '^[0-9]{8}-[0-9]{6}-request\.md$' | sort | tail -n 1)
latest_tasks=$(ls -1 "$ROOT_DIR/docs/tasks" | grep -E '^[0-9]{8}-[0-9]{6}-tasks\.md$' | sort | tail -n 1)

[[ -n "$latest_req" ]]
[[ -n "$latest_tasks" ]]

[[ -f "$ROOT_DIR/docs/requests/$latest_req" ]]
[[ -f "$ROOT_DIR/docs/tasks/$latest_tasks" ]]

grep -q "$req" "$ROOT_DIR/docs/requests/$latest_req"
grep -q "## Micro-tasks" "$ROOT_DIR/docs/tasks/$latest_tasks"

echo "OK: generated $latest_req and $latest_tasks"
