---
name: pm-meeting-notes
description: Analyze PM, product, project, and cross-functional meeting records from transcripts, pasted notes, or extracted document text, then produce structured Markdown meeting notes focused on decisions, action items, owners, due dates, risks, blockers, open questions, and follow-up planning. Use when Codex needs to turn meeting records into action-oriented PM documentation or clarify meeting outcomes without inventing missing facts.
---

# PM Meeting Notes

## Workflow

1. Inspect the input and identify whether it is a meeting transcript, rough notes, document excerpt, or a request involving audio/video.
2. If the user provides audio or video without a transcript, ask for a transcript or extract text with an available transcription workflow before applying this skill.
3. Match the output language to the input language unless the user requests a different language.
4. Extract only information supported by the source. Do not invent decisions, owners, due dates, priorities, or next steps.
5. Read `references/meeting-note-template.md` and produce Markdown using that structure.
6. Keep the output action-oriented and suitable for pasting into Notion, Docs, issues, or task trackers.

## Extraction Rules

- Mark missing owners as `未指派`.
- Mark missing due dates or schedules as `未定`.
- Mark unclear decisions, unresolved dependencies, or facts requiring confirmation as `待確認`.
- Preserve important product terms, feature names, customer names, metrics, dates, and constraints from the source.
- Separate confirmed decisions from discussion points, ideas, and open questions.
- Convert vague follow-ups into action items only when there is a clear task. Otherwise, place them under Open Questions or Follow-up / Next Meeting.
- Include source context briefly when it helps explain why an action, risk, or decision exists.

## Output Guidance

- Start with the structured meeting note, not a long explanation of the process.
- Use concise bullets and tables where they improve scanning.
- Prefer Markdown headings from the template.
- If the source is too thin to complete a section, keep the section and write `無` or `待確認` as appropriate.
- If the meeting contains sensitive or ambiguous claims, phrase them as source-supported observations rather than conclusions.
