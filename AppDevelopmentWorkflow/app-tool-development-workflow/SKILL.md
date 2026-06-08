---
name: app-tool-development-workflow
description: Create, organize, and maintain a complete Traditional Chinese workflow for building applications or developer tools from planning to implementation, testing, delivery, usage, maintenance, and iteration. Use when Codex needs to turn an idea into implementation-ready documents, task plans, acceptance criteria, README usage docs, or a lightweight delivery process for personal or small-team software projects.
---

# App / Tool Development Workflow

## Workflow

1. Identify the target output: new app, internal tool, CLI, automation script, dashboard, API service, frontend prototype, or maintenance iteration.
2. Determine whether the task is greenfield planning, brownfield improvement, implementation planning, delivery review, or usage documentation.
3. If source material exists, inspect it first and separate confirmed facts from assumptions, gaps, and open questions.
4. Use `references/app-tool-development-workflow.md` as the main process and load only the templates needed for the requested phase.
5. Write in Traditional Chinese by default while preserving technical names, commands, paths, APIs, schemas, and field names in their original form.
6. Keep the process lightweight for personal or small-team work. Add formal governance only when the user asks for team-scale delivery, compliance, production operations, or handoff.
7. Produce artifacts that are directly usable by Codex, engineers, or the future maintainer. Do not invent owners, dates, architecture, APIs, metrics, or constraints.

## Phase Guidance

- For vague ideas, start with `references/project-brief-template.md`.
- For implementation-ready scope, use or extend the existing `system-specification` skill and include functional requirements, non-functional requirements, acceptance criteria, and open questions.
- For architecture and engineering decisions, use `references/technical-design-template.md`.
- For execution planning, use `references/tasks-template.md`.
- For release and usage handoff, use `references/readme-template.md` and `references/acceptance-checklist.md`.
- For an existing repository, inspect entrypoints, package manifests, configs, tests, routes, schemas, scripts, and README files before drafting conclusions.

## Quality Rules

- Every planned feature should map to at least one acceptance criterion.
- Every task should have a completion condition and a verification method.
- Separate product intent from technical design.
- Prefer the smallest usable version before optional enhancements.
- Surface missing facts under `待確認`, not as hidden assumptions.
- Record important tradeoffs as decisions, especially technology stack, storage, deployment, authentication, and external services.
- For UI work, include responsive behavior, empty states, loading states, errors, and accessibility basics.
- For automation or scheduled tools, include trigger, retry, logging, idempotency, timeout, and failure notification behavior.
- For data tools, include source, freshness, schema assumptions, validation, output format, and privacy concerns.
- For production-facing tools, include secrets handling, monitoring, rollback, backup, and runbook notes.

## Output Guidance

- Start with the requested artifact, not a long explanation of the workflow.
- Use concise Markdown headings, checklists, and tables when they improve scanning.
- When creating a project documentation set, use stable filenames:
  - `project-brief.md`
  - `system-spec.md`
  - `technical-design.md`
  - `tasks.md`
  - `README.md`
  - `acceptance-checklist.md`
- Keep documentation decision-ready and implementation-ready, but do not over-specify unsupported details.
- End with `待確認事項` only when meaningful gaps remain.
