# Team Proposal

Team name: [TBD]

Members: [TBD]

Track: Improve Patient Experience

Project title: MedAssist - Age-Aware Plain Summary and Question Card

## Problem

User: Patients (and caregivers) leaving a visit with medication and follow-up instructions.

Pain point: Clinical summaries are hard to understand, patients miss action steps, and many forget to ask important clarifying questions in follow-up encounters.

Problem statement: For patients who need to follow medication, testing, and follow-up plans, our prototype improves understanding and adherence readiness by transforming synthetic visit notes into plain-language actions and personalized "questions to ask" for the next clinician conversation.

## Solution

What we will build:
- Plain-language visit summary from synthetic note.
- Action checklist (medications, follow-up, warning signs, lifestyle).
- Suggested question list (6 prompts) grouped by:
  - medications,
  - tests/appointments,
  - warning signs,
  - daily routine/lifestyle.
- Patient selects top 3 questions plus optional custom question.
- Shareable "Visit Question Card."

What we will demo:
- 3 synthetic cases (young adult, adult, senior).
- Before/after comparison: raw note vs MedAssist output.
- Human reviewer approve/edit step before final patient view.
- One evaluation slide with pilot metrics.
- Workflow fit for post-visit patient communication.

What we will not build:
- Real EHR integration.
- PHI ingestion.
- Autonomous diagnosis/treatment advice.
- Longitudinal production adherence tracking.

## Data

Data source:
- Synthea synthetic records (primary).
- Optional RxNorm/RxNav for medication term normalization.

Why it is synthetic or de-identified:
- Demo uses synthetic cases only; no real patient identifiers or production exports.

## AI Usage

Where AI is used:
- Summarization of raw clinical note.
- Jargon simplification.
- Extraction of follow-up actions and warning signs.
- Generation of probable patient clarification questions.

What AI outputs:
- Plain-language summary.
- Action checklist.
- Candidate question list.

What a human reviews:
- Accuracy of medication/follow-up details.
- Safety wording and unsupported claims.
- Final approve/edit before patient-facing output.

## Trust / Safety / Transparency

Guardrail:
- Source-anchored generation (key output tied to note content).
- "Conversation starters, not medical advice" label on question list.
- Block unsupported treatment recommendations.

Known limitations:
- Measures understanding proxies, not long-term real-world adherence outcomes.
- Small pilot sample during hackathon.
- Performance may vary by note quality.

## Success Metric

Metric:
- Primary: Task comprehension accuracy (%) against a gold checklist.
- Secondary:
  - Question coverage score (% critical categories represented),
  - Question usefulness rating (1-5),
  - Unsupported claim rate (%),
  - Time to readiness (seconds).

Why it matters:
- Better comprehension and better questions increase patient readiness to follow care plans and reduce avoidable confusion at follow-up.
- This aligns with post-visit communication workflows where clear next steps lower unnecessary callbacks.

## Help Needed

Access blockers:
- Confirm any preferred organizer data kit location and API availability.

TA questions:
- Is this framing acceptable for Track 1 judging?
- Any preferred format for reporting pilot metrics in final submission?
