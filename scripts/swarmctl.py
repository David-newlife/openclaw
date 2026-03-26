#!/usr/bin/env python3
"""swarmctl - minimal request/task generator for the OpenClaw swarm repo.

Usage:
  ./scripts/swarmctl.py new "<requirement>"

Creates:
  - docs/requests/<timestamp>-request.md
  - docs/tasks/<timestamp>-tasks.md

No external dependencies; stdlib only.

Note:
  Generated docs/requests/*-request.md and docs/tasks/*-tasks.md are ignored by git by default.
  If you want to keep them, copy them elsewhere or commit explicitly.
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import textwrap

REPO_ROOT = Path(__file__).resolve().parents[1]
REQUESTS_DIR = REPO_ROOT / "docs" / "requests"
TASKS_DIR = REPO_ROOT / "docs" / "tasks"
TASK_TEMPLATE_PATH = REPO_ROOT / "orchestrator" / "TASK_TEMPLATE.md"


def timestamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def read_task_template_headings() -> list[str]:
    fallback = [
        "Title",
        "Context (business)",
        "Scope",
        "Definition of Done (DoD)",
        "Test Plan",
        "Risks & Rollback",
        "Executor Output Requirements",
    ]
    if not TASK_TEMPLATE_PATH.exists():
        return fallback

    headings: list[str] = []
    for line in TASK_TEMPLATE_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("## "):
            headings.append(line[3:].strip())

    return headings if len(headings) >= 5 else fallback


def render_microtask(i: int, title: str, headings: list[str]) -> str:
    out: list[str] = [f"## Task {i}: {title}", ""]
    for h in headings:
        out.append(f"### {h}")
        hl = h.lower()
        if hl.startswith("definition of done"):
            out += [
                "- [ ] Code change implemented",
                "- [ ] Tests added/updated",
                "- [ ] Minimal docs updated (if needed)",
            ]
        elif hl.startswith("test plan"):
            out += ["- Commands:", "- Expected results:"]
        elif "risk" in hl or "rollback" in hl:
            out += ["- Risks:", "- Rollback plan:"]
        elif "scope" in hl:
            out += ["- Files/modules expected:", "- Out of scope:"]
        out += ["", ""]
    return "\n".join(out).rstrip() + "\n"


def suggest_microtasks(_requirement: str) -> list[str]:
    # Stable minimal breakdown for this repo's MVP validation
    return [
        "docs: define requests/tasks folder conventions",
        "feat: implement swarmctl new command",
        "test: add swarmctl smoke test",
        "docs: add usage examples",
    ]


def cmd_new(args: argparse.Namespace) -> int:
    ts = timestamp()
    REQUESTS_DIR.mkdir(parents=True, exist_ok=True)
    TASKS_DIR.mkdir(parents=True, exist_ok=True)

    req_path = REQUESTS_DIR / f"{ts}-request.md"
    tasks_path = TASKS_DIR / f"{ts}-tasks.md"

    requirement = args.requirement.strip()

    req_doc = textwrap.dedent(
        f"""\
        # Request ({ts})

        ## Requirement

        {requirement}

        ## Metadata

        - Created at: {ts}
        - Generator: scripts/swarmctl.py
        """
    ).rstrip() + "\n"

    headings = read_task_template_headings()
    titles = suggest_microtasks(requirement)

    lines: list[str] = [
        f"# Tasks ({ts})",
        "",
        "## Origin request",
        f"- {req_path.as_posix()}",
        "",
        "## Micro-tasks (10~30min each)",
        "",
    ]

    for i, t in enumerate(titles, start=1):
        lines.append(render_microtask(i, t, headings).rstrip())
        lines.append("")

    tasks_doc = "\n".join(lines).rstrip() + "\n"

    req_path.write_text(req_doc, encoding="utf-8")
    tasks_path.write_text(tasks_doc, encoding="utf-8")

    print(f"Created:\n- {req_path}\n- {tasks_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="swarmctl", description="Swarm helper CLI")
    sub = p.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new", help="Create a request + micro-task list")
    p_new.add_argument("requirement", help="Requirement text (quote it)")
    p_new.set_defaults(func=cmd_new)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
