# MedAssist Hackathon PPT (Editable)

Use this as the source script for your slides. Each section below maps to one slide.

---

## Slide 1 - Title

**MedAssist: Age-Aware Plain Summary and Question Card**  
Track: Improve Patient Experience  
Team: [Team Name]  
Members: [Member 1], [Member 2], [Member 3]

Speaker note:
MedAssist helps patients and caregivers better understand what to do after a visit by converting dense instructions into plain-language actions and questions.

---

## Slide 2 - Problem

**Patients leave visits with instructions that are hard to follow**

- Clinical notes are often dense and full of jargon
- Patients may miss meds, lab, and follow-up steps
- Many forget key questions to ask at the next visit

Pain for providers:
- More confusion and avoidable follow-up clarification calls

Speaker note:
The core gap is not diagnosis. It is follow-through and communication clarity after the visit.

---

## Slide 3 - Solution

**MedAssist turns one synthetic note into patient-ready output**

Input:
- Synthetic clinical note (Synthea-style)

Output:
- Plain-language summary
- Prioritized action checklist
- Personalized "Questions to Ask Your Clinician" list

Final artifact:
- Shareable "Visit Question Card"

Speaker note:
The patient picks top questions, and we preserve a simple artifact they can bring into follow-up care conversations.

---

## Slide 4 - Why It Matters

**Expected value**

- Better understanding of what changed and what to do next
- Better readiness for follow-up conversations
- More support for caregivers and age-specific communication
- Potential reduction in avoidable callback confusion

Speaker note:
We focus on practical patient experience improvements that can fit post-visit communication workflows.

---

## Slide 5 - Demo Flow

**End-to-end flow**

1. Synthetic note input
2. AI generation (summary + checklist + questions)
3. Guardrail checks and safety labeling
4. Human reviewer approve/edit
5. Final patient-facing question card

Visual:
- Before/After panel: raw note vs MedAssist output

Speaker note:
Show one complete golden-path case live. Keep this flow crisp and reproducible.

---

## Slide 6 - Trust, Safety, and Transparency

**Safety by design**

- Synthetic data only (no PHI in demo)
- "Conversation starters, not medical advice" label
- Human approve/edit gate before patient-facing output
- Unsupported-claim checks against source note
- Clear limitation message when source detail is missing

Speaker note:
We do not automate medical decision-making; we support communication quality with a human in the loop.

---

## Slide 7 - Technical Architecture

**Current stack**

- Frontend: React
- Backend: FastAPI
- AI: Azure OpenAI API

Backend modules:
- `generate` route
- prompt builder
- Azure OpenAI service
- guardrails service
- review service
- metrics service

Current persistence:
- In-memory placeholder (database deferred for MVP speed)

Speaker note:
Architecture is modular so we can add persistence and production hardening after hackathon validation.

---

## Slide 8 - Evaluation Method

**Pilot design (prototype-level)**

- n = 5, within-subject, counterbalanced order
- Compare:
  - Condition A: raw clinical note
  - Condition B: MedAssist output
- Same synthetic case facts and 3 fixed evaluation questions
- Gold checklist scoring rubric from `evaluation-protocol.md`

Speaker note:
This gives us measurable signal on understanding and readiness, even without long-term clinical outcomes yet.

---

## Slide 9 - Metrics and Targets

**Primary KPI**

- Task comprehension accuracy (%)

**Secondary KPIs**

- Question coverage score (%)
- Question usefulness rating (1-5)
- Unsupported claim rate (%)
- Time to readiness (seconds)

**Prototype targets**

- +25 percentage-point comprehension improvement vs raw note
- >= 75% question coverage
- >= 4.0 usefulness
- 0% unsupported claims after review

Speaker note:
Anchor your results discussion around comprehension and safety together.

---

## Slide 10 - Results, Limits, and Next Steps

Results:
- Raw note comprehension: [X%]
- MedAssist comprehension: [Y%]
- Median time: [A min] -> [B min]
- Readability grade: [M] -> [N]

Limitations:
- Small pilot sample
- Synthetic-only demo
- Measures understanding proxy, not long-term adherence outcomes

Next steps:
- Broader outpatient validation
- Multilingual support
- Workflow integration with reminders/follow-up systems

Speaker note:
End with practical roadmap and clear safety posture.

---

## Optional Backup Slide - Judge Q&A

**One-sentence judge answer**

MedAssist improves post-visit follow-through by converting synthetic clinical notes into human-reviewed plain summaries, action checklists, and question cards, and we measure impact through comprehension, safety, and readiness metrics.
