# Source Code Guide

[Chinese / 中文版](./README.zh-CN.md)

`source-code-guide` is a Codex skill for reading unfamiliar codebases in stages instead of jumping straight into raw source.

It helps an agent:

- map major features in a project
- trace one feature's main call chain
- keep branch-level reading context while drilling deeper
- produce focused code-reading docs before optionally adding source comments

## What It Generates

The skill writes reading artifacts under:

```text
docs/source-guides/<project-slug>/
  00-project-map.md
  01-feature-<feature-name>.md
  02-feature-<feature-name>-subchain.md
  03-feature-<feature-name>-code-<topic>.md
```

## Key Rules

- Cite evidence before claiming architecture.
- Include `path:line` references for confirmed call points.
- Use `unlocated` when a line number cannot be verified.
- Keep uncertain claims in `Unconfirmed Points`.
- Ask before writing comments into source files.

## Repository Layout

- `SKILL.md` - core workflow and hard rules
- `references/templates.md` - markdown templates for generated guides
- `scripts/collect_source_map.py` - helper for extracting stable `path:line` matches
- `agents/openai.yaml` - UI-facing metadata

## Quick Start

Place this folder in your Codex skills directory and invoke it when you want to understand a new repository by feature map, branch navigation, and focused code reading.

Example intents:

- "Help me understand the main features in this repository."
- "Show me the key call chain for the login feature."
- "I want to closely read the token validation code path."

## Helper Script

The helper script can locate literal text in one file and print stable `path:line` matches:

```bash
python scripts/collect_source_map.py --file ./SKILL.md --find "## Core Rules"
```
