# Final Submission

Team name: [TBD]

Members: [TBD]

Track: Improve Patient Experience

Project title: MedAssist - Age-Aware Plain Summary and Question Card

## Problem Statement

Patients often receive follow-up instructions in language that is difficult to understand. As a result, they may miss medication, lab, and appointment steps and may not know what questions to ask in follow-up visits. We target this communication gap with a patient-centered, plain-language workflow using synthetic data only.

## Solution Summary

MedAssist converts a synthetic clinical note into:
- a plain-language summary,
- a prioritized action checklist, and
- a personalized list of probable questions the patient can ask their clinician.

The patient selects top questions to create a shareable "Visit Question Card." A human reviewer approves/edit before final output.

Workflow fit:
- Designed as a companion to post-visit communication so patients and caregivers can follow through after leaving clinic.

Operational value:
- Improves readiness for follow-up conversations and may reduce avoidable clarification call-backs.

## Links

Repo: https://github.com/ashoksmore/med-assist

Demo: [TBD]

Artifact: [TBD]

Backup screenshot or recording: [TBD]

## Data Inputs

- Synthea synthetic patient note snippets (primary)
- Optional RxNorm/RxNav medication terminology lookup
- No PHI, no customer-identifiable data

## AI Usage

- Summarization of raw note to plain language
- Extraction of tasks, timelines, and warning signals
- Generation of probable clarification questions
- Age-band style adaptation (young adult, adult, senior)

## Trust, Safety, Transparency

Guardrail:
- Source-anchored output and unsupported-claim checks
- "Conversation starters, not medical advice" label for suggested questions

Human review:
- Reviewer checks and approves/edit output before patient-facing display

Limitations:
- Prototype evaluates understanding proxies, not long-term real adherence outcomes
- Small pilot during hackathon timeframe

## Success Metric

Primary metric:
- Task comprehension accuracy (%) against a predefined gold checklist.

Secondary metrics:
- Question coverage score (% of required categories represented)
- Question usefulness rating (1-5)
- Unsupported claim rate (%)
- Time to readiness (seconds to choose top questions and explain next steps)

## What We Built Today

- End-to-end before/after prototype flow
- 3 synthetic age-band examples
- Plain-language summary + action checklist + question card
- Human review gate
- Pilot scoring sheet and evaluation protocol

## Future Work

- Expand to multilingual support
- Validate with broader outpatient pilot
- Integrate with appointment reminder workflows
- Measure longer-term behavioral adherence endpoints

## Third-Party Credits

| Source | Use | Attribution |
|---|---|---|
| Synthea | Synthetic patient examples | https://github.com/synthetichealth/synthea |
| RxNorm/RxNav (optional) | Medication term normalization | https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html |
