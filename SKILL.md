---
name: source-code-guide
description: Use when a user wants to understand an unfamiliar codebase, map major features, trace a specific feature's key call chain, keep branch-level reading context while drilling deeper, or prepare annotated code-reading material before optionally writing comments into source files.
---

# Source Code Guide

Guide source-code reading from global structure to focused code study. Keep the user oriented, cite evidence, and avoid invented architecture.

## Core Rules

- Start global, then narrow one feature at a time.
- Write reading artifacts under `docs/source-guides/<project-slug>/`.
- Use the templates in `references/templates.md`.
- Every confirmed call point must include a file path and line number.
- If a line number cannot be verified, write `unlocated`. Never guess.
- If a relationship is not direct, label it as `indirect call`, `route dispatch`, `configuration binding`, `event trigger`, or `unresolved`.
- Put uncertain claims in `Unconfirmed Points` with a confidence label.
- Do not modify source files by default. Ask before using `code-commenter`.

## Workflow

1. Build `00-project-map.md`.
2. After the user chooses a feature, build `01-feature-<feature-name>.md`.
3. Maintain `02-feature-<feature-name>-subchain.md` as the shared branch-navigation page for that feature.
4. When the user focuses on one code region, build `03-feature-<feature-name>-code-<topic>.md`.
5. Ask whether the final annotated output should stay in the reading doc, go into source files, or both.

## Document Rules

### `00-project-map.md`

Include a short project introduction, feature groups, entry evidence, recommended reading order, and unconfirmed points.

### `01-feature-<feature-name>.md`

Include a short feature introduction, feature goal, user-facing entry, key modules, main call-chain overview, suggested next branches, and evidence notes.

### `02-feature-<feature-name>-subchain.md`

Store all branch drill-down sections in one file. Use `## to_<branch-name>` headings. For each branch, include its purpose, key call points, path-and-line references, relationship type, confidence, drill-down guidance, and sibling branches worth reading next.

### `03-feature-<feature-name>-code-<topic>.md`

Start with a rough summary, explain what the user should know before reading the code, provide annotated reading material, map it back to the parent branch, and record the persistence decision.

## Evidence Discipline

- Do not infer features from directory names alone.
- Back feature claims with routes, command registration, module declarations, or other entry evidence.
- Do not treat naming similarity as proof of a call relationship.
- Do not treat folder adjacency as proof of a call relationship.
- Prefer exact `path:line` evidence gathered from search results or `scripts/collect_source_map.py`.
- If you cannot confirm source or target locations, say so explicitly.

## Navigation Block

Every document except `00-project-map.md` must begin with:

- current feature
- current branch or topic
- parent document path
- 2-3 suggested next reading targets

## Final Annotation Step

Before using `code-commenter`, produce a reading-first summary. Then ask whether to:

- keep the annotation in the reading doc only
- write comments into source files
- do both

Use `code-commenter` only after the user chooses an option that includes source edits.
