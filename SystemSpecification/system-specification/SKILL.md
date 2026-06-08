---
name: system-specification
description: Create, revise, audit, or reverse-engineer Traditional Chinese system specification documents for software systems, products, modules, or features. Use when Codex needs to produce an integrated system spec, SRS, requirements specification, technical specification, architecture specification, API/interface specification, data model specification, non-functional requirements, acceptance criteria, traceability matrix, or implementation-ready spec from user notes, meeting records, PRDs, codebases, or existing documents without inventing unsupported facts.
---

# System Specification

## Workflow

1. Identify the target system, feature, module, audience, source material, requested output file or format, and whether the task is greenfield creation, brownfield reverse-engineering, revision, or audit.
2. If source material exists, inspect it first and separate confirmed facts from assumptions, gaps, and open questions.
3. Choose the appropriate emphasis:
   - Integrated system spec by default: requirements, architecture, data, APIs, operations, security, and acceptance.
   - SRS emphasis when the user asks for IEEE-style requirements, compliance, contracts, vendor handoff, or traceability.
   - SDS emphasis when the user asks for software design, UML, class diagrams, sequence diagrams, database design, implementation plan, or developer assignments.
   - Architecture emphasis when the user asks for context diagrams, architecture views, capacity, reliability, data flow, API contracts, technology decisions, or failure modes.
4. Load `references/system-spec-template.md` and use it as the output structure unless the user provides a custom template.
5. Write in Traditional Chinese by default while preserving product names, API names, database names, field names, and common terms such as `SRS`, `NFR`, `API`, `ADR`, `SLO`, and `traceability matrix`.
6. Produce a decision-ready Markdown specification. If creating or editing a file, keep the filename clear and stable, such as `system-spec.md` or `<feature>-system-spec.md`.
7. End with unresolved questions and source-backed assumptions when information is missing. Do not silently fill gaps.

## Specification Rules

- State the document goal and scope before detailed requirements.
- Include revision history, intended audience, references, glossary, and a tracked `待確認` list for formal or handoff-ready documents.
- Separate requirements from implementation design. Mark speculative design as `建議` or `假設`, not confirmed fact.
- Make functional requirements observable and testable. Prefer `FR-001`, `FR-002` numbering for formal specs.
- Make non-functional requirements measurable when possible: latency, availability, retention, security, auditability, throughput, recovery time, or compatibility targets.
- Distinguish functional requirements from non-functional requirements and business rules.
- Include acceptance criteria for user-visible behavior and critical backend behavior.
- Include a traceability matrix when the output has formal requirements, multiple stakeholders, or implementation handoff needs.
- For APIs, specify method, path, request, response, auth, validation, errors, idempotency, rate limits, and versioning when known.
- Apply DRY documentation: if OpenAPI, Swagger, ERD, ADR, runbooks, or external specs already exist, summarize the contract and link or reference the authoritative source instead of duplicating full payloads.
- For data models, specify entities, key fields, relationships, constraints, lifecycle, retention, and migration concerns when known.
- For architecture, start with the fewest components that satisfy the requirements. Every added component should have a reason.
- Use role-oriented architecture views when the system is complex: application, security, sizing/performance, infrastructure/operations, and development.
- Include diagrams when they clarify behavior: Mermaid or PlantUML context diagrams, sequence diagrams, ER diagrams, class diagrams, deployment diagrams, or data-flow diagrams.
- Add back-of-the-envelope sizing when architecture choices depend on traffic, storage, throughput, read/write ratio, concurrency, or cost.
- For reliability, list failure modes, blast radius, detection, recovery, and fallback for critical components.
- For security, cover authentication, authorization, data sensitivity, audit logs, secrets, abuse prevention, and compliance constraints when relevant.
- Do not invent owners, deadlines, business rules, metrics, schemas, API contracts, or technology choices. Use `待確認` for missing facts.

## Brownfield Rules

- Inspect repository structure, entrypoints, routes, schemas, configuration, and tests before drafting conclusions.
- Treat code as stronger evidence than comments or stale docs, but flag contradictions instead of resolving them silently.
- Describe current implementation separately from recommended future changes.
- If no source can be inspected, ask for repository access, file paths, screenshots, pasted docs, or product notes.

## Audit Rules

- Review completeness against the template sections.
- Check whether each requirement has acceptance criteria and whether critical requirements map to implementation or test coverage.
- Flag ambiguous requirements, unmeasurable NFRs, missing API/data/security details, and unsupported assumptions.
- Provide concrete edits or a revised spec when the user asks for improvement, not only a score.

## Output Guidance

- Start directly with the specification or audit result, not a long explanation of the process.
- Use concise headings, numbered requirements, and tables where they improve scanability.
- Keep the document implementation-ready but not over-specified beyond available evidence.
- Preserve important dates, metrics, constraints, stakeholder terms, and domain language from the source.
- If the request is broad and the source is thin, create a useful v0 spec and make gaps visible under `待確認事項`.
