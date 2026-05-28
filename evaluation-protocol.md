# CareSteps — Evaluation Protocol (Pilot)

Use this document to answer judges: **what metric, how measured, and what “correct” looks like.**

**Primary metric:** Task comprehension accuracy (%) vs a gold-standard action checklist  
**Design:** Within-subject, counterbalanced order — participants review both conditions, with randomized order (raw first or plain first).  
**Pilot size:** n = 5 volunteers (not the person who wrote the plain summary)

---

## 1. Synthetic test case (shared across all age bands)

**Patient (Synthea-style, synthetic):** Jordan Lee, DOB 1980-03-14 (age 45 at visit)  
**Visit:** Primary care follow-up — type 2 diabetes, blood pressure  
**Same clinical facts** for young / adult / senior demos; only **tone and format** change by age band.

### Raw clinical note (Condition A — “before”)

```text
DISCHARGE / VISIT SUMMARY — SYNTHETIC

Patient: Jordan Lee (MRN SYN-88421)
Date of service: 2026-05-28
Provider: Dr. A. Patel, MD

ASSESSMENT:
1. Type 2 diabetes mellitus — suboptimal glycemic control; A1c 8.2% (2026-05-10).
2. Essential hypertension — controlled on current regimen.

PLAN / INSTRUCTIONS:
- Start metformin HCl 500 mg PO BID with meals. Counsel on GI upset; if tolerated,
  increase to 1000 mg PO BID at follow-up visit if clinically appropriate.
- Continue lisinopril 10 mg PO daily.
- Home glucose monitoring: fasting and 2-hour post-prandial checks 3x weekly; log results.
- Repeat HbA1c and CMP in 12 weeks (order placed; patient to schedule at lab).
- Nutrition referral placed; Mediterranean-style diet, limit refined carbohydrates.
- Return to clinic in 4 weeks for medication titration and symptom review.
- Call clinic or go to ED for: persistent vomiting, signs of lactic acidosis (severe fatigue,
  rapid breathing, muscle pain), blood glucose >400 mg/dL, or SBP >180 despite meds.

Follow-up appointment: 2026-06-25 10:00 — Primary Care, Building A.
```

---

## 2. Gold-standard action checklist (answer key)

Scorers mark each item **correct (1)**, **partial (0.5)**, or **incorrect (0)** when the participant’s answers (written or spoken) are compared to this list.

| # | Required action / fact | Accept if participant says… |
|---|------------------------|-------------------------------|
| G1 | **New medicine:** metformin, 500 mg, **twice daily with meals** | Metformin started; twice a day with food; 500 mg BID |
| G2 | **Continue:** lisinopril 10 mg **once daily** | Still on lisinopril; don’t stop blood pressure med |
| G3 | **Home monitoring:** check blood sugar at home (fasting + after meals), **about 3x per week**, keep a log | Test sugar at home; write down results; fasting and after meals |
| G4 | **Lab:** repeat **A1c** (and/or “blood work”) in **~12 weeks**; patient must **schedule** lab | Blood test in 3 months; A1c recheck; go to lab to schedule |
| G5 | **Appointment:** return to clinic in **4 weeks** (≈ 2026-06-25 acceptable) | Follow-up visit in one month; June 25 appointment |
| G6 | **Lifestyle:** diet change / nutrition referral (lower carbs, healthier eating) | See nutrition; eat healthier; less sugar/carbs |
| G7 | **When to call doctor (≥2 of):** vomiting, very high sugar (>400), very high BP, serious side effects / “acidosis” symptoms | Don’t have to use medical terms; must capture “call if worse” with examples |

**Comprehension score (primary KPI):**

```text
Score = (sum of item points) / (7 × 1.0) × 100%
```

Example: 6.5 / 8 = **81%**

---

## 3. Three evaluation questions (ask every participant)

Read these **after** each condition (raw note OR plain summary). Answers may be **written or spoken**; scorers use the gold checklist above.

### Q1 — Medicines

**Question:**  
*What medicine changes were made today? How should you take each relevant medicine?*

**Gold answer (full credit = G1 + G2):**
- **Started** metformin 500 mg, **two times per day with meals**.
- **Keep taking** lisinopril 10 mg **once every day** (blood pressure).

**Partial credit examples:**
- “New diabetes pill twice a day” (no dose or with-meals) → G1 partial  
- “Take blood pressure med” (no daily) → G2 partial  

---

### Q2 — Follow-up tasks (labs, visits, monitoring)

**Question:**  
*What should you do in the next 1–3 months for follow-up (appointments, labs/tests, home monitoring, other steps)?*

**Gold answer (full credit = G3 + G4 + G5 + G6):**
- Check blood sugar at home (fasting and after meals), **several times per week**, **write down results**.
- Get **blood work / A1c** rechecked in about **12 weeks** (schedule at lab).
- **Clinic visit in 4 weeks** (e.g., June 25).
- **Nutrition / diet** help — eat healthier, fewer refined carbs.

**Partial credit:** mentions “follow up” without timing or misses lab vs visit distinction.

---

### Q3 — Safety / when to seek help

**Question:**  
*When should you call your clinic or seek urgent care? Name at least two situations.*

**Gold answer (G7 = 1 if ≥2 valid triggers from list):**
- Persistent **vomiting**
- Signs of serious metformin reaction / **very sick**, muscle pain, breathing problems (lay terms OK)
- Blood sugar **very high** (e.g., over 400)
- Blood pressure **very high** (e.g., over 180) despite meds
- **Emergency** if severe/worsening — OK to say “call or go to ER if…”

**Partial credit:** only one trigger, or vague “if you feel bad” with no examples.

---

## 4. Scoring rubric (quick reference)

| Response quality | Points per gold item |
|------------------|----------------------|
| Correct and specific | 1.0 |
| Partially correct (right idea, missing dose/time) | 0.5 |
| Missing or wrong | 0 |

Note: Unsupported claims are scored as a **separate model-output fidelity metric**, not mixed into participant comprehension scoring.

---

## 5. Secondary metrics (record on score sheet)

| Field | How to record |
|-------|----------------|
| **Time to answer** | Stopwatch: start when they begin reading → stop when Q1–Q3 answered |
| **Readability (automated)** | Run raw note vs plain output through Flesch-Kincaid; record grade level |
| **Confidence (optional)** | 1–5: “I know what to do next week” — after each condition |
| **Unsupported claims** | Count bullets in plain output not in source (target **0** after human review) |

### Model-output fidelity metric (separate from comprehension)

Use this formula for the generated plain output:

```text
Unsupported Claim Rate = (unsupported generated items / total generated items) * 100
```

Report this separately from participant comprehension to avoid mixing model quality with participant recall.

### Score sheet (one participant)

```text
Participant ID: P___   Order: [ ] Raw first  [ ] Plain first
Age band shown (if applicable): [ ] 25  [ ] 45  [ ] 70

Condition: [ ] A Raw  [ ] B Plain
Time (min:sec): _______
Q1 items: G1 ___  G2 ___
Q2 items: G3 ___  G4 ___  G5 ___  G6 ___
Q3 items: G7 ___
Comprehension %: _______
Confidence 1-5: ___

(Then repeat for second condition)
```

---

## 6. Plain-language “after” reference (Condition B — for builders)

Your prototype should cover **all gold items**. Example target output (adult band):

```text
YOUR VISIT SUMMARY — plain language (synthetic demo)

What changed today
• You started a diabetes medicine called metformin (500 mg).
  Take it twice a day with breakfast and dinner.
• Keep taking your blood pressure medicine lisinopril (10 mg) once every morning.

What to do this month
• Check your blood sugar at home 3 times a week (before breakfast and 2 hours after a meal). Write the numbers down.
• Book a lab visit for blood work and A1c within the next 12 weeks.
• Come back to the clinic on June 25 at 10:00 AM (4-week check-in).
• A nutrition visit was ordered — focus on fewer sugary/refined carbs.

When to call us or get urgent help
• Throwing up and cannot keep fluids down
• Feeling very weak, muscle pain, or breathing fast
• Blood sugar over 400
• Blood pressure over 180
• Any symptoms that feel severe or sudden — call the clinic or go to the ER

[Human reviewer: Approve / Edit]  Sources: linked to lines in clinical note above.
```

**Age-band tweaks (same facts):**
- **Young (~25):** shorter bullets, “add reminders to your phone,” optional emoji-free checklist  
- **Adult (~45):** as above  
- **Senior (~70):** larger sections, **“caregiver: help with med box and lab scheduling,”** repeat critical warnings once  

---

## 7. How to report results (one slide for judges)

```text
Metric: Task comprehension accuracy (% of gold checklist items correct)

Method: n=5 within-subject pilot; raw clinical note vs plain-language + checklist;
         3 fixed questions; dual scorers; synthetic Synthea-style case only.

Results (fill after pilot):
  Raw note:    ___% comprehension, median time ___ min
  Plain output: ___% comprehension, median time ___ min
  Readability: grade ___ → grade ___

Limitation: Proxy for adherence (understanding), not 90-day refill data.
Next step:   Outpatient pilot with IRB and real adherence endpoints.
```

---

## 8. One-sentence answer for judges

> We measure **task comprehension accuracy** by scoring answers to **three fixed questions** against a **7-item gold checklist** derived from the same synthetic visit note, comparing the **raw clinical summary** to our **human-reviewed plain-language output** in a **5-person within-subject pilot**, with **time-to-answer** and **readability grade** as secondary metrics and a separate **unsupported-claim rate** for model-output fidelity.
