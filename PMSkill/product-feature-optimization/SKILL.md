---
name: product-feature-optimization
description: Guide product feature optimization from problem discovery through launch validation. Use when Codex needs to define optimization goals, collect and analyze user problems, prioritize improvements, design solution proposals, write PRDs, create test and acceptance records, or evaluate post-launch product impact for an existing product feature.
---

# Product Feature Optimization

## Workflow

Use this as one end-to-end workflow with eight stages. First identify the user's current stage, then continue from there:

1. Define optimization goal.
2. Collect problems and needs.
3. Analyze and classify issues.
4. Prioritize optimization items.
5. Define the solution.
6. Write the PRD or functional requirements.
7. Support development validation and acceptance.
8. Track post-launch results.

If the user says only that they want to optimize a feature, start at stage 1. If they provide feedback, data, tickets, or interviews, start at stage 2 or 3. If they already know what to build, start at stage 5 or 6. If the feature is already released, start at stage 8.

## Operating Rules

- Match the user's language unless they request another language.
- Do not jump to solutions before clarifying the problem, evidence, and goal.
- Ask only the minimum questions needed to produce a useful next artifact.
- Mark assumptions clearly when evidence, metrics, owners, dates, or constraints are missing.
- Preserve the source distinction between confirmed facts, hypotheses, decisions, and open questions.
- Prefer tables for problem pools, classification, prioritization, requirements, test cases, acceptance records, and metrics.
- Keep each stage output usable as a standalone product document.

## Stage Guidance

### 1. Define Optimization Goal

Clarify why the feature needs optimization and how success will be measured. Ask for the feature, business trigger, current symptoms, target metric, timeline, and constraints. Output a product optimization goal statement.

### 2. Collect Problems and Needs

Gather pain points from user feedback, support tickets, analytics, sales or operations feedback, internal interviews, and competitor observations. Output a problem and requirement collection table.

### 3. Analyze and Classify

Turn scattered input into structured issue categories, affected users, impact, and root-cause hypotheses. Output a problem analysis report.

### 4. Prioritize Optimization Items

Decide what should be done first. Use RICE by default unless the user requests another method. If inputs are incomplete, estimate transparently and mark confidence. Output a feature optimization prioritization table.

### 5. Define Solution

Describe how the product should change, including user flow changes, functional rules, edge cases, risks, and dependencies. Output a feature optimization solution proposal.

### 6. Write PRD

Create a requirements document that design, engineering, data, and QA can execute. Include goals, non-goals, user stories, functional requirements, UX states, tracking, acceptance criteria, dependencies, and open questions.

### 7. Develop and Validate

Translate requirements into test cases and acceptance records. Confirm implementation against the PRD, call out deviations, and separate pass/fail results from unresolved questions.

### 8. Track Post-launch Results

Compare pre-launch and post-launch metrics, summarize feedback, identify regressions or remaining gaps, and create the next optimization backlog. Output a launch impact report and next-round optimization list.

## Templates

Read `references/templates.md` when producing formal artifacts for any stage. Use only the sections relevant to the user's current request.
