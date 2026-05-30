# Patient Insights API

A FastAPI backend that turns raw patient data into two LLM-generated artifacts
using Azure OpenAI:

1. **Patient Summary**
2. **Patient Probable Questions**

Both are returned together in a single array.

## Architecture

```
GET /patients/insights
        │
        ▼
  load patient1.json
        │
        ▼
 ┌──────────────────────────────────────────────┐
 │  Azure LLM Service Layer (AzureLLMService)     │
 │  generate(prompt, patient_data) -> dict        │
 └──────────────────────────────────────────────┘
   1) (patient data + PROMPT1) ─► Patient Summary
   2) (Patient Summary + PROMPT2) ─► Probable Questions
        │
        ▼
  response: [ patient_summary, probable_questions ]
```

| Piece | File |
| --- | --- |
| Azure LLM Service Layer | `app/services/azure_llm.py` |
| Route / orchestration | `app/routers/patient.py` |
| Prompts (prompt1, prompt2) | `app/prompts/prompts.py` |
| Sample patient data | `app/data/patient1.json` |
| Config & DI | `app/config.py`, `app/dependencies.py` |
| App entry point | `app/main.py` |

The service layer is constructed once (cached) with the Azure endpoint, API key,
deployment, and API version, then exposes a single async `generate(prompt,
patient_data)` method. It forces JSON output (`response_format=json_object`) so
each step reliably returns a parseable object.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in your Azure details
```

## Run

```bash
uvicorn app.main:app --reload
```

Then call the endpoint:

```bash
curl http://127.0.0.1:8000/patients/insights
```

Interactive docs: http://127.0.0.1:8000/docs

## Response shape

```json
[
  { "patient_id": "P-10293", "name": "Jane Doe", "...": "patient summary" },
  { "patient_id": "P-10293", "probable_questions": [ { "question": "..." } ] }
]
```

## Notes

- Set `AZURE_OPENAI_DEPLOYMENT` to the **deployment name** in your Azure
  resource, not the base model name.
- `AZURE_OPENAI_API_VERSION` defaults to a GA version; bump it if you need newer
  features.
- Swap `app/data/patient1.json` or extend the route to accept a patient ID /
  request body to make it dynamic.
