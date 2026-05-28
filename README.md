# MedAssist

MedAssist is a hackathon prototype for improving patient follow-through after a visit.
It transforms a synthetic clinical note into:

- a plain-language summary,
- a prioritized action checklist, and
- a personalized "Visit Question Card" for the next clinician conversation.

This repository currently contains submission-ready documentation artifacts for the
athenahealth hackathon track: **Improve Patient Experience**.

## Repository Contents

- `caresteps-team-proposal-draft.md` - team proposal draft
- `caresteps-final-submission-draft.md` - final submission draft
- `caresteps-use-cases-and-metrics.md` - judge-facing problem/use case/metrics narrative
- `evaluation-protocol.md` - pilot scoring protocol and rubric

## Project Scope (Current)

- Uses synthetic case data only (Synthea-style notes)
- No PHI ingestion
- Human review gate before patient-facing output
- Focus on understanding/readiness metrics rather than long-term clinical outcomes

## Evaluation Approach

Primary KPI:
- Task comprehension accuracy (%), measured with a gold checklist in a small
  within-subject pilot.

Secondary KPIs:
- Question coverage score (%)
- Question usefulness rating (1-5)
- Unsupported claim rate (%)
- Time to readiness (seconds)

See `evaluation-protocol.md` for full methodology, score sheet, and reporting format.

## Status

This repo is currently documentation-first and hackathon-focused.
Implementation code can be added in a future phase.

## Contributing

1. Open an issue or proposal note describing the change.
2. Keep edits focused and easy to review.
3. For methodology changes, update all related docs for consistency.

## License

Add your license information here (for example, MIT, Apache-2.0, or proprietary).
