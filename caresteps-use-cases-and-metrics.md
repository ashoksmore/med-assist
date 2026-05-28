# CareSteps: Problem Statement, Use Cases, and Metrics

## 1) Judge-ready problem statement

Patients often leave visits with instructions written in clinical language. They may not fully understand medication changes, follow-up steps, or warning signs, and they frequently forget what to ask at the next visit. This leads to poor follow-through and lower adherence.

Our prototype, **CareSteps**, improves this workflow by converting synthetic visit notes into:
- a plain-language summary,
- a clear action checklist, and
- a personalized "Questions to Ask Your Clinician" list that patients can bring to the next encounter.

The goal is to improve patient understanding and readiness to act, especially across age groups (young adults, adults, seniors), while keeping a human reviewer in the loop.

## 2) Solution summary

**Input:** one synthetic visit/discharge note (Synthea-style)  
**AI tasks:** summarize, simplify jargon, extract actions, generate probable clarification questions  
**Output to patient:**
- What changed today
- What to do next
- When to call for help
- Top 6 suggested questions (patient picks top 3 + optional custom question)

**Shareable artifact:** "Visit Question Card" patients can show in clinic.

**Workflow fit:** Companion to after-visit instructions to improve patient follow-through between visits.

## 3) Use cases (before vs after)

### Use case A: Young adult (new diagnosis, first long-term medication)
- **Before:** Patient reads raw note, understands only part of dosing and follow-up.
- **After:** Patient sees simple summary, picks 3 questions:
  - "What side effects should make me call right away?"
  - "What if I miss one dose?"
  - "When should I repeat my blood test?"

### Use case B: Working adult (multiple tasks, low time)
- **Before:** Patient misses one of the follow-up tasks.
- **After:** Checklist separates this week vs this month tasks, plus 3 practical questions to confirm priorities.

### Use case C: Senior (caregiver support needed)
- **Before:** Instructions are dense; caregiver is unsure what to monitor.
- **After:** Large, chunked summary includes caregiver notes and a question card:
  - "Can you explain this in plain words for my caregiver?"
  - "Which symptom means emergency vs call clinic?"
  - "Can we simplify the medication schedule?"

## 4) What we will deliver today (MVP)

- One demo flow from note input to final output.
- Three synthetic patient examples (young/adult/senior).
- Before/after view: raw note vs CareSteps output.
- Human review step (Approve/Edit) before final patient view.
- Download/copy "Visit Question Card."
- One metric slide with pilot results.

## 5) Evaluation metrics and how we will measure them

## Primary KPI

**Task Comprehension Accuracy (%)**

Definition: Percent of required care actions correctly recalled by participant after reading the material.

Formula:

```text
Comprehension Accuracy = (points earned on gold checklist / total checklist points) * 100
```

Method:
- 5-person pilot, within-subject.
- Each participant reviews both:
  - Condition A: raw clinical note (before)
  - Condition B: CareSteps output (after)
- Same 3 fixed questions, same synthetic case facts.

## Secondary KPIs

1. **Question Coverage Score (%)**
   - Measures whether generated questions cover critical categories:
     - medications,
     - follow-up tests/appointments,
     - warning signs,
     - lifestyle/next steps.
   - Formula:

```text
Coverage = (covered categories / 4) * 100
```

2. **Question Usefulness Rating (1-5)**
   - Human raters score: "Would this question help the patient have a better follow-up conversation?"
   - Report average score per case.

3. **Unsupported Claim Rate (%)**
   - Any summary bullet or suggested question not traceable to the source note.
   - Target: 0% after human review.
   - Formula:

```text
Unsupported Claim Rate = (unsupported items / total generated items) * 100
```

4. **Time to Readiness (seconds)**
   - Time from opening output to selecting top 3 questions and correctly stating next steps.

## Suggested success thresholds (prototype-level)

- Comprehension Accuracy: +25 percentage-point improvement vs raw note
- Question Coverage: >= 75%
- Question Usefulness: >= 4.0 / 5
- Unsupported Claim Rate: 0% after review
- Time to Readiness: faster than raw-note condition

## 6) Trust, safety, and transparency

- Synthetic data only.
- AI output labeled as draft support, not medical advice.
- Human reviewer approves final output.
- Source anchoring for each key action/question.
- Clear limitation message when note lacks needed details.

## 7) One-paragraph script for judges

CareSteps helps patients understand and act on visit instructions. We convert a synthetic clinical note into a plain-language summary, an action checklist, and a personalized question card patients can bring to their next visit. To evaluate impact without historical production data, we run a within-subject pilot comparing raw notes vs our output on the same cases. Our primary metric is task comprehension accuracy; secondary metrics include question coverage, usefulness, unsupported claim rate, and time to readiness. This demonstrates practical value, safety, and measurable workflow improvement in one day.
