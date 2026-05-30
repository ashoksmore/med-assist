# MedAssist 3-Minute Deck (Short Version)

Use this version when total time is capped at 3 minutes (including demo).

---

## Total Timing Plan (180 seconds)

- Slide 1 (Title + one-liner): 15s
- Slide 2 (Problem): 25s
- Slide 3 (Data choice - Synthea): 20s
- Slide 4 (Use-case flow): 30s
- Slide 5 (Trust + architecture): 20s
- Slide 6 (Metrics + result target): 20s
- Live Demo clip/walkthrough: 40s
- Close (ask + next step): 10s

---

## Slide 1 - Title (15s)

**MedAssist: Age-Aware Plain Summary and Question Card**  
Track: Improve Patient Experience  
Team: [Team Name]

Talk track:
MedAssist helps patients understand exactly what to do after a visit by turning complex instructions into plain actions and better follow-up questions.

---

## Slide 2 - Problem (25s)

**The gap is follow-through, not diagnosis**

- Post-visit instructions are often dense and clinical
- Patients miss meds/labs/follow-up steps
- Patients and caregivers forget what to ask next

Talk track:
This leads to confusion and avoidable follow-up burden. We focus on communication clarity after the visit.

---

## Slide 3 - Data Choice (20s)

**Why we chose Synthea dataset**

- Fully synthetic patient notes (no PHI)
- Fast to curate for hackathon timelines
- Supports age-band scenarios (young/adult/senior)
- Aligned with trust and safety constraints

Talk track:
We intentionally use Synthea so our demo is safe, realistic enough for workflow testing, and easy to evaluate quickly.

---

## Slide 4 - Use-Case Flow (30s)

**One note in -> patient-ready output out**

Use case:
- Patient leaves clinic with dense instructions
- MedAssist converts note into:
  - plain-language summary,
  - prioritized action checklist,
  - suggested questions to ask doctor
- Patient picks top 3 questions
- Reviewer approves/edits
- Final Visit Question Card is shared

Flow:
- Note input -> AI generation -> guardrails -> human review -> patient card

Talk track:
The key outcome is better follow-through: patients know what to do next and what to ask at follow-up.

---

## Slide 5 - Trust + Architecture (20s)

**Safety + practical build**

Safety:
- Synthetic data only
- "Conversation starters, not medical advice"
- Unsupported-claim checks
- Human approve/edit gate

Tech:
- React frontend
- FastAPI backend
- Azure OpenAI integration

Talk track:
This is intentionally lightweight for hackathon speed and production-aware modularity.

---

## Slide 6 - Metrics + What Success Looks Like (20s)

**Primary KPI:** Task comprehension accuracy (%)

Secondary:
- Question coverage
- Usefulness rating
- Unsupported claim rate
- Time to readiness

Prototype success target:
- +25 percentage-point comprehension vs raw note
- 0% unsupported claims after review

Talk track:
We measure both usefulness and safety, not just model output quality.

---

## Demo Script (40s)

1. Show raw synthetic note (5s)
2. Click Generate (5s)
3. Show summary + checklist + suggested questions (15s)
4. Show reviewer approve/edit step (10s)
5. Show final question card output (5s)

Backup plan:
- Keep one screenshot each for before/after in case of network delay.

---

## Final Close (10s)

MedAssist improves post-visit understanding and readiness with a human-reviewed, measurable workflow.  
Next step: validate with a broader outpatient pilot and multilingual support.

