# Source Code Guide Templates

Use these templates as the default output shape.

## `00-project-map.md`

```md
# Project Map

## Short Introduction
- Project type:
- Primary job:
- Suggested first features to read:

## Feature Groups
### <feature-name>
- What it does:
- Entry evidence:
  - `path/to/file.ext:line`
- Confidence: high | medium | low

## Recommended Reading Order
1. <feature-name>
2. <feature-name>
3. <feature-name>

## Unconfirmed Points
- None.
```

## `01-feature-<feature-name>.md`

```md
# <Feature Name>

## Short Introduction
- Why this feature matters:
- Why this main chain is worth reading first:

## Current Reading Position
- Current feature: <feature-name>
- Current branch or topic: overview
- Parent document: `docs/source-guides/<project-slug>/00-project-map.md`
- Suggested next targets:
  - `02-feature-<feature-name>-subchain.md#to_<branch-name>`
  - `02-feature-<feature-name>-subchain.md#to_<branch-name>`

## Feature Goal
- User-facing goal:

## Entry and Key Modules
- Entry:
  - `path/to/file.ext:line`
- Key modules:
  - `path/to/file.ext:line`

## Main Call Chain
- `<source> -> <target>`
  - From: `path/to/file.ext:line`
  - To: `path/to/file.ext:line`
  - Relationship: direct call | indirect call | route dispatch | configuration binding | event trigger | unresolved
  - Why it matters:
  - Confidence: high | medium | low

## Suggested Branches
- `to_<branch-name>`:
- `to_<branch-name>`:

## Unconfirmed Points
- None.
```

## `02-feature-<feature-name>-subchain.md`

```md
# <Feature Name> Branch Navigation

## Current Reading Position
- Current feature: <feature-name>
- Current branch or topic: branch navigation
- Parent document: `docs/source-guides/<project-slug>/01-feature-<feature-name>.md`
- Suggested next targets:
  - `## to_<branch-name>`
  - `## to_<branch-name>`

## to_<branch-name>
- Purpose:
- When to follow this branch:

### Key Call Points
- `<source> -> <target>`
  - From: `path/to/file.ext:line`
  - To: `path/to/file.ext:line`
  - Relationship: direct call | indirect call | route dispatch | configuration binding | event trigger | unresolved
  - Role:
  - Confidence: high | medium | low

### Read Next
- Drill deeper if:
- Sibling branches worth reading after this:
  - `to_<branch-name>`
  - `to_<branch-name>`

## Unconfirmed Points
- None.
```

## `03-feature-<feature-name>-code-<topic>.md`

```md
# <Feature Name> Code Reading: <Topic>

## Current Reading Position
- Current feature: <feature-name>
- Current branch or topic: <topic>
- Parent document: `docs/source-guides/<project-slug>/02-feature-<feature-name>-subchain.md#to_<branch-name>`
- Suggested next targets:
  - sibling branch
  - return to feature overview

## Rough Summary
- What this code region is responsible for:

## Read This First
- Required context:
- Inputs:
- Outputs:

## Annotated Reading Material
- File: `path/to/file.ext`
- Focus region: `path/to/file.ext:line`
- Notes:

## Parent Branch Mapping
- This code belongs to:
- Upstream call point:
- Downstream effect:

## Persistence Decision
- Reading doc only | source edits | both
```
